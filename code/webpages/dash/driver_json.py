import json

def driver_json():
    with open("drivers.json") as jsonFile:
        data = json.load(jsonFile)
    return data