from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json, csv, pandas

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('driver.html')

if __name__ == "__main__":
    app.run()