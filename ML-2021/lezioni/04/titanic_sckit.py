import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from io import StringIO
import pydotplus
import numpy as np

train_df = pd.read_csv("titanic_train.csv")
test_df = pd.read_csv('titanic_test.csv')

# train data 

lbSex = LabelEncoder()
train_df['Sex'] = lbSex.fit_transform(train_df['Sex'])
#print(train_df['Sex'])

count_null_embarked = len(train_df['Embarked'][ train_df.Embarked.isnull() ])
value_to_fill_embarked = train_df['Embarked'].dropna().mode().values
train_df['Embarked'][ train_df.Embarked.isnull() ] = value_to_fill_embarked

lbEmb = LabelEncoder()
train_df['Embarked'] = lbEmb.fit_transform(train_df['Embarked'])

target = train_df['Survived']
train_df = train_df.drop(['Name', 'Cabin', 'Ticket', 'PassengerId', 'Survived'], axis = 1)

# fix NaN with means etc.
im = SimpleImputer()
train_predictors = im.fit_transform(train_df)

# test data

lbSexTst = LabelEncoder()
test_df['Sex'] = lbSexTst.fit_transform(test_df['Sex'])

count_null_embarked = len(test_df['Embarked'][ test_df.Embarked.isnull() ])
value_to_fill_embarked = test_df['Embarked'].dropna().mode().values
test_df['Embarked'][ test_df.Embarked.isnull() ] = value_to_fill_embarked

lbEmbTst = LabelEncoder()
test_df['Embarked'] = lbEmbTst.fit_transform(test_df['Embarked'])

test_df = test_df.drop(['Name', 'Cabin', 'Ticket', 'PassengerId'], axis = 1)

imTst = SimpleImputer()
test_predictors = imTst.fit_transform(test_df)

# train
classifier = DecisionTreeClassifier()
classifier = classifier.fit(train_predictors, target)

# predict
predictions = classifier.predict(test_predictors)

test_data = pd.read_csv('titanic_test.csv').values
result = np.c_[test_data[:,0].astype(int), predictions.astype(int)]
df_result = pd.DataFrame(result[:,0:2], columns =['PassengerId','Survived'])
df_result.to_csv('titanic_predictions.csv', index=False)

'''
out = StringIO()
tree.export_graphviz(classifier, out_file=out)
graph = pydotplus.graph_from_dot_data(out.getvalue())
graph.write_png('titanic.png')
'''