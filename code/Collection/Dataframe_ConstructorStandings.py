import pandas as pd
import numpy as np
import requests
import time

rounds = []
race = pd.read_csv("../webpages/dash/static/Data/RaceData.csv")
for year in np.array(race.Season.unique()):
    rounds.append([year, list(race[race.Season == year]["Round"])])
rounds = rounds[8:]
start_time = time.time()
constructor_standings = {"Season": [], "Round": [], "Constructor": [], "ConstructorPoints": [], "ConstructorWins": [], "ConstructorStandings": []}

rows = 0
for i in list(range(len(rounds))):
    for j in rounds[i][1]:
        url = "https://ergast.com/api/f1/{}/{}/constructorStandings.json"
        request = requests.get(url.format(rounds[i][0], j))
        json = request.json()
        for entry in json['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']:
            try:
                constructor_standings['Season'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['season']))
            except:
                constructor_standings['Season'].append(None)
            try:
                constructor_standings['Round'].append(int(json['MRData']['StandingsTable']['StandingsLists'][0]['round']))
            except:
                constructor_standings['Round'].append(None)                              
            try:
                constructor_standings['Constructor'].append(entry['Constructor']['constructorId'])
            except:
                constructor_standings['Constructor'].append(None)  
            try:
                constructor_standings['ConstructorPoints'].append(int(entry['points']))
            except:
                constructor_standings['ConstructorPoints'].append(None)
            try:
                constructor_standings['ConstructorWins'].append(int(entry['wins']))
            except:
                constructor_standings['ConstructorWins'].append(None)       
            try:
                constructor_standings['ConstructorStandings'].append(int(entry['position']))
            except:
                constructor_standings['ConstructorStandings'].append(None)
            rows += 1

df = pd.DataFrame(constructor_standings)
df = df.reindex(columns=list(constructor_standings.keys()))
df.to_csv("../webpages/dash/static/Data/ConstructorStandings.csv", index = False)
print("--- %s seconds ---" % (time.time() - start_time))