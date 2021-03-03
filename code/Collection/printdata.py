import pandas as pd
import numpy as np

team_list = ["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"]
df = pd.read_csv("../webpages/dash/static/Data/CompleteDF.csv")
print(df.shape)