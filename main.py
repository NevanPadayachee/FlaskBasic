from flask import Flask, redirect, url_for

app = Flask(__name__)#instance of flask webapp

a=False

@app.route("/") #when app is run it will run idex
def index():
    return "<h1> hello world </h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    if a:
        return redirect(url_for("index"))
if __name__=="__main__":
    app.run()