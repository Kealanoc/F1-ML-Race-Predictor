import pandas as pd
import numpy as np
import requests
import time
race = pd.read_csv("../Data/RaceData.csv")
races = {"Season": [], "Round": [], "Track_ID": [] , "Country": [], "Date": [], "URL": []}
df = race.reindex(columns=list(races.keys()))
print(df)