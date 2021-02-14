import pandas as pd
import numpy as np
import requests
import time
import csv

total = 0
race = pd.read_csv("../Data/RaceResults.csv")
race = race.drop(["Season", "Round", "Track_ID", "DOB", "Nationality", "Grid", "Time", "Status", "Points", "URL", "Podium"], axis=1)
redbull = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in redbull and team == "red_bull":
        redbull[driver] = 1
    elif driver in redbull and team == "red_bull":
        redbull[driver] = redbull[driver] + 1
df = pd.DataFrame(list(redbull.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Red_Bull"), index=False)
mercedes = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in mercedes and team == "mercedes":
        mercedes[driver] = 1
    elif driver in mercedes and team == "mercedes":
        mercedes[driver] = mercedes[driver] + 1
df = pd.DataFrame(list(mercedes.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Mercedes"), index=False)

mclaren = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in mclaren and team == "mclaren":
        mclaren[driver] = 1
    elif driver in mclaren and team == "mclaren":
        mclaren[driver] = mclaren[driver] + 1
df = pd.DataFrame(list(mclaren.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Mclaren"), index=False)

renault = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in renault and team == "renault":
        renault[driver] = 1
    elif driver in renault and team == "renault":
        renault[driver] = renault[driver] + 1
df = pd.DataFrame(list(renault.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Renault"), index=False)

alfa = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in alfa and team == "alfa":
        alfa[driver] = 1
    elif driver in alfa and team == "alfa":
        alfa[driver] = alfa[driver] + 1
df = pd.DataFrame(list(alfa.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Alfa"), index=False)

alphatauri = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in alphatauri and (team == "alphatauri" or team == "toro_rosso"):
        alphatauri[driver] = 1
    elif driver in alphatauri and (team == "alphatauri" or team == "toro_rosso"):
        alphatauri[driver] = alphatauri[driver] + 1
df = pd.DataFrame(list(alphatauri.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Alphatauri"), index=False)

haas = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in haas and team == "haas":
        haas[driver] = 1
    elif driver in haas and team == "haas":
        haas[driver] = haas[driver] + 1
df = pd.DataFrame(list(haas.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Haas"), index=False)

williams = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in williams and team == "williams":
        williams[driver] = 1
    elif driver in williams and team == "williams":
        williams[driver] = williams[driver] + 1
df = pd.DataFrame(list(williams.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Williams"), index=False)

ferrari = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in ferrari and team == "ferrari":
        ferrari[driver] = 1
    elif driver in ferrari and team == "ferrari":
        ferrari[driver] = ferrari[driver] + 1
df = pd.DataFrame(list(ferrari.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Ferrari"), index=False)

racingpoint = {}
for i in range(len(race)):
    driver = race.Driver[i]
    team = str(race.Constructor[i])
    if driver not in racingpoint and (team == "racingpoint" or team == "force_india"):
        racingpoint[driver] = 1
    elif driver in racingpoint and (team == "racingpoint" or team == "force_india"):
        racingpoint[driver] = racingpoint[driver] + 1
df = pd.DataFrame(list(racingpoint.items()), columns=["Driver", "Races"])
df.to_csv("../Data/TeamLineups/{}.csv".format("Racing_Point"), index=False)