import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def loadAndCleanData():
    # La funzione carica il dataset IRIS da file CSV
    dataframe = pd.read_csv('iris.csv')
    dataframe.drop(['species'], axis=1, inplace=True)
    return dataframe

def selectRandomRows(dataframe, numrows):
    # Utilizzando una funzione pandas, vengono selezionate numrows righe nel dataframe
    return dataframe.sample(n = numrows)

def calculateDistances(dataframe, centerPoints, printInfo = False):
    """la funzione calcola le distanze tra i punti di un dataframe
    e dei centerPoints.
    Viene resitituito un DataFrame con le distanze di ogni punto 
    Da ogni centerPoint
    """
    distances = pd.DataFrame()
    i = 0
    for c in centerPoints:
        diff = dataframe.to_numpy() - np.asarray(c)
        square = np.square(diff)
        sum_square = np.sum(square, axis=1)
        distance = np.sqrt(sum_square)
        distances[f'c_{i}'] = distance
        i += 1
        if printInfo:
            print('********************************')
            print('dataframe:', dataframe.head(3).to_numpy())
            print('centroid: ', np.asarray(c[1:]))
            print('diff: ', diff)
            print('squares: ', square)
            print('sum squares: ', sum_square)
            print('distance: ', distance)
            print('********************************')
    return distances

def calulateMeanCentroids(dataframe, columnindex):
    """calcola il valore medio di punti di un DataFrame, raggruppandoli
    per i diversi valori di una data colonna (il cluster)
    """
    return dataframe.groupby(by=columnindex).mean().values

def algorithmloop(centroids, dataframe, maxIterations = 10, printInfo= False):
    """ funzione ricorsiva che costituisce il loop principale dell'algoritmo
    Dato un dataframe e dei centroidi, ripete l'algoritmo di classificazione
    Finchè si verifica una delle due condizioni:
    - i punti non hanno cambiato classe rispetto alla precedente iterazione
    - è stato raggiunto il numero massimo di iterzioni previste
    """
    if (maxIterations >= 1):
        distances = calculateDistances(iris_data, centroids, printInfo= False)
        classification = distances.idxmin(axis=1)
        countclasses = classification.groupby(classification).count()
        if('cluster' in dataframe.columns):
            countclusters = dataframe['cluster'].groupby(dataframe['cluster']).count()
            if(countclasses.shape[0] == countclusters.shape[0]):
                if(countclasses.equals(countclusters)):
                    dataframe['cluster'] = classification
                    if(printInfo):
                        print(f'convergence at iteration {maxIterations} with centroids {centroids}')
                    return centroids
        
        dataframe['cluster'] = classification
        centroids = calulateMeanCentroids(iris, 'cluster')
        maxIterations -= 1
        return algorithmloop(centroids, dataframe, maxIterations, printInfo)
    else:
        if(printInfo):
            print(f'reached max iterations limit with centroids {centroids}')
        return centroids

def clustervariance(dataframe, centroid, cluster):
    # calcola la varianza di un gruppo di righe di un DataFrame
    rows = dataframe.loc[dataframe['cluster'] == cluster]
    rows = rows.drop(['cluster'], axis = 1)
    distances = calculateDistances(rows, centroid.reshape(1,4))
    return distances['c_0'].var()

# main program

iris = loadAndCleanData()
iris_data = iris.copy()

maxK = 5
repetitions = 1
graphData = pd.DataFrame(columns= ['K', 'VAR'])

for k in range(1, maxK + 1):
    print('********BEGIN**********')
    print(f'Running algo for K={k}')
    print('***********************')    
    bestKVariance = sys.maxsize
    classified_iris = pd.DataFrame()
    for r in range(1, repetitions + 1):
        print('---')
        print(f'Repetition {r} for K={k}')
        print('---')

        centroids = selectRandomRows(iris_data, k).to_numpy()
        centroids = algorithmloop(centroids, iris, printInfo=True)

        iterVariance = 0
        for c in iris['cluster'].unique():
            iterVariance += clustervariance(iris, centroids[int(c[-1:])], c)

        if (iterVariance < bestKVariance):
            bestKVariance = iterVariance
            classified_iris = iris.copy()

        print('---')

    print(f'Best Variance for K={k}: {bestKVariance}')
    print(f'classified iris for K={k}', classified_iris)
    
    graphData = graphData.append(pd.Series( [ k,  bestKVariance ], index=graphData.columns ), ignore_index= True)
    print('*********END*************')

print(graphData)
graphData.plot(x="K", y="VAR", kind="line")
plt.show()