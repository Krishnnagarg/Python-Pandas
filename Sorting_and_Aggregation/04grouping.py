
import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,22,21,30,20,18,29],
    "Salary":[50000,60000,45000,48000,55000,40000,52000],
    "Performance Score":[85,79,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

print(df.groupby("Age")["Salary"].sum())

print(df.groupby(["Age","Name"])["Salary"].sum()) # groupby Age and Name

df["Department"] = ["IT","IT","HR","Manegar","IT","HR","Manegar"]
print(df) 

# 1. Average salary by department

print(df.groupby("Department")["Salary"].mean())

# 2. Maximum performance score by department

print(df.groupby("Department")["Performance Score"].max())

# 3. Total employees by department

print(df.groupby("Department")["Name"].count())
