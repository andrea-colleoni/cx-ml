from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

df = pd.read_csv('./iris.csv')

x = df['sepal_length']
y = df['petal_length']
setosa_x = x[:50]
setosa_y = y[:50]

versicolor_x = x[50:100]
versicolor_y = y[50:100]

virginica_x = x[100:]
virginica_y = y[100:]
# plot of the dataset: +: setosa, _: versicolor, o: virginica
plt.figure(figsize=(8,6))
plt.scatter(setosa_x,setosa_y,marker='+',color='green')
plt.scatter(versicolor_x,versicolor_y,marker='_',color='red')
plt.scatter(virginica_x,virginica_y,marker='o',color='blue')

Y = df['species']
df = df.drop(['species'],axis=1)

df = df.drop(['sepal_width','petal_width'],axis=1)
X = df.values.tolist()

X, Y = shuffle(X, Y)
x_train = []
y_train = []
x_test = []
y_test = []

x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9)

# use linear kernel function
clf = SVC(kernel='linear', verbose=True)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
sv = np.array(clf.support_vectors_)

# plot of support vectors: *
plt.scatter(sv[:,0],sv[:,1],marker='*',color='yellow')
plt.show()
print(accuracy_score(y_test,y_pred))

clf = SVC(kernel='poly', verbose=True)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print(accuracy_score(y_test,y_pred))

clf = SVC(kernel='rbf', verbose=True)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)

print(accuracy_score(y_test,y_pred))