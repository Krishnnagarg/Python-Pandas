import pandas as pd

data = {
    "Name" :["Rakhi" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)


# single condition apply  ---------------> 

# filter_age = df[df["Age"] >= 30] 
# print(filter_age)

# multiple condition apply  ----------->  And(&) OR(|) use 

# filter_data = df[(df["Age"] > 30) & (df["Salary"] > 40000)]
# print(filter_data)

# filter_data = df[(df["Age"] > 30) | (df["Salary"] > 40000)]
# print(filter_data)

filter_data = df[(df["Age"] >= 30) & (df["Salary"] >= 15000)]

# practice questions :------>
filter_age = df[df["Age"] > 25]
print(filter_age)

filter_salary = df[df["Salary"] < 20000]
print(filter_salary)

filter_data = df[(df["Age"] >20) & (df["Salary"] > 15000)]
print(filter_data)