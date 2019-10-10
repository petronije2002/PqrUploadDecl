from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello 1 Flask, on Azure App Service for Linux - updated version Checkingsafsafsfsa"

    