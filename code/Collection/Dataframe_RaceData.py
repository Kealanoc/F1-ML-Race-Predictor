import pandas as pd
import numpy as np
import requests

races = {"Season": [], "Round": [], "Track_ID": [] , "Country": [], "Date": [], "URL": []}

for year in list(range(1950, 2021)):
    url = "https://ergast.com/api/f1/{}.json"
    request = requests.get(url.format(year))
    json = request.json()

    for i in json["MRData"]["RaceTable"]["Races"]:
        try:
            races["Season"].append(int(i["season"]))
        except:
            races["Season"].append(None)
        try:
            races["Round"].append(int(i["round"]))
        except:
            races["Round"].append(None)
        try:
            races['Track_ID'].append(i['Circuit']['circuitId'])
        except:
            races["Track_ID"].append(None)
        try:
            races['Country'].append(i['Circuit']['Location']['country'])
        except:
            races['Country'].append(None)
        try:
            races['Date'].append(i['date'])
        except:
            races['Date'].append(None)
        try:
            races['URL'].append(i['url'])
        except:
            races['URL'].append(None)
races = pd.DataFrame(races)
print(races.shape)

races.to_csv("../Data/RaceData.csv", index = False)