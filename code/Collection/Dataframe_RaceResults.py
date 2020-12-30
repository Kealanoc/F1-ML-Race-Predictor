import pandas as pd
import numpy as np
import requests
import time
start_time = time.time()
rounds = []
race = pd.read_csv("../Data/RaceData.csv")
for year in np.array(race.Season.unique()):
    rounds.append([year, list(race[race.Season == year]['Round'])])

RaceResults = {"Season": [], "Round": [], "Track": [], "Driver": [],
                "D.O.B": [], "Nationality": [], "Constructor": [], "Grid Pos": [],
                "Time": [], "Status": [], "Points": [], "Podium": [], "URL": []}

for i in list(range(len(rounds))):
    for j in rounds[i][1]:
        url = "https://ergast.com/api/f1/{}/{}/results.json"
        request = requests.get(url.format(rounds[i][0], j))
        json = request.json()

        for entry in json['MRData']['RaceTable']['Races'][0]['Results']:
            try:
                RaceResults["Season"].append(int(json['MRData']['RaceTable']['Races'][0]['season']))
                print(RaceResults["Season"])
            except:
                RaceResults["Season"].appned(None)
            try:
                RaceResults["Round"].append(int(json["MRData"]["RaceTable"]["Races"][0]["round"]))
            except:
                RaceResults["Round"].append(None)
            try:
                RaceResults["Track"].append(json['MRData']['RaceTable']['Races'][0]['Circuit']['circuitId'])
            except:
                RaceResults["Track"].append(None)
            try:
                RaceResults["Driver"].append(entry['Driver']['driverId'])
            except:
                RaceResults["Driver"].append(None)
            try:
                RaceResults['Nationality'].append(entry['Driver']['nationality'])
            except:
                RaceResults['Nationality'].append(None)
            try:
                RaceResults["Constructor"].append(entry["Constructor"]["constructorId"])
            except:
                RaceResults['Constructor'].append(None)
            try:
                RaceResults["D.O.B"].append(entry['Driver']['dateOfBirth'])
            except:
                RaceResults["D.O.B"].append(None)
            try:
                RaceResults["Grid Pos"].append(int(entry["grid"]))
            except:
                RaceResutls["Grid Pos"].append(None)
            try:
                RaceResults["Points"].append(int(entry["points"]))
            except:
                RaceResults["Points"].append(None)
            try:
                RaceResults["Time"].append(int(entry['Time']['millis']))
            except:
                RaceResults["Time"].append(None)
            try:
                RaceResults['Status'].append(entry['status'])
            except:
                RaceResults['Status'].append(None)
            try:
                RaceResults["Podium"].append(int(entry["position"]))
            except:
                RaceResults["Podium"].append(None)
            try:
                RaceResults['URL'].append(json['MRData']['RaceTable']['Races'][0]['url'])
            except:
                RaceResults['URL'].append(None)

RaceResults = pd.DataFrame(RaceResults)
print(RaceResults.shape)
RaceResults.to_csv("../Data/RaceResults.csv", index = False)
print("--- %s seconds ---" % (time.time() - start_time))