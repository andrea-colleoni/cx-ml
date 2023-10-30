import pandas as pd

df = pd.read_csv('./Iris.csv')

print(type(df))
print(df.to_string()) 