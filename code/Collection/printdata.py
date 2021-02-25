import pandas as pd
import numpy as np

team_list = ["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"]
df = pd.read_csv("../webpages/dash/static/Data/ConstructorStandings.csv")
standings = {}
for team in team_list:
    position = {}
    for i in range(len(df)):
        if df.Constructor[i] == team and df.Season[i] == 2020:
            Round = df.Round[i]
            Position = df.ConstructorStandings[i]
            position[Round] = Position
    if "Round" not in standings:
        standings["Round"] = position.keys()
    if team not in standings:
        standings[team] = position.values()
    standings = pd.DataFrame.from_dict(standings)
print(standings)