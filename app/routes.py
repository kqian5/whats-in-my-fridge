import requests
from flask import render_template
from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    params = request.query_string
    #access api and search the params
    resp = requests.get()
    return render_template('results.html')

@app.route('/search')
def results():
    return render_template('search.html')