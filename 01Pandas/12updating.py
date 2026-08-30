
import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

# .loc[] = df.loc[row_idx_number,"column_name"] = new_value
df.loc[0,"Salary"] = 55000
print(df)

# increasing Salary by 5% :- updating existing column Salary Column 

df["Salary"] = df["Salary"] * 1.05
print(df)

