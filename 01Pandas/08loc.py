import pandas as pd

data = {
    "Name" :["Rakhi" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)
# print(df)

print(df.loc[1,"Name"])
print(df.loc[1]) # only one row pass in which 
print(df.loc[0:2]) # only rows pass in which 0 to 2 

print(df.loc[:, ["Name", "Salary"]]) # all rows from start to end and only Name and Salary Column Shows




