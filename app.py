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
        upphaedd = request.form.get("upphaedd")
        tekstur = request.form.get("tekstur")
        dato = request.form.get("dato")

        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = """
                INSERT INTO KASSAKLADDA 
                (FRÁ_KONTO, TIL_KONTO, UPPHÆDD, TEKSTUR, DATO, STATUS)
                VALUES 
                (:fra_konto, :til_konto, :upphaedd, :tekstur, TO_DATE(:dato, 'YYYY-MM-DD'), :status)
            """

            cursor.execute(sql, {
                "fra_konto": int(fra_konto),
                "til_konto": int(til_konto),
                "upphaedd": float(upphaedd),
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

if __name__ == "__main__":
    app.run(debug=True)