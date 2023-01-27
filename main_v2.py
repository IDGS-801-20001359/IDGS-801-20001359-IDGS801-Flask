
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo Flask cambios nuevos"

@app.route("/Hola")
def hola():
    return "Hola desde Hola"

@app.route("/nueva")
def nueva():
    return "Hola desde Nueva"

if __name__ == "__main__":
    app.run(debug=True,port=3000)
