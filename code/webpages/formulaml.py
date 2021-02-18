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
    return render_template('driverPages/verstappen.html')

if __name__ == "__main__":
    app.run(debug=True)