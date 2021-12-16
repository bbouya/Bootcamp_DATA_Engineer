import pandas as pd
from clean  import *



df = pd.read_csv("appstore_games.csv")
sho = df.shape

df = df_nan_filter(df)

print(df.head(1))