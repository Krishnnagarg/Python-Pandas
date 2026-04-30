import pandas as pd

# read data from csv file

# df = pd.read_csv("sales_data_sample.csv")
# print(df.head())

# df = pd.read_excel("SampleSuperstore.xlsx" , engine="openpyxl")
# print(df.head())

df = pd.read_json("sample_Data.json")
print(df.head())

