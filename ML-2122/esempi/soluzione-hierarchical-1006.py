import pandas as pd
import numpy as np
import sys
import math

def loadAndCleanData():
    # La funzione carica il dataset distanze_citta da file CSV
    dataframe = pd.read_excel('distanze-città.xlsx', index_col=0)
    dataframe = dataframe.replace('–', sys.maxsize)
    dataframe = dataframe.fillna(0)
    dataframe.index = dataframe.columns
    return dataframe

def coppiaminima(dataframe):
    min = dataframe.min().min()
    coppia = dataframe[dataframe.eq(min).any(1)]
    return (coppia, min)

def coppie_livelli(dataframe):
    coppie = pd.DataFrame(columns=['c1', 'c2', 'dist', 'level'])
    for level in range(1, math.ceil(math.log2(dataframe.shape[0]))):
        df = dataframe.copy()
        while(df.shape[0] > 1):
            coppia, min = coppiaminima(df)
            dataframe = dataframe.replace(min, sys.maxsize)
            df = df.drop([coppia.index[0], coppia.index[1]], axis=0)
            df = df.drop([coppia.index[0], coppia.index[1]], axis=1)
            coppie = coppie.append(pd.Series( [ coppia.index[0],  coppia.index[1], min, level ], index=coppie.columns ), ignore_index= True)
    return coppie, dataframe

def coppieminimadistanza(dataframe):
    coppie = pd.DataFrame(columns=['c1', 'c2', 'dist'])
    df = dataframe.copy()
    while(np.amin(df.to_numpy()) < sys.maxsize):
        coppia, min = coppiaminima(df)
        df = df.replace(min, sys.maxsize)
        coppie = coppie.append(pd.Series( [ coppia.index[0],  coppia.index[1], min ], index=coppie.columns ), ignore_index= True)
    return coppie    

# main program

citta = loadAndCleanData()
coppie = coppieminimadistanza(citta)
print(coppie)
# print(citta)