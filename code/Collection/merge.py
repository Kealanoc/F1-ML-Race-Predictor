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
dataframe_2 = pd.merge(dataframe_1, results, how="inner", on=["Season", "Round", "Track_ID", "URL"]).drop(["URL", "Points", "Status", "Race_Time"], axis=1)
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
    
complete_df.dropna(inplace = True )
#complete_df['quali_time'] = complete_df.Time.map(lambda x: 0 if str(x) == '00.000' else(float(str(x).split(':')[1]) + (60 * float(str(x).split(':')[0])) if x != 0 else 0))
#complete_df = final_df[final_df['quali_time'] != 0]
#complete_df.sort_values(['Season', 'Round', 'Grid'], inplace = True)
#complete_df['qualif_time_diff'] = complete_df.groupby(['Season', 'Round']).quali_time.diff()
#complete_df['quali_time'] = complete_df.groupby(['Season', 'Round']).quali_time_diff.cumsum().fillna(0)
#complete_df.drop('quali_time_diff', axis = 1, inplace = True)
df = pd.DataFrame(complete_df)
df.to_csv("../Data/CompleteDF.csv", index = False)