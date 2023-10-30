import pymysql
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

datalogin = ()

app = Flask(__name__)

def dbconnect(dbname):
    db = pymysql.connect(host='localhost:3006', user='root', passwd="password", db=dbname, unix_socket="/tmp/mysql.sock")
    return db

def dbdisconnect(db):
    db.close()

def dbquery(db, sql):
    try:
        cur = db.cursor()
        cur.execute(sql) 
        alldata = cur.fetchall()
        return alldata
    except Exception as e:
        print(e)
    cur.close()
    db.close()

@app.route("/")
def principale():
    return "Prova<br>vai a <a href='/index'>parola index</a>"

@app.route("/index")
def index():
    print("utente ha cliccato su link index")
    return render_template("index.html")

@app.route("/prova")
def funzioneprova():
    return render_template("paginaprova.html")

@app.route("/paglink")
def linkpage():
    p1 = request.args.get('param1') #testo
    p2 = request.args.get('keyparam') #esempio
    p3 = request.args.get('terzo') #nonsocosascrivere
    print("stampo in console i parametri", p1, p2, p3)
    return render_template("link.html", param_one=p1, param_two=p2, terz=p3)

@app.route("/formget")
def formgetpage():
    return render_template("form_con_get.html")

@app.route("/formgetparam")
def formgetpageparam():
    testo = request.args.get("campotesto")
    print("richiesta GET inviata client -> server con value", testo)
    return render_template("formparam.html", fieldtext=testo)

@app.route("/formpost")
def formpostpage():
    return render_template("form_con_post.html")

@app.route("/formpostparam", methods = ["post"])
def formpostvalue():
    testo = request.form.get("campotesto")
    print("richiesta POST inviata client -> server con value", testo)
    return render_template("formparam.html", fieldtext=testo)

@app.route("/logincondb")
def login():
    return render_template("login.html")

@app.route("/postlogin", methods = ["post"])
def getlogin():
    usr = request.form.get("txtusername")
    pwd = request.form.get("txtpassword")
    sql = "select * from Clienti where username='%s' and password='%s';" % (usr, pwd)
    print("login: ", sql)
    db = dbconnect("CentroCommerciale")
    datalogin=dbquery(db, sql)
    dbdisconnect(db)
    print(datalogin)
    if len(datalogin) == 0:
        return "Errore"
    else:
        return render_template("userdetail.html",user=datalogin[0])

@app.route("/userlist")
def userlist():
    sql = "select * from Clienti;"
    print("sql all users: ", sql)
    db = dbconnect("CentroCommerciale")
    data=dbquery(db, sql)
    dbdisconnect(db)
    print(data)
    return render_template("userlist.html",users=data)

@app.route("/userdetail")
def userdetail():
    if len(datalogin) == 0:
        return redirect("/logincondb", code=200)
    else:
        return render_template("userdetail.html",user=datalogin)

@app.route("/userinfo")
def userinfo():
    userid = request.args.get("id")
    sql = "select * from Clienti where id=%s;" % (userid)
    print("sql user info: ", sql)
    db = dbconnect("CentroCommerciale")
    data=dbquery(db, sql)
    dbdisconnect(db)
    print(data)
    return render_template("userdetail.html",user=data[0])


if __name__ == "__main__":
    app.run()
