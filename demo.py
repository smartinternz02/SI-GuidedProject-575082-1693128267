from flask import Flask

app = Flask(__name__)
@app.route("/")
def hi():
    return "welcome"


@app.route("/hello")
def hi1():
    return "hello world"


   

@app.route("/type/<desg>")
def desg(desg):
    return "welcome all" + desg + "to CAD CLASS"
if __name__=="__main__":
    app.run(debug=True)
