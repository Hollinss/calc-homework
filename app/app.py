"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from calc_mod.calculator import Calculator
app = Flask(__name__)

@app.route("/")
def index():
    """index routing"""
    return render_template('index.html')

