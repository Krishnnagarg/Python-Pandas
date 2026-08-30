 
import pandas as pd

data = {
    "Name" :["Renu" , "Krishna" , None , None , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,None,29,30,32,34,40],
    "Salary":[12099,82020,None,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,None,94,83,83,94,39]
}

df = pd.DataFrame(data)
print(df)

# method :- dropna() syntsx :- df.dropna(axis = 0 , inplace = True)

df.dropna(inplace=True) # (inplace = true) means "Original DataFrame ko hi change kar do."
df.reset_index(drop=True, inplace=True)
print(df)


