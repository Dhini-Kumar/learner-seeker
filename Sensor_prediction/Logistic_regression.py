import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import seaborn as sn

# Reading Data 
dataset = pd.read_csv('Final_concat/Final_dataset.csv', header = None) # header = 0 to include the first row


#Assigning X & y values
X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0].values

# Splitting data for training and test 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr', random_state = 0)
classifier.fit(X_train, y_train.ravel())

#save the model as .YAML Format with using pickle package
file = classifier
filename = 'trained_model/eagle_model.yml'
pickle.dump(file, open(filename,'wb'))


