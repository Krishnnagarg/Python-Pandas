
import pandas as pd 

data = {
    "Name":["Krishna","Rakhi","Vashu","Amit","Nikhil","Tarun","Yash","Amit"],
    "Age":[23,22,21,23,25,26,27,21],
    "Salary":[98000,82999,28888,29999,90000,98000,82999,28888],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

# print(df.head())
# print(df.head(7))

print(df.describe())