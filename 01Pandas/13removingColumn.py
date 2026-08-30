
import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

# syntax = df.drop(column = ["Column_name"] ,inplace = True)

# df.drop(columns = ["Performance Score"] , inplace=True) # single column remove
# print(df)

df.drop(columns = ["Performance Score" , "Age"] , inplace=True)  # multiple column remove
print(df)