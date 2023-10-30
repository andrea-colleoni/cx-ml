import entropy

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