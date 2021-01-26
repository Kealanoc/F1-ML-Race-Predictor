import pandas as pd
import numpy as np
from dateutil.relativedelta import *

race = pd.read_csv("../Data/RaceData.csv")
results = pd.read_csv("../Data/RaceResults.csv")
quali = pd.read_csv("../Data/QualifyingResults.csv")
driver_standings = pd.read_csv("../Data/DriverStandings.csv")
constructor_standings = pd.read_csv("../Data/ConstructorStandings.csv")
weather = pd.read_csv("../Data/Weather.csv")
dataframe_1 = pd.merge(race, weather, how="inner", on=["Season", "Round", "Track_ID"]).drop(["Country", "weather"], axis=1)
dataframe_2 = pd.merge(dataframe_1, results, how="inner", on=["Season", "Round", "Track_ID", "URL"]).drop(["URL", "Points", "Status", "Time"], axis=1)
dataframe_3 = pd.merge(dataframe_2, driver_standings, how="left", on=["Season", "Round", "Driver"])
dataframe_4 = pd.merge(dataframe_3, constructor_standings, how="left", on=["Season", "Round", "Constructor"])
complete_df = pd.merge(dataframe_4, quali, how="inner", on=["Season", "Round", "Grid"]).drop(["Car", "Driver_ID"], axis=1)

complete_df['Date'] = pd.to_datetime(complete_df.Date)
complete_df['DOB'] = pd.to_datetime(complete_df.DOB)
complete_df['Driver_Age'] = complete_df.apply(lambda x: relativedelta(x['Date'], x['DOB']).years, axis=1)
complete_df.drop(['Date', 'DOB'], axis = 1, inplace = True)
for columns in ['weather_warm', 'weather_cold','weather_dry', 'weather_wet', 'weather_cloudy']:
    complete_df[columns] = complete_df[columns].map(lambda x: bool(x))
for columns in ['Driver Points', 'Driver Wins', 'Driver Standings', 'Constructor Points', 
            'Constructor Wins' , 'Constructor Standings']:
    complete_df[columns].fillna(0, inplace = True)
    complete_df[columns] = complete_df[columns].map(lambda x: int(x))
complete_df.dropna(inplace=True)

df = pd.get_dummies(complete_df, columns=['Track_ID', 'Nationality', 'Constructor'] )

for column in df.columns:
    if 'Nationality' in column and df[column].sum() < 100:
        df.drop(column, axis=1, inplace=True) 
    elif 'Constructor' in column and df[column].sum() < 100:
        df.drop(column, axis=1, inplace=True)  
    elif 'Track_ID' in column and df[column].sum() < 50:
        df.drop(column, axis=1, inplace=True)
    else:
        pass

for i in df.Quali_Time:
    try:
        if ":" in i:
            m,s = i.split(":")
            m = ("{:.3f}".format(float(m)*60) + float(s))
            df["Quali_Time"].replace({i:m}, inplace=True)
    except:
        pass


df.to_csv("../Data/CompleteDF.csv", index=False)
print(df.shape)