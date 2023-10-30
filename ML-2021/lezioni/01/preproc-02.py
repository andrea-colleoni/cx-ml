import numpy as num
import matplotlib.pyplot as mtp
import pandas as pd

fiori=pd.read_csv('preprocessing-02.csv')
fiori.head(1)
fiori.info()
print('\n\n-----')
fiori["colore"] = fiori["colore"].astype('category')

fiori.info()
print('\n\n-----')
print(fiori["colore"].describe())

print('\n\n-----')
x= fiori.iloc[:,:-1].values
y= fiori.iloc[:,3].values

print('\n\nend of script.')