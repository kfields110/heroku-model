import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def house_prediction(marks):

    # data = pd.read_csv('C:\Users\kfiel\DataInternship\Flask_Web_App\Data\data.csv')

    # X= data[['bedrooms', 'bathrooms', 'sqft_living', 'yr_built']]
    # y = data['price']

    # X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .2, random_state = 0)

    # regressor = LinearRegression()
    # regressor.fit(X_train.values, y_train)

    # print(regressor.predict([[3.0, 2.5, 2000, 2000]]))
    
    model = pickle.load(open('model.pkl', 'rb'))
    return model.predict(marks)

