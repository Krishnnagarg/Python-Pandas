
import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)

print(df)

# method 1
df["Bonus"]  = df["Salary"] * 0.10 # add new Column :- Bonus 
print(df)

# method 2
df.insert(0,"Employee_id",[101,102,103,104,105,106,107,108])
print(df)