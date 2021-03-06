import pandas as pd
import numpy as np
import requests
import time

rounds = []
race = pd.read_csv("../webpages/dash/static/Data/RaceData.csv")
for year in np.array(race.Season.unique()):
    rounds.append([year, list(race[race.Season == year]['Round'])])

start_time = time.time()
driver_standings = {"Season": [], "Round": [], "Driver": [], "DriverPoints": [], "DriverWins": [], "DriverStandings": []}

for i in list(range(len(rounds))):
    for j in rounds[i][1]:
        url = "https://ergast.com/api/f1/{}/{}/driverStandings.json"
        request = requests.get(url.format(rounds[i][0], j))
        json = request.json()
        for entry in json['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']:
            try:
                driver_standings['Season'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['season']))
            except:
                driver_standings['Season'].append(None)
            try:
                driver_standings['Round'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['round']))
            except:
                driver_standings['Round'].append(None)                              
            try:
                driver_standings['Driver'].append(entry['Driver']['driverId'])
            except:
                driver_standings['Driver'].append(None)  
            try:
                driver_standings['DriverPoints'].append(int(entry['points']))
            except:
                driver_standings['DriverPoints'].append(None)
            try:
                driver_standings['DriverWins'].append(int(entry['wins']))
            except:
                driver_standings['DriverWins'].append(None)       
            try:
                driver_standings['DriverStandings'].append(int(entry['position']))
            except:
                driver_standings['DriverStandings'].append(None)

df = pd.DataFrame(driver_standings)
df = df.reindex(columns=list(driver_standings.keys()))
df.to_csv("../webpages/dash/static/Data/DriverStandings.csv", index = False)
print("--- %s seconds ---" % (time.time() - start_time))