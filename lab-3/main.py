import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge

#convert txt to csv
read_file = pd.read_csv ('apartmentComplexData.txt')
read_file.to_csv ('apartmentComplexData.csv', index=None)

df = pd.read_csv('apartmentComplexData.csv', usecols=[2, 3, 4, 5, 6, 8])

#rename columns
df.columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'medianCompexValue']
#replace NaN values with column mean
df.fillna(df.mean(), inplace=True)

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

#apartament to predict values
linear_prediction = np.array([[74, 200, 342, 234, 90]])

#predicting the apartment using linear regression
linear_prediction_median_compex_value = regressor.predict(linear_prediction)

print('Predicted medianCompexValue value using linear regression: ', linear_prediction_median_compex_value)
#prints: Predicted medianCompexValue value using linear regression: 184830.21801261377

rige_regressor = Ridge(alpha=100)
rige_regressor.fit(X_train, y_train)

#predict using X_test as input 
ridge_y_pred = rige_regressor.predict(X_test)

#calculate rmse for Ridge
ridge_mse = mean_squared_error(y_test, ridge_y_pred)
ridge_rmse = np.sqrt(ridge_mse)
print('RMSE for Ridge:', ridge_rmse)
#RMSE for Ridge: 105453.7602732192

#apartament to predict values
ridge_prediction = np.array([[74, 200, 342, 234, 90]])

#predicting the apartment using Ridge
ridge_prediction_median_compex_value = rige_regressor.predict(ridge_prediction)

print('Predicted medianCompexValue for the new apartment complex using Ridge: ', ridge_prediction_median_compex_value)
#prints: Predicted medianCompexValue value using Ridge regression: 184827.36920557747