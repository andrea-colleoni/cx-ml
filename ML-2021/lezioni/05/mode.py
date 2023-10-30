import pandas as pd

df = pd.DataFrame()

df['col_1'] = [1,0,0,0,1]
df['col_2'] = [0,0,0,0,1]
df['col_3'] = [1,1,1,0,1]
df['col_4'] = [1,1,0,0,1]

print(df.mode(axis=1))