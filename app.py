from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/termos")
def termos():
    return render_template("termos.html")

@app.route("/politica")
def politica():
    return render_template("politica.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
