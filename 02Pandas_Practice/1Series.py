
import pandas as pd
marks = pd.Series([80,75,88,56,99])
print(marks)

print(marks[0]) # Access Index
print(marks[1])
print(marks[2])

print(marks[1:4]) # slicing marks[start:stop] stop value not include in which

print(marks.shape)
print(marks.size)
print(marks.ndim)
print(marks.dtype)
print(marks.index)
print(marks.values)

# important Methods 

print(marks.sum())
print(marks.mean())
print(marks.median())
print(marks.min())
print(marks.max())
print(marks.std())
print(marks.count())

print(marks.describe())

# sort_value 

print(marks.sort_values())
print(marks.sort_values(ascending=False))

# Values_count()
grades = pd.Series(["A","B","A","C","B","A"])
print(grades.value_counts())

# Missing Values 

mark1 = pd.Series([80,90,None,75,88,None])
print(mark1) 
print(mark1.isna()) # check missing value
print(mark1.isna().sum()) # count missing value