import pandas as pd
import numpy as np
import requests
import time
total = 0
quali = pd.read_csv("../webpages/dash/static/Data/QualifyingResults.csv")
qd = quali.drop(["Pos", "No"], axis=1)

def get_comparison(team):
    driver_1 = []
    driver_2 = []
    time_1 = []
    time_2 = []
    driver_1.append(team["driver"].iloc[0])
    for i in range(len(team)):
        j = i+1
        if team["driver"].iloc[i] in driver_1:
            time_1.append(team["Quali_Time"].iloc[i])
        elif team["driver"].iloc[i] in driver_2:
            time_2.append(team["Quali_Time"].iloc[i])
        else:
            driver_2.append(team["driver"].iloc[i])
            time_2.append(team["Quali_Time"].iloc[i])
    diff_1 = {}
    for i in range(len(time_1)):
        race = i+1
        diff_1[race] = round((time_1[i]-time_2[i]),3)
    name = [x for x in driver_1[0].split()]
    name = name[2]
    df = pd.DataFrame(list(diff_1.items()), columns=["Round", "Quali Time Difference"])
    df.to_csv("../webpages/dash/static/Data/QualiComparison/{}.csv".format(name), index=False)

    diff_2 = {}
    for i in range(len(time_2)):
        race = i+1
        try:
            diff_2[race] = round((time_2[i]-time_1[i]),3)
        except:
            pass
    name = [x for x in driver_2[0].split()]
    name = name[2]
    df = pd.DataFrame(list(diff_2.items()), columns=["Round", "Quali Time Difference"])
    df.to_csv("../webpages/dash/static/Data/QualiComparison/{}.csv".format(name), index=False)

team = qd[(qd["Season"] == 2020) & (qd["Car"] == 'Alfa Romeo Racing Ferrari')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'Mercedes')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'Ferrari')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'Haas Ferrari')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'Renault')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'McLaren Renault')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'Williams Mercedes')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'Racing Point BWT Mercedes')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'AlphaTauri Honda')]
get_comparison(team) 
team = qd[(qd['Season'] == 2020) & (qd["Car"] == 'Red Bull Racing Honda')]
get_comparison(team) 