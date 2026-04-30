import pandas as pd

data = {
    "Name" :["Rakhi" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)
# print(df)

# print(df.loc[1,"Name"])
# print(df.loc[1])
# print(df.loc[0:2])

# print(df.loc[:, ["Name", "Salary"]])


# print(df.head())

print(df.loc[:,"Name"])
print(df["Name"])
# print(df.loc[:,["Name","Salary"]])
# print(df.iloc[0:3])
# print(df.info())

