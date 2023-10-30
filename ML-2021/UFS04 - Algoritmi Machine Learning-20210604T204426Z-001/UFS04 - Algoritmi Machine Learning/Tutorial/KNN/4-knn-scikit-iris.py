import numpy as np 
import pandas as pandas
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.feature_names)
print(list(iris.target_names))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2) # 80% training and 20% test
print("X_train", X_train)
print("X_test", X_test)
print("y_train", y_train)
print("y_test", y_test)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

#Import knearest neighbors Classifier model
from sklearn.neighbors import KNeighborsClassifier

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=7)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)


#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


#Predict the response for test dataset
X_test = [[5., 3.6, 1.7, 0.4]]
X_test = scaler.transform(X_test)
y_pred = knn.predict(X_test)
print("MY y_pred", y_pred)
targetlist = list(iris.target)
print("MY target", iris.target_names[y_pred])

