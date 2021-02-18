from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json, csv, pandas

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verstappen')
def getmax():
    return render_template('driverPages/verstappen.html', driver_name='max_verstappen', driver_code='VER')

@app.route('/vettel')
def getvet():
    return render_template('driverPages/vettel.html', driver_name='vettel', driver_code='VET')

@app.route('/russell')
def getrus():
    return render_template('driverPages/russell.html', driver_name='russell', driver_code='RUS')

if __name__ == "__main__":
    app.run(debug=True)