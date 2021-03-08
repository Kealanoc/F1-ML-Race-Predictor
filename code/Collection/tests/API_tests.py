import pandas as pd
import numpy as np
import requests
import pytest
import os


request_urls = ["https://ergast.com/api/f1/1950.json",
                "https://ergast.com/api/f1/2020/1/constructorStandings.json", 
                "https://ergast.com/api/f1/2020/1/driverStandings.json",
                "https://ergast.com/api/f1/2020/1/results.json",
                "https://www.formula1.com/en/results.html/1983/races.html"]
@pytest.mark.parametrize("url", request_urls)
def test_http_request(url):
    print("\n \nRequesting Data...")
    print("Request sent for: {}".format(url))
    response = requests.get(url)
    assert response.status_code == 200
    print("Response Code 200 Recieved")


request_urls = ["https://ergast.com/api/f1/1950.json",
                "https://ergast.com/api/f1/1950/1/constructorStandings.json", 
                "https://ergast.com/api/f1/1950/1/driverStandings.json",
                "https://ergast.com/api/f1/1950/1/results.json"]
@pytest.mark.parametrize("url", request_urls)
def test_racedata_json_response(url):
    print("\n\nTesting Response Format For: {}".format(url))
    response = requests.get(url)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print("Response Recieved In Json Format")


def test_racedata_json_content():
    print("\n\nTesting Content for expected Entries")
    response = requests.get("https://ergast.com/api/f1/1950.json")
    response_body = response.json()
    print("Content Verified")
    assert response_body["MRData"]["RaceTable"]["Races"][0]["raceName"] == "British Grand Prix"

def test_constructorStandings_json_content():
    print("\n\nTesting Content for expected Entries")
    response = requests.get("https://ergast.com/api/f1/2020/1/constructorStandings.json")
    response_body = response.json()
    print("Content Verified")
    assert response_body["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"][0]["Constructor"]["constructorId"] == "mercedes"

def test_driverStandings_json_content():
    print("\n\nTesting Content for expected Entries")
    response = requests.get("https://ergast.com/api/f1/2020/1/driverStandings.json")
    response_body = response.json()
    print("Content Verified")
    assert response_body["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["driverId"] == "bottas"

def test_raceResults_json_content():
    print("\n\nTesting Content for expected Entries")
    response = requests.get("https://ergast.com/api/f1/2020/1/results.json")
    response_body = response.json()
    print("Content Verified")
    assert response_body["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["driverId"] == "bottas"


def test_validate_num_driver_finish():
    DIR = '../../webpages/dash/static/Data/DriverRaceFinishes'
    print("\n\nVerifying All Driver Finish DataFrames Are Present...")
    num_drivers = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print("DataFrames Verified")
    assert num_drivers-1 == 20
def test_validate_driver_finish_contents():
    print("\n\nVerifying Contents of Driver Finish Dataframe...")
    race = pd.read_csv("../../webpages/dash/static/Data/DriverRaceFinishes/albon.csv")
    assert race.columns[0] == "RaceResult" and race.columns[1] =="Race_Num"


def test_validate_num_driver_quali():
    DIR = '../../webpages/dash/static/Data/QualiComparison'
    print("\n\nVerifying All Driver Qualifying DataFrames Are Present...")
    num_drivers = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print("DataFrames Verified")
    assert num_drivers == 20
def test_validate_driver_quali_contents():
    print("\n\nVerifying Contents of Driver Quali Dataframe...")
    race = pd.read_csv("../../webpages/dash/static/Data/QualiComparison/ALB.csv")
    assert race.columns[0] == "Round" and race.columns[1] =="Quali Time Difference"


def test_validate_num_team_lineups():
    DIR = '../../webpages/dash/static/Data/TeamLineups'
    print("\n\nVerifying All TeamLineup DataFrames Are Present...")
    num_drivers = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print("DataFrames Verified")
    assert num_drivers == 10
def test_validate_driver_quali_contents():
    print("\n\nVerifying Contents of Team Lineup Dataframe...")
    race = pd.read_csv("../../webpages/dash/static/Data/TeamLineups/Haas.csv")
    assert race.columns[0] == "Driver" and race.columns[1] =="Races"


def test_validate_num_team_Finishes():
    DIR = '../../webpages/dash/static/Data/TeamRaceFinishes'
    print("\n\nVerifying All Team Finish DataFrames Are Present...")
    num_drivers = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print("DataFrames Verified")
    assert num_drivers == 10
def test_validate_driver_finish_contents():
    print("\n\nVerifying Contents of Team Finish Dataframe...")
    race = pd.read_csv("../../webpages/dash/static/Data/TeamRaceFinishes/haas.csv")
    assert race.columns[0] == "RaceResult" and race.columns[1] =="Race_Num"

def test_validate_number_columns_Complete_DataFrame():
    race = pd.read_csv("../../webpages/dash/static/Data/CompleteDF.csv")
    count = 0
    print("\n\nVerifying the Number of Columns in Complete Dataframe")
    for col in race.columns:
        count+=1
    assert count == 116

def test_validate_data_format_Complete_DataFrame():
    race = pd.read_csv("../../webpages/dash/static/Data/CompleteDF.csv")
    print("\n\nVerifying Data is of Correct type in Complete Dataframe")
    for time in race.Quali_Time:
        if time != '':
            assert type(time) is float

def test_validate_data_FeatureImportance():
    race = pd.read_csv("../../webpages/dash/static/Data/Predictions/2020_FeatureImportance")
    print("\n\nVerifying The size and contents of Feature Importance")
    count = 0
    for col in race.columns:
        count+=1
    assert count == 114
    
def test_validate_Correct_Evaluation_Feature_Importance():
    df = pd.read_csv("../../webpages/dash/static/Data/Predictions/2020_FeatureImportance")
    print("\n\nVerifying Values of Feature Importance Evalutate Correctly")
    count = 0
    for i in range(len(df.columns)):
        count += df[df.columns[i]][0]
    assert int(count) == 1




if __name__ == "__main__":
    main()