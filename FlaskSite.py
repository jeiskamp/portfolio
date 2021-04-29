import requests
from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__=="__main__":
    app.run(debug=True)
