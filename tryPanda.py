import pandas as pd

df=pd.read_csv("pokemon_data.csv")
print(df.head())
print(df.columns)
print(df.iloc[3])