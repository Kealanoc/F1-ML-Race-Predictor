import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time
start_time = time.time()

qualifying_results = pd.DataFrame()
for year in list(range(1983,2021)):
    url = "https://www.formula1.com/en/results.html/{}/races.html"
    r = requests.get(url.format(year))
    soup = BeautifulSoup(r.text, "html.parser")
    
    links = []
    for page in soup.find_all("a", attrs = {'class':"resultsarchive-filter-item-link FilterTrigger"}):
        link = page.get('href')
        if f"/en/results.html/{year}/races/" in link: 
            links.append(link)

    year_df = pd.DataFrame()
    new_url = "https://www.formula1.com{}"
    for i, link in list(enumerate(links)):
        link = link.replace("race-result.html", "starting-grid.html")
        dataframe = pd.read_html(new_url.format(link))
        dataframe = dataframe[0]
        dataframe["season"] = year
        dataframe["round"] = i+1
        for column in dataframe:
            if "Unnamed" in column:
                dataframe.drop(column, axis=1, inplace=True)

        year_df = pd.concat([year_df, dataframe])
    qualifying_results = pd.concat([qualifying_results, year_df])
qualifying_results.rename(columns={"Time":"Quali_Time"}, inplace=True)

for i in qualifying_results.Quali_Time:
    try:
        if ":" in i:
            m,s = i.split(":")
            m = round((float(m)*60) + float(s), 3)
            qualifying_results["Quali_Time"].replace({i:m}, inplace=True)
    except:
        pass
qualifying_results.to_csv("../Data/QualifyingResults.csv", index=False)
