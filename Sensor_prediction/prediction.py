import pandas as pd
import pickle
import os, random
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

loaded_model = pickle.load(open('trained_model/eagle_model.yml', 'rb'))

# New data for prediction

new_dataset = pd.read_csv('Test_data/Lose_test.csv', header = None)
Trans_data = new_dataset.T
to_predict = Trans_data.iloc[:,:].values

# Predicting the Test set results
y_pred = loaded_model.predict(to_predict)

if y_pred == 1:
	print ("Nut is tight for ",os.path.basename("Test_data/Lose_test.csv"))
else:
	print ("Nut is lose for ",os.path.basename("Test_data/Lose_test.csv"))
