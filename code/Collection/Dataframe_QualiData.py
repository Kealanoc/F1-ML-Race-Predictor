import bs4
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time
start_time = time.time()

qualifying_results = pd.DataFrame()
for year in list(range(1983,2020)):
    url = 'https://www.formula1.com/en/results.html/{}/races.html'
    r = requests.get(url.format(year))
    soup = BeautifulSoup(r.text, 'html.parser')
    
    year_links = []
    for page in soup.find_all('a', attrs = {'class':"resultsarchive-filter-item-link FilterTrigger"}):
        link = page.get('href')
        if f'/en/results.html/{year}/races/' in link: 
            year_links.append(link)

    year_df = pd.DataFrame()
    new_url = 'https://www.formula1.com{}'
    for n, link in list(enumerate(year_links)):
        link = link.replace('race-result.html', 'starting-grid.html')
        df = pd.read_html(new_url.format(link))
        df = df[0]
        df['season'] = year
        df['round'] = n+1
        for col in df:
            if 'Unnamed' in col:
                df.drop(col, axis = 1, inplace = True)

        year_df = pd.concat([year_df, df])

    qualifying_results = pd.concat([qualifying_results, year_df])
qualifying_results.to_csv("../Data/QualifyingResults.csv", index = False)
print("--- %s seconds ---" % (time.time() - start_time))


