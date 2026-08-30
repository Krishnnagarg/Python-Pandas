
import pandas as pd

data = {
    "Name" : ["Krishna" , "Rakhi", "Yash"],
    "Age":[22,21,20],
    "City":["Safidon" , "Panipat" , "Sonipat"]
}

df = pd.DataFrame(data)
print(df.head())
print(df.info())


# df.to_csv("output.csv",index=False) # create csv file whose name output.csv
# df.to_excel("output.xlsx",index=False) # create excel file whose name output.xlsx
# df.to_json("output.json",index=False) # create json file whose name output.


