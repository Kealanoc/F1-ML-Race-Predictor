import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time
start_time = time.time()

race = pd.read_csv("../webpages/dash/static/Data/RaceData.csv")
weather = race.iloc[:,[0,1,2]]
data = []

for links in race.URL:
    try:
        dataframe = pd.read_html(links)[0]
        if "Weather" in list(dataframe.iloc[:,0]):
            i = list(dataframe.iloc[:,0]).index("Weather")
            data.append(dataframe.iloc[i,1])
        else:
            dataframe = pd.read_html(links)[1]
            if "Weather" in list(ds.iloc[:,0]):
                i = list(df.iloc[:,0]).index("Weather")
                data.append(df.iloc[i,1])
            else:
                dataframe = pd.read_html(links)[2]
                if "Weather" in list(ds.iloc[:,0]):
                    i = list(dataframe.iloc[:,0]).index("Weather")
                    data.append(dataframe.iloc[i,1])
                else:
                    dataframe = pd.read_html(links)[3]
                    if "Weather" in list(ds.iloc[:,0]):
                        i = list(dataframe.iloc[:,0]).index("Weather")
                        data.append(dataframe.iloc[i,1])
    except:
        data.append("N/A")

weather['weather'] = data
weather_class = {"weather_warm": ['clear', 'warm', 'hot', 'sunny', 'fine', 'mild'],
               "weather_cold": ['cold', 'fresh', 'chilly', 'cool'],
               "weather_dry": ['dry'],
               "weather_wet": ['showers', 'wet', 'rain', 'damp', 'thunderstorms', 'rainy'],
               "weather_cloudy": ['overcast', 'clouds', 'cloudy', 'grey']}

weather_data = pd.DataFrame(columns=weather_class.keys())
for column in weather_data:
    weather_data[column] = weather["weather"].map(lambda x: 1 if any(i in weather_class[column] for i in x.lower().split()) else 0)
weather_data = pd.concat([weather, weather_data], axis=1)
weather_data.to_csv("../webpages/dash/static/Data/Weather.csv", index=False)
print("--- %s seconds ---" % (time.time() - start_time))