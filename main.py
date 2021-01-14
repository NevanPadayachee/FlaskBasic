from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)#instance of flask webapp

a=False

@app.route("/") #when app is run it will run idex
def index():
    return render_template("index.html", content=["nev", "kev", "steve"])

#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}!"

#@app.route("/admin/")
#def admin():
#    if a:
#        return redirect(url_for("index"))

if __name__=="__main__":
    app.run()