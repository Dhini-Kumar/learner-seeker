import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading Data 
dataset = pd.read_csv('dummy.csv')

X_T = dataset.T #Transposing the matrix 
#print(X_T)

#Assigning X & y values
X = X_T.iloc[:,0:-1].values
y = X_T.iloc[:,-1].values
#print (X, y)


# Splitting data for training and test 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr', random_state = 0)
classifier.fit(X_train, y_train.ravel())

# Predicting the Test set results
y_pred = classifier.predict(X_test)
#print (X_train)
print (X_test)
print (y_pred)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)


#print (classifier.classes_)
print (classifier.intercept_)
print (classifier.coef_)
print (classifier.score(X, y))

from sklearn.metrics import accuracy_score 
print ("Accuracy : ", accuracy_score(y_test, y_pred)) 
# Visualising the Training set results
#from matplotlib.colors import ListedColormap
#X_set, y_set = X_train, y_train


