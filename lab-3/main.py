import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge

read_file = pd.read_csv ('apartmentComplexData.txt')
read_file.to_csv ('apartmentComplexData.csv', index=None)

file_data = pd.read_csv('apartmentComplexData.csv', usecols=[2, 3, 4, 5, 6, 8])

file_data.columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'medianCompexValue']
file_data = file_data.fillna(0)
file_data.drop_duplicates()
# print(file_data)

#split the data into training and testing sets
X = file_data[['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr']]
y = file_data['medianCompexValue']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=10)
 
regressor = LinearRegression()
regressor.fit(X_train, y_train)
linear_prediction = np.array([[52.0, 2491.0, 474.0, 1098.0, 468.0]])

#predicting the apartment using linear regression
linear_prediction_median_compex_value = regressor.predict(linear_prediction)

print('Predicted medianCompexValue using linear regression: ', linear_prediction_median_compex_value)

from sklearn.metrics import r2_score
regressor_y_pred = regressor.predict(X_test)
linear_r2 = r2_score(y_test, regressor_y_pred)

ridge_regressor = Ridge(alpha=10)
ridge_regressor.fit(X_train, y_train)

ridge_y_pred = ridge_regressor.predict(X_test)

ridge_prediction = np.array([[52.0, 2491.0, 474.0, 1098.0, 468.0]])
ridge_prediction_median_compex_value = ridge_regressor.predict(ridge_prediction)

print('Predicted medianCompexValue using Ridge: ', ridge_prediction_median_compex_value) 

ridge_r2 = r2_score(y_test, ridge_y_pred)
print("R2 score for ridge : ",  ridge_r2)
print("R2 score for linear: ", linear_r2) 



mean_values = file_data.mean() 
median_values = file_data.median()
std_deviation = file_data.std()

print("mean ",mean_values)
print("median ",median_values)
print("deviation ",std_deviation)
import matplotlib.pyplot as plt
file_data[['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr']].plot()
file_data[['medianCompexValue']].plot()
# plt.show()
import pandas as pd 

mean_rounded = mean_values.round(2)
median_rounded = median_values.round(2)
std_rounded = std_deviation.round(2)
 
data = pd.DataFrame({'Mean': mean_rounded, 'Median': median_rounded, 'Standard Deviation': std_rounded})
 
print(data)
