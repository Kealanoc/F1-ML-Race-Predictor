import pandas as pd
import numpy as np
import requests
import time
start_time = time.time()
rounds = []
race = pd.read_csv("../Data/RaceData.csv")
for year in np.array(race.Season.unique()):
    rounds.append([year, list(race[race.Season == year]['Round'])])

RaceResults = {"Season": [], "Round": [], "Track_ID": [], "Driver": [],
                "DOB": [], "Nationality": [], "Constructor": [], "Grid": [],
                "Race_Time": [], "Status": [], "Points": [], "Podium": [], "URL": []}

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
                RaceResults["Track_ID"].append(json['MRData']['RaceTable']['Races'][0]['Circuit']['circuitId'])
            except:
                RaceResults["Track_ID"].append(None)
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
                RaceResults["DOB"].append(entry['Driver']['dateOfBirth'])
            except:
                RaceResults["DOB"].append(None)
            try:
                RaceResults["Grid"].append(int(entry["grid"]))
            except:
                RaceResults["Grid"].append(None)
            try:
                RaceResults["Points"].append(int(entry["points"]))
            except:
                RaceResults["Points"].append(None)
            try:
                RaceResults["Race_Time"].append(int(entry['Time']['millis']))
            except:
                RaceResults["Race_Time"].append(None)
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

df = pd.DataFrame(RaceResults)
df = df.reindex(columns=list(RaceResults.keys()))
df.to_csv("../Data/RaceResults.csv", index = False)
print("--- %s seconds ---" % (time.time() - start_time))