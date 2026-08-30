import pandas as pd 

df_customers = pd.DataFrame({
    "CustomerId" : [1,2,3],
    "Name": ['Ramesh','Suresh','Kalpesh']
})

df_orders = pd.DataFrame({
    "CustomerId":[1,2,4],
    "OrderAmount":[250,450,350]
})

# merge

print("Inner Join ---->")
df_merged = pd.merge(df_customers,df_orders,on="CustomerId" ,how="inner")
print(df_merged)

print("Outer Join ---->")
df_merged = pd.merge(df_customers,df_orders,on="CustomerId" ,how="outer")
print(df_merged)

print("left Join ---->")
df_merged = pd.merge(df_customers,df_orders,on="CustomerId" ,how="left")
print(df_merged)
    
print("Right Join ---->")
df_merged = pd.merge(df_customers,df_orders,on="CustomerId" ,how="right")
print(df_merged)
