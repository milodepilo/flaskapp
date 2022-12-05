# Import what we need from flask
from flask import Flask, render_template, redirect

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/', methods=["GET"])
def index():
    return 'Hello, world!!, i did it!'

@app.route('/cow')
def cow():
    return 'MOoooOo!'


