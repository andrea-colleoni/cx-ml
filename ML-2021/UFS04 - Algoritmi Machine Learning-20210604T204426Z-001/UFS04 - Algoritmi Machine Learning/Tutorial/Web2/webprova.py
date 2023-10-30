from flask import Flask
from flask import render_template

app = Flask(__name__)

conta = 0

#http://localhost:5000/
@app.route("/")
def pippo():
    return render_template("index.html")

@app.route("/pluto")
def funzplut():
    return "sono pluto"

@app.route("/topo")
def funztopo():
    return "sono topo"

@app.route("/lino")
def lino():
    return "sono lino"


@app.route("/prova")
def funzionediprova():
    x = ""
    global conta
    conta = conta + 1
    if conta % 2 == 0:
        nome = "Antonio"
    else:
        nome = "Pippo"
    return render_template("paginaprova.html", x = nome)

if __name__ == "__main__":
    app.run()
