from flask import Flask
app=Flask(__name__)

@app.route("/")
def rani():
    return "hyderabad"


@app.route("/hai")
def prameela():
    return "vijayawada"

if __name__=="__main__":
    app.run(debug=True)