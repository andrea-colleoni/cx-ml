# see: https://media.geeksforgeeks.org/wp-content/uploads/nba.csv
import pandas as pd
import numpy as num

df = pd.read_csv('nba.csv')#, index_col="Name")

df.dropna(inplace=True)

#print(df.columns)
#print(df.tail(10))
#print(df.info)
#print(df["Age"])
#print(df["Name"].describe())

#wght = pd.DataFrame(df[['Weight','Height','Age']])
#print(wght)

#print(df)

#print(df.loc['Jordan Mickey'])
#print(df.loc[2])

df2 = df.reindex(index=range(364))
#print(df2.loc[0:20])
#print(df[df['Team'] == 'Boston Celtics'])

#print(df['Salary'].mean())
#print(df['Team'] == 'Boston Celtics')

print(df['Team'].value_counts())
print(df.shape)
p_t = df['Team'].value_counts()/df.shape[0]
print(p_t)