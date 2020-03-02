import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

# Reading Data 
dataset = pd.read_csv('sensor_data.csv')

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

# New data for prediction
new_dataset = pd.read_csv('to_pred.csv')
Trans_data = new_dataset.T
to_predict = Trans_data.iloc[0:,:].values

# Predicting the Test set results
y_pred = classifier.predict(to_predict)

print (y_pred)

# Making the Confusion Matrix
#confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
#sn.heatmap(confusion_matrix, annot=True)
#print (confusion_matrix)


#from sklearn.metrics import accuracy_score 
#print ("Accuracy : ", accuracy_score(y_test, y_pred)) 




