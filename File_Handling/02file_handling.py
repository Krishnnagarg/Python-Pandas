import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())

# df = pd.read_json("krishna.json")
# print(df.head())

df = pd.to_csv("output.csv" , index = False)