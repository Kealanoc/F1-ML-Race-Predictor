import pandas as pd
import numpy as np
total = 0
race = pd.read_csv("../webpages/dash/static/Data/RaceResults.csv")

def get_comparison(team):
    df = team.drop(["Track_ID", "Nationality", "Time", "Status", "Points", "URL", "DOB", "Pos"], axis=1)
    results = {}
    race = []
    race_num = 1
    for team in df.Constructor:
        name = team
    for position in df.Podium:
        if position != "":
            results[race_num] = position
            race.append(round(race_num))
            race_num +=1
    df = pd.DataFrame({"Race_Num": race})        
    results = pd.DataFrame.from_dict(results, orient='index', columns=["RaceResult"])
    results  = results.join(df)
    results.to_csv("../webpages/dash/static/Data/TeamRaceFinishes/{}.csv".format(name), index=False)
    

team = race[(race["Constructor"] == 'alfa')]
get_comparison(team) 
team = race[(race["Constructor"] == 'mercedes')]
get_comparison(team) 
team = race[(race["Constructor"] == 'ferrari')]
get_comparison(team) 
team = race[(race["Constructor"] == 'haas')]
get_comparison(team) 
team = race[(race["Constructor"] == 'renault')]
get_comparison(team) 
team = race[(race["Constructor"] == 'mclaren')]
get_comparison(team) 
team = race[(race["Constructor"] == 'williams')]
get_comparison(team) 
team = race[(race["Constructor"] == 'racing_point') | (race["Constructor"] == 'force_india')]
get_comparison(team) 
team = race[(race["Constructor"] == 'alphatauri') | (race["Constructor"] == 'toro_rosso')]
get_comparison(team) 
team = race[(race["Constructor"] == 'red_bull')]
get_comparison(team) 