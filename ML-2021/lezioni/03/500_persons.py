import pandas as pd
import numpy as np
import itertools

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
  func: function to be used to calculate Information Gain in case of classification.
  '''
  # n. of elements xj<O
  a = sum(mask)
  # n. of elements xj>=O
  b = mask.shape[0] - a
  
  if(a == 0 or b ==0): 
    ig = 0
  
  else:
    if y.dtypes != 'O':
      # the case of regression (continuous variable)
      ig = variance(y) - (a/(a+b)* variance(y[mask])) - (b/(a+b)*variance(y[-mask]))
    else:
      # the case of classification (continuous variable)
      impurity = a/(a+b)*func(y[mask])-b/(a+b)*func(y[-mask])
      ig = func(y) - impurity
  
  return ig

def categorical_options(a):
  '''
  Creates all possible combinations from a Pandas Series.
  a: Pandas Series from where to get all possible combinations. 
  '''
  a = a.unique()
  options = []
  for L in range(0, len(a)+1):
      for subset in itertools.combinations(a, L):
          subset = list(subset)
          options.append(subset)
  return options[1:-1]

def max_information_gain_split(x, y, func=entropy):
  '''
  Given a predictor & target variable, returns the best split, the error and the type 
  of variable based on a selected cost function.

  x: predictor variable as Pandas Series.
  y: target variable as Pandas Series.
  func: function to be used to calculate the best split.
  '''

  split_value = []
  ig = [] 

  numeric_variable = True if x.dtypes != 'O' else False

  # Create options according to variable type
  if numeric_variable:
    options = x.sort_values().unique()[1:]
  else: 
    options = categorical_options(x)

  # Calculate ig for all values
  for val in options:
    mask =   x < val if numeric_variable else x.isin(val)
    val_ig = information_gain(y, mask, func)
    # Append results
    ig.append(val_ig)
    split_value.append(val)

  # Check if there are more than 1 results if not, return False
  if len(ig) == 0:
    return(None,None,None, False)

  else:
  # Get results with highest IG
    best_ig = max(ig)
    best_ig_index = ig.index(best_ig)
    best_split = split_value[best_ig_index]
    return(best_ig,best_split,numeric_variable, True)


data = pd.read_csv("500_Person_Gender_Height_Weight_Index.csv")
data.head()

data['obese'] = (data.Index >= 4).astype('int')
data.drop('Index', axis = 1, inplace = True)

#print(gini_impurity(data.Gender))
#print(gini_impurity(data.Height))
#print(gini_impurity(data.Weight))

#print(entropy(data.Gender))
#print(entropy(data.Height))
#print(entropy(data.Weight))

#print(information_gain(data['obese'], data['Gender'] == 'Male'))

# wght > 100 and not obese?... wght < 100 and obese?
'''
print(
  " Misclassified when cutting at 100kg:",
  data.loc[(data['Weight']>=100) & (data['obese']==0),:].shape[0], "\n",
  "Misclassified when cutting at 80kg:",
  data.loc[(data['Weight']>=80) & (data['obese']==0),:].shape[0]
)

weight_ig, weight_slpit, _, _ = max_information_gain_split(data['Weight'], data['obese'],)  
height_ig, height_slpit, _, _ = max_information_gain_split(data['Height'], data['obese'],)  

print(
  "The best split for Weight is when the variable is less than ",
  weight_slpit,"\nInformation Gain for that split is:", weight_ig
)

print(
  "The best split for Height is when the variable is less than ",
  height_slpit,"\nInformation Gain for that split is:", height_ig
)
'''
x = data.drop('obese', axis= 1)
y = data['obese']
print('    col   |          best_ig          | best_split | numeric_variable ')
print('--------------------------------------------------------------------')
for col in x:
    b_ig, spl, num, _ = max_information_gain_split(x[col], y,)
    print(' %8r | %25r | %10r | %10r' % (col, b_ig, spl, num))


