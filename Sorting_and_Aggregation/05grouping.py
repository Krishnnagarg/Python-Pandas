import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)
print(df)

# Department Wise Average Salary 
avg_IT_Salary = df.groupby("Department")["Salary"].mean()
print(avg_IT_Salary)

# Total Salary by Department
print(df.groupby("Department")["Salary"].sum())

# Employee Count

print(df.groupby("Department")["Name"].count())

# Multiple Aggregations
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))