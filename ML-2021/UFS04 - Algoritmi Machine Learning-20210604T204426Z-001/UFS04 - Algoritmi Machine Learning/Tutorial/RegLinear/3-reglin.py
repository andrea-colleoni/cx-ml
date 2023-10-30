import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def linear_regression(x, y):
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()
    
    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean)**2).sum()
    B1 = B1_num / B1_den
    
    B0 = y_mean - (B1*x_mean)
    
    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))
    
    return (B0, B1, reg_line)

def corr_coef(x, y):
    N = len(x)
    
    num = (N * (x*y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x**2).sum() - x.sum()**2) * (N * (y**2).sum() - y.sum()**2))
    R = num / den
    return R

def predict(B0, B1, new_x):
    y = B0 + B1 * new_x
    return y

# The Square of Error function
def MSE(b, m, x_points, y_points):
    totalError = 0
    error = 0
    npoints = len(x_points)
	
    # MSE = ((y_initial - y_predicted)^2) / Number of rows
    for i in range(0, npoints):
        x = x_points[i]
        y = y_points[i]
        error = ((y - (m*x + b)) ** 2)
        totalError = totalError + error

    totalError = totalError / npoints
    return totalError

data = pd.read_csv('WeatherData.csv')
x = data['Temperature(C)']
y = data['Humidity']

B0, B1, reg_line = linear_regression(x, y)
print('Regression Line: ', reg_line)
R = corr_coef(x, y)
print('Correlation Coef.: ', R)
print('"Goodness of Fit": ', R**2)
mse = MSE(B0, R, x, y)
print('MSE: ', mse)

plt.figure(figsize=(12,5))
plt.scatter(x, y, s=300, linewidths=1, edgecolor='black')
text = '''X Mean: {} Years
Y Mean: ${}
R: {}
R^2: {}
y = {} + {}X'''.format(round(x.mean(), 2), 
                       round(y.mean(), 2), 
                       round(R, 4), 
                       round(R**2, 4),
                       round(B0, 3),
                       round(B1, 3))
plt.text(x=10, y=10, s=text, fontsize=12, bbox={'facecolor': 'grey', 'alpha': 0.2, 'pad': 10})
plt.title('Weather')
plt.xlabel('Temperature(C)', fontsize=15)
plt.ylabel('Humidity', fontsize=15)
plt.plot(x, B0 + B1*x, c = 'r', linewidth=5, alpha=.5, solid_capstyle='round')
plt.scatter(x=x.mean(), y=y.mean(), marker='*', s=10**2.5, c='r') # average point
plt.show()