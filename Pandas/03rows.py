
import pandas as pd 

df = pd.read_csv("sales_data_sample.csv")

print(df.head()) # show first 5 rows by default
print(df.head(10)) # show first 10 rows

print(df.tail(10)) # show last 10 rows 
print(df.tail()) # show last 5 rows by default

print(df.info())  # shows:- 1.total rows&column 2.column name 3.Data types 4.Missing Values? 5.Memomy Usages

