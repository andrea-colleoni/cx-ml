import pandas as pd 

fiori = pd.read_csv('preprocessing-02.csv')
# fiori è un pandas DataFrame
fiori.head(1)
# head() è il metodo che interpreta come intestazione la riga di dati indicata
fiori.info()
print('\n\n-----')

fiori["colore"] = fiori["colore"].astype("category")
fiori["spine"] = fiori["spine"].astype("category")
# fiori["lung_petalo"] = fiori["lung_petalo"].astype("int")
# fiori.info()

# print(fiori["colore"].describe())
# print(fiori.describe())

# print(fiori)
# one hot encoding
print(fiori["colore"])
print('\n\n-----')
print(pd.get_dummies(fiori["colore"], prefix='  '))
print('\n\n-----')
fiori['spine'] = fiori["spine"].replace(['no'], 0).replace(['sì'], 1)
print(fiori)


