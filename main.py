from flask import Flask, redirect, url_for,\
    render_template, request

app = Flask(__name__)#instance of flask webapp

a=False

@app.route("/") #when app is run it will run idex
def index():
    return render_template("index.html", content="Testing")

#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}!"

#@app.route("/admin/")
#def admin():
#    if a:
#        return redirect(url_for("index"))
@app.route("/login", methods =["POST","GET"])
def login():
    if request.method == "POST":
        user=request.form["nm"]
        return redirect(url_for("user", usr=user))

    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__=="__main__":
    app.run(debug=True )