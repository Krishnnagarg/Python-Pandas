
import pandas as pd

data = {
    "Name" : ["Krishna","Rahul","Amit"],
    "Age":[22,21,23],
    "Salary":[90000,60000,27900]
}

df = pd.DataFrame(data)
print(df)

print(df.shape) # (rows,columns)
print(df.size) # 3 rows * 3 columns
print(df.ndim) # dataframe ---> 2d

print(df.columns) # show columns names
print(df.index)

print(df.dtypes)


print(df.head())
print(df.tail())
print(df.sample())

# selecting one column
print(df["Name"])
print(df[["Name"]]) # return dataframe
print(df[["Name","Salary"]]) # Select Multiple Column
