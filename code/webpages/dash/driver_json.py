import json

def driver_json():
    with open("drivers.json") as jsonFile:
        data = json.load(jsonFile)
    return data

def team_json():
    with open("teams.json") as jsonFile:
        data = json.load(jsonFile)
    return data