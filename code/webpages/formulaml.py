from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json, csv, pandas

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teamlist')
def index():
    return render_template('teamlist.html')

@app.route('/driverlist')
def index():
    return render_template('driverlist.html')

@app.route('/driver/max_verstappen')
def getmax():
    return render_template('driver.html')

@app.route('/driver/albon')
def getalex():
    return render_template('driver.html')

@app.route('/team/redbull')
def getredbull():
    return render_template('team.html')

@app.route('/driver/leclerc')
def getcharles():
    return render_template('driver.html')

@app.route('/driver/vettel')
def getseb():
    return render_template('driver.html')

@app.route('/team/ferrari')
def getferrari():
    return render_template('team.html')

@app.route('/driver/perez')
def getsergio():
    return render_template('driver.html')

@app.route('/driver/stroll')
def getlance():
    return render_template('driver.html')

@app.route('/team/racingpoint')
def getracingpoint():
    return render_template('team.html')

@app.route('/driver/kevin_magnussen')
def getkevin():
    return render_template('driver.html')

@app.route('/driver/grosjean')
def getromain():
    return render_template('driver.html')

@app.route('/team/haasf1')
def gethaas():
    return render_template('team.html')

@app.route('/driver/latifi')
def getnicolas():
    return render_template('driver.html')

@app.route('/driver/russell')
def getgeorge():
    return render_template('driver.html')

@app.route('/team/williams')
def getwilliams():
    return render_template('team.html')

@app.route('/driver/giovinazzi')
def getantonio():
    return render_template('driver.html')

@app.route('/driver/raikkonen')
def getkimi():
    return render_template('driver.html')

@app.route('/team/alfaromeo')
def getalfaromeo():
    return render_template('team.html')

@app.route('/driver/hamilton')
def getlewis():
    return render_template('driver.html')

@app.route('/driver/bottas')
def getvaltteri():
    return render_template('driver.html')

@app.route('/team/mercedes')
def getmercedes():
    return render_template('team.html')

@app.route('/driver/ricciardo')
def getdaniel():
    return render_template('driver.html')

@app.route('/driver/ocon')
def getesteban():
    return render_template('driver.html')

@app.route('/team/renault')
def getrenault():
    return render_template('team.html')

@app.route('/driver/gasly')
def getpierre():
    return render_template('driver.html')

@app.route('/driver/kvyat')
def getkvyat():
    return render_template('driver.html')

@app.route('/team/alphatauri')
def getalphatauri():
    return render_template('team.html')

@app.route('/driver/sainz')
def getcarlos():
    return render_template('driver.html')

@app.route('/driver/norris')
def getlando():
    return render_template('driver.html')

@app.route('/team/mclaren')
def getmclaren():
    return render_template('team.html')

@app.route('/season')
def getseason():
    return render_template('season.html')

@app.route('/predictor')
def getprediction():
    return render_template('team.html')



if __name__ == "__main__":
    app.run()