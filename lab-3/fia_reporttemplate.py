# -*- coding: utf-8 -*-
"""FIA_ReportTemplate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GoDxLN9l62EgC4X6_wOGoLLqJM6Gbrhy

# FAF.FIA16.1 -- Artificial Intelligence Fundamentals

> **Lab 3:** Linear Regression \\
> **Performed by:** Furdui Alexandru, group FAF-192 \\
> **Verified by:** Mihail Gavrilita, asist. univ.

## Imports and Utils
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge

"""## Task 1 -- Import your data. Analyze it via common statistical approaches. Cleanse the data if necessary."""

#convert txt to csv
read_file = pd.read_csv ('apartmentComplexData.txt')
read_file.to_csv ('apartmentComplexData.csv', index=None)

df = pd.read_csv('apartmentComplexData.csv', usecols=[2, 3, 4, 5, 6, 8])

#rename columns
df.columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'medianCompexValue']
#replace NaN values with column mean
df.fillna(df.mean(), inplace=True)

"""## Task 2 -- Train your model by applying linear regression."""

#split the data into training and testing sets
X = df[['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr']]
y = df['medianCompexValue']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predict the medianCompexValue for the test set
regressor_y_pred = regressor.predict(X_test)

#calculate rmse
mse = mean_squared_error(y_test, regressor_y_pred)
rmse = np.sqrt(mse)
print('RMSE: ', rmse)
#prints: RMSE: 105453.7614875964

"""## Task 3 -- Show the prediction power of your model by attempting to predict the price of a new house"""

#apartament to predict values
linear_prediction = np.array([[74, 200, 342, 234, 90]])

#predicting the apartment using linear regression
linear_prediction_median_compex_value = regressor.predict(linear_prediction)

print('Predicted medianCompexValue value using linear regression: ', linear_prediction_median_compex_value)
#prints: Predicted medianCompexValue value using linear regression: 184830.21801261377

"""# Task 4 -- Re-train your model. Use Ridge, Lasso or Elastic Net regularization."""

rige_regressor = Ridge(alpha=100)
rige_regressor.fit(X_train, y_train)

#predict using X_test as input 
ridge_y_pred = rige_regressor.predict(X_test)

#calculate rmse for Ridge
ridge_mse = mean_squared_error(y_test, ridge_y_pred)
ridge_rmse = np.sqrt(ridge_mse)
print('RMSE for Ridge:', ridge_rmse)
#RMSE for Ridge: 105453.7602732192

"""# Task 5 -- Score and compare the scores of the models you have implemented. Interpret the result."""

#apartament to predict values
ridge_prediction = np.array([[74, 200, 342, 234, 90]])

#predicting the apartment using Ridge
ridge_prediction_median_compex_value = rige_regressor.predict(ridge_prediction)

print('Predicted medianCompexValue for the new apartment complex using Ridge: ', ridge_prediction_median_compex_value)
#prints: Predicted medianCompexValue value using Ridge regression: 184827.36920557747

"""comparing 2 RMSE values for Linear and Ridge regression which is 105453.7614875964 and 105453.7602732192 respectively, we can see that Ridge regression performs sligtly better as the RMSE value is smaller. This means that the predicted apartment value by Ridge regression, is closer to truth

## Conclusions:

Concluding, i can say that even if the Ridge regression performed a bit better, it did not make a very big difference from Linear regression prediction. This is mostly because the dataset is very large or because the alpha value for the Ridge regression is not set to this dataset(i tried my best to choose the most appropriate value)

## Bibliography:

https://datatofish.com/convert-text-file-to-csv-using-python-tool-included/ -- Convert from text to csv

https://www.javatpoint.com/rsme-root-mean-square-error-in-python -- What is rmse and how to calculate it

https://realpython.com/linear-regression-in-python/ -- How to implement linear regresion model

https://machinelearningmastery.com/ridge-regression-with-python/ -- How to implement ridge regression model
"""