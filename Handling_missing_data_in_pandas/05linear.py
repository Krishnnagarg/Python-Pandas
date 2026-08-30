import pandas as pd

data = {
    "Time" : [1,2,3,4,5],
    "Value" :[10,None,30,None,50]
}

df = pd.DataFrame(data)

print("Before Interpolation -----> ")
print(df)

print("After Interpolation -----> ")
df["Value"] = df["Value"].interpolate(method="linear") # add estimate values in None place
print(df)

'''
interpolation is use when :-

1. when you work with time series
2. numeric data with trends
3. avoid droping rows
'''
