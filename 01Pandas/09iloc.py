import pandas as pd

data = {
    "Name" :["Rakhi" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)

print(df.iloc[1,0]) # means 1 idx rows and 0 index column

print(df.iloc[0:2]) # 0 to 2 rows pass only 

print(df.iloc[:,0:2]) # all rows and 0 to 2 column pass in which 