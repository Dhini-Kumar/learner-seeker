import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('position_salary.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#Splitting Dataset
""" from sklearn.cross_validation import train_test_split
X_trai, X_test, y_train, y_test = train_test-split(X,y test_size = 0.2, randon_state = 0)"""

#Feature Scaling
""" from sklearn.preprocessing importStandardScaler
Sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#Fitting Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

#Predicting new result
#y_pred = regressor.predict([[7.5]])

# Visualising the Decision Tree Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
