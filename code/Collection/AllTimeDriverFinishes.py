import pandas as pd
import numpy as np
total = 0
race = pd.read_csv("../webpages/dash/static/Data/RaceResults.csv")

def get_comparison(driver):
    df = driver.drop(["Track_ID", "Nationality", "Time", "Status", "Points", "URL", "DOB", "Pos"], axis=1)
    results = {}
    race = []
    race_num = 1
    name = ""
    for position in df.Podium:
        if position != "":
            results[race_num] = position
            race.append(round(race_num))
            race_num +=1
    df1 = pd.DataFrame({"Race_Num": race})        
    results = pd.DataFrame.from_dict(results, orient='index', columns=["RaceResult"])
    results  = results.join(df1)
    for team in df.Driver:
        name = team
    results.to_csv("../webpages/dash/static/Data/DriverRaceFinishes/{}.csv".format(name), index=False)
    

driver = race[(race["Driver"] == 'hamilton')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'bottas')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'max_verstappen')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'albon')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'sainz')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'norris')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'perez')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'stroll')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'ricciardo')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'ocon')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'leclerc')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'vettel')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'kvyat')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'gasly')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'raikkonen')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'giovinazzi')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'latifi')]
get_comparison(driver) 
driver = race[(race["Driver"] == 'russell')]
get_comparison(driver)
driver = race[(race["Driver"] == 'kevin_magnussen')]
get_comparison(driver)
driver = race[(race["Driver"] == 'grosjean')]
get_comparison(driver)
