import pandas as pd
import numpy as np

def gini_impurity(y):
  '''
  Given a Pandas Series, it calculates the Gini Impurity. 
  y: variable with which calculate Gini Impurity.
  '''
  if isinstance(y, pd.Series):
    p = y.value_counts()/y.shape[0]
    gini = 1-np.sum(p**2)
    return(gini)

  else:
    raise('Object must be a Pandas Series.')

def entropy(y):
  '''
  Given a Pandas Series, it calculates the entropy. 
  y: variable with which calculate entropy.
  '''
  if isinstance(y, pd.Series):
    a = y.value_counts()/y.shape[0]
    entropy = np.sum(-a*np.log2(a+1e-9))
    return(entropy)

  else:
    raise('Object must be a Pandas Series.')    

def variance(y):
  '''
  Function to help calculate the variance avoiding nan.
  y: variable to calculate variance to. It should be a Pandas Series.
  '''
  if(len(y) == 1):
    return 0
  else:
    return y.var()

def information_gain(y, mask, func=entropy):
  '''
  It returns the Information Gain of a variable given a loss function.
  y: target variable.
  mask: split choice.
  func: function to be used to calculate Information Gain in case os classification.
  '''
  
  a = sum(mask)
  b = mask.shape[0] - a
  
  if(a == 0 or b ==0): 
    ig = 0
  
  else:
    if y.dtypes != 'O':
      # the case of regression (continuous variable)
      ig = variance(y) - (a/(a+b)* variance(y[mask])) - (b/(a+b)*variance(y[-mask]))
    else:
      # the case of classification (continuous variable)
      ig = func(y)-a/(a+b)*func(y[mask])-b/(a+b)*func(y[-mask])
  
  return ig


data = pd.read_csv("500_Person_Gender_Height_Weight_Index.csv")
data.head()

data['obese'] = (data.Index >= 4).astype('int')
data.drop('Index', axis = 1, inplace = True)

# wght > 100 and not obese?... wght < 100 and obese?
print(
  " Misclassified when cutting at 100kg:",
  data.loc[(data['Weight']>=100) & (data['obese']==0),:].shape[0], "\n",
  "Misclassified when cutting at 80kg:",
  data.loc[(data['Weight']>=80) & (data['obese']==0),:].shape[0]
)

print(gini_impurity(data.Gender))
print(gini_impurity(data.Height))
print(gini_impurity(data.Weight))

print(entropy(data.Gender))
print(entropy(data.Height))
print(entropy(data.Weight))

print(information_gain(data['obese'], data['Gender'] == 'Male'))