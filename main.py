# Import what we need from flask
from flask import Flask, render_template, redirect

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/', methods=["GET"])
def index():
    return render_template("index.html", title="Index")


@app.route('/cow')
def cow():
    return 'MOoooOo!'


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="about")