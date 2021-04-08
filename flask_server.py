from flask import Flask,redirect,url_for,render_template
import utils
app=Flask(__name__)


@app.route("/")
def homePage():
    my=utils.amazon()
    return  render_template("index.html",me=my)


if __name__=="__main__":
    app.run(debug=True)