from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from db import get_connection

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/kassakladda", methods=["GET", "POST"])
def kassakladda():
    if request.method == "POST":
        fra_konto = request.form.get("fra_konto")
        til_konto = request.form.get("til_konto")
        upphædd = request.form.get("upphædd")
        tekstur = request.form.get("tekstur")
        dato = request.form.get("dato")

        if float(upphædd) <= 0:
            flash("Upphædd má vera størri enn 0", "danger")
            return redirect(url_for("kassakladda"))

        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = """
                INSERT INTO KASSAKLADDA
                (FRÁ_KONTO, TIL_KONTO, UPPHÆDD, TEKSTUR, DATO, STATUS)
                VALUES
                (:fra_konto, :til_konto, :upphædd, :tekstur, TO_DATE(:dato, 'YYYY-MM-DD'), :status)
            """

            cursor.execute(sql, {
                "fra_konto": int(fra_konto),
                "til_konto": int(til_konto),
                "upphædd": float(upphædd),
                "tekstur": tekstur,
                "dato": dato,
                "status": "Gjort"
            })

            connection.commit()
            flash("Kassakladdu-postur varð goymdur.", "success")
            return redirect(url_for("kassakladda"))

        except Exception as e:
            if connection:
                connection.rollback()
            flash(f"Feilur: {e}", "danger")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    return render_template("kassakladda.html")


@app.route("/kontoavrit")
def kontoavrit():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT KLADDA_ID, FRÁ_KONTO, TIL_KONTO, UPPHÆDD, TEKSTUR, DATO
            FROM KASSAKLADDA
            ORDER BY KLADDA_ID DESC
            FETCH FIRST 20 ROWS ONLY
        """)

        rows = cursor.fetchall()
        return render_template("kontoavrit.html", data=rows)

    except Exception as e:
        flash(f"Feilur: {e}", "danger")
        return redirect(url_for("home"))

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


@app.route("/um")
def um():
    return render_template("um.html")

@app.route("/kontoyvirlit", methods=["GET", "POST"])
def kontoyvirlit():
    connection = None
    cursor = None
    rows = []
    kunda_id = None

    if request.method == "POST":
        kunda_id = request.form.get("kunda_id")

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                SELECT KONTO_ID, KONTO_NR, KONTO_NAVN, SALDO
                FROM KONTO
                WHERE KUNDA_ID = :kunda_id
                ORDER BY KONTO_ID
            """, {"kunda_id": int(kunda_id)})

            rows = cursor.fetchall()

        except Exception as e:
            flash(f"Feilur: {e}", "danger")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    return render_template("kontoyvirlit.html", data=rows, kunda_id=kunda_id)

if __name__ == "__main__":
    app.run(debug=True)