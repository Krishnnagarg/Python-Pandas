import pandas as pd

data = {
    "Name" :["Rakhi" , "Krishna" , "Sohan" , "DhanShyam" , "Jagdish" ,"Rohan","Raj","Simran"],
    "Age":[22,25,28,29,30,32,34,40],
    "Salary":[12099,82020,19920,19292,10292,10992,109191,109201],
    "Performance Score":[85,79,48,94,83,83,94,39]
}

df = pd.DataFrame(data)

# 1. Display first 5 rows
print(df.head())

# 2. Show only Name column

print(df["Name"])
print(df.loc[:,"Name"])

# 3. Show Name and Salary columns

print(df.loc[:,["Name","Salary"]])
print(df[["Name","Salary"]])

# 4. Display last 3 rows

print(df.tail(3))

# 5. display dataset info 

df.info()

# 6. Show employees with Age > 30

filter_age = df[df["Age"] > 30]
print(filter_age)

# 7. Show employees with Salary < 20000

filter_salary = df[df["Salary"] < 20000]
print(filter_salary)

# 8. Show employees with Performance Score > 80

filter_perf = df[df["Performance Score"] > 80]
print(filter_perf)

# 9. Show employees where: Age > 25 AND Salary > 15000
filter_ageCond = df[(df["Age"] > 25) & (df["Salary"] > 15000)]
print(filter_ageCond)

# 11. Display row index 2 using loc[] 
print(df.loc[2])

# 12. Display row index 4 using iloc[]

print(df.iloc[4])

# 13. Get Krishna’s Salary using loc[]
print(df.loc[1,"Salary"])

print(df.loc[df["Name"] == "Krishna", "Salary"].values[0])

# 14. Get Raj’s Performance Score using iloc[]
print(df.iloc[6,3]) 

# 15. Show only Name and Age columns using loc[]

print(df.loc[:,["Name","Age"]])

# 16. Find average salary

print(f"Average of Salary is :- {df['Salary'].mean()}")
print(df["Salary"].max())  # find max Salary
print(df["Salary"].min())  # find min salary


# # # 17. Find maximum performance score
print(f"Anser--------------------------->")
print(df["Performance Score"].max())
print(df["Performance Score"].min())

# # # 18. Find minimum age
print(df["Age"].min())

# # # 19. Find employee with highest salary

print(df.loc[df["Salary"].idxmax()])

# 20. Find employee with lowest performance score

print(df.loc[df["Performance Score"].idxmin()])

# 21. Sort by Age ascending

print(df.sort_values(by="Age"))
 
# 22. Sort by Salary descending

print(df.sort_values(by="Salary" , ascending=False))

# 23. Sort by Performance Score highest first
print(df.sort_values(by="Performance Score" , ascending = False))


# 24. Add new column: Bonus = Salary * 0.10

df["Bonus"] = df["Salary"] * 0.10
print(df)

# 25. Find employees eligible for promotion: Performance Score > 85

print(df.loc[df["Performance Score"] > 85])

# 26. Employees with Salary greater than average salary :- Salary > average salary

print(df[df["Salary"] > df["Salary"].mean()])

print(df.loc[df["Salary"] > df["Salary"].mean()])

# 27.  New DataFrame with Name, Salary, and Bonus

new_df = df[["Name" , "Salary" , "Bonus" ]]
print(new_df)

# 28.  Save DataFrame to CSV

df.to_csv("employees.csv" , index = False)