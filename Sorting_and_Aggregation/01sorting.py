import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,23,21,30,20,18,29],
    "Salary":[12099,82020,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by="Age",ascending=False,inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)