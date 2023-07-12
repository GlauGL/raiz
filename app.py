from flask import Flask, render_template, request, flash
import os
import sys
import secrets
sys.path.insert(0,f'{os.getcwd()}')
from calcula import calcula_raiz


app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex()

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        numero = int(request.form.get("campo_numero"))
        flash(f"{calcula_raiz(numero)}")
        resultado =calcula_raiz(numero)
        return render_template("index.html",resultado=resultado)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

