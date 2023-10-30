import pandas as pd

data = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')

data['obese'] = (data.Index >= 4).astype('int')
data.drop('Index',axis=1,inplace=True)
print(data)