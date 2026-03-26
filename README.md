# 🏦 Bankaskipan GUI (Flask + Oracle)

## 📌 Lýsing

Henda verkætlan er ein GUI-loysn til eina bankaskipan, gjørd í Python við Flask og Oracle Database.

Skipanin gevur brúkaranum møguleika at:

* skráseta kassakladdu-postar
* síggja kontoavrit

GUI’ið ger tað møguligt at arbeiða við databasanum uttan at brúka SQL Developer.

---

## ⚙️ Krøv

Tú mást hava:

* Python 3
* Oracle Database (ella Oracle XE)
* SQL Developer (valfrítt)
* Git

---

## 📦 Installatión

### 1. Klona projectið

```bash
git clone https://github.com/DITT_USERNAME/sql-bank-gui.git
cd sql-bank-gui
```

### 2. Ger virtual environment

```bash
python -m venv .venv
```

### 3. Aktiver venv

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask oracledb python-dotenv
```

---

## 🔐 Environment variables

Ger eina `.env` fílu:

```env
SECRET_KEY=bank_secret_key

DB_USER=banki
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=1521
DB_SERVICE=xepdb1
```

---

## ▶️ Koyr applikatiónina

```bash
python app.py
```

Far til:
👉 http://127.0.0.1:5000

---

## 🧩 Funktiónir

### Kassakladda

* Skrásetir flytingar
* Goymir í databasu
* Brúkar trigger til ID

### Kontoavrit

* Vísir bókingar
* Lesur úr databasu
* Sorterar eftir nýggjastu fyrst

---

## 🗄️ Database

Skipanin brúkar:

* `KASSAKLADDA` tabell
* sequence til ID
* trigger til automatiskan KLADDA_ID

---

## 👨‍💻 Tøkni

* Python (Flask)
* HTML / CSS
* Oracle SQL
* Git / GitHub

---

## 📄 Viðmerking

`.env` er ikki við í GitHub av trygdarávum.
