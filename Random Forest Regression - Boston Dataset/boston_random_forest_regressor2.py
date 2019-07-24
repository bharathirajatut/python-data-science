# Random Forest Classification

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
from sklearn.datasets import load_boston
boston = load_boston()

#boston is a dictionary.
print(boston.keys())

#get shape of data
print(boston.data.shape)

#get feature names
print(boston.feature_names)

#about the dataset
print(boston.DESCR)

#create boston dataframe
dataset = pd.DataFrame(boston.data)

#alternatively you can get the dataset using
#https://archive.ics.uci.edu/ml/machine-learning-databases/housing/
#dataset1=pd.read_table("housing.csv")
#assign column name
dataset.columns = boston.feature_names

#add target variable
dataset['PRICE'] = boston.target

#Summary Statistics
print(dataset.describe())

#split x and y
x = dataset.drop('PRICE', axis = 1)
y = dataset['PRICE']

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)



# Fitting Random Forest Regression to the Training set
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 50, random_state = 0)
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)


# Evaluating the Algorithm
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


"""

Result for n_estimators=50

Mean Absolute Error: 2.55118110236
Mean Squared Error: 15.7084229921
Root Mean Squared Error: 3.96338529443



Result for n_estimators=40

Mean Absolute Error: 2.52090551181
Mean Squared Error: 15.0942913386
Root Mean Squared Error: 3.88513723549



Result for n_estimators=30

Mean Absolute Error: 2.54162729659
Mean Squared Error: 15.5711529309
Root Mean Squared Error: 3.94603002154



Result for n_estimators=60

Mean Absolute Error: 2.55049868766
Mean Squared Error: 15.9157054243
Root Mean Squared Error: 3.98944926328



Result for n_estimators=100

Mean Absolute Error: 2.55906299213
Mean Squared Error: 16.7221060866
Root Mean Squared Error: 4.0892671821

"""  
