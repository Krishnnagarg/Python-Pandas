import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,23,21,30,20,18,29],
    "Salary":[12099,82020,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

print(df["Salary"].mean()) # find Average salary 
print(df["Salary"].min()) # find min salary in column
print(df["Salary"].max())
print(df["Salary"].sum()) # add all vales in column 
print(df["Salary"].count()) # count how many values in which  
print(df["Salary"].std()) # calculate Standard Deviation 


