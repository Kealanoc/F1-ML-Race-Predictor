import pandas as pd
import numpy as np
import requests
import time
total = 0
race = pd.read_csv("../Data/QualifyingResults.csv")
for i in race.Quali_Time:
    try:
        m = ("{:.3f}".format(i))
        race["Quali_Time"].replace({i:m}, inplace=True)
    except:
        pass
race.to_csv("../Data/QualifyingResults.csv", index=False)