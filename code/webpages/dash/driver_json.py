import json

def driver_json():
    with open("code\webpages\dash\drivers.json") as jsonFile:
        data = json.load(jsonFile)
    
    #print(data)
    return data