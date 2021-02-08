from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json, csv, pandas

app = Flask(__name__)


@app.route('/driver')
def getjson():
    
    data = []

    with open('DriverStandings.csv') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            data.append(rows)
    
    with open('DriverStandings.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

    return jsonify(data)

@app.route('/driver')
def getapi():
    return render_template('driver.html')

if __name__ == "__main__":
    app.run()