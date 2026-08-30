
import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , None , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,None,29,30,32,34,40],
    "Salary":[12099,82020,None,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,None,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

# fillna() syntax :- df["Column_name1"] = df["Column_name1"].fillna(value,inplace = True)

df["Name"] = df["Name"].fillna("unknown")   # Option 1 (Best): Har column ke according fill karo
df["Age"] = df["Age"].fillna(22)
df["Salary"] = df["Salary"].fillna(28000)
df["Performance Score"] = df["Performance Score"].fillna(87)
print(df)


# df.fillna({  # Option 2 (Short Method): Dictionary use karo
#     "Name" :"unknown",
#     "Age":22,
#     "Salary":27999,
#     "Performance Score":73
# }, inplace = True)

# print(df)

# df["Age"] = df["Age"].fillna(df["Age"].mean(),inplace=True)
# print(df)