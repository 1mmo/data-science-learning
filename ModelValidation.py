import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


melbourne_file_path = 'data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print('melbourne_data = ', melbourne_data)
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
print('filtered =', filtered_melbourne_data)
# Choose target and features
y = filtered_melbourne_data.Price
print('y = \n', y)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize',
                      'BuildingArea', 'YearBuilt', 'Lattitude',
                      'Longtitude']
X = filtered_melbourne_data[melbourne_features]
print("X = \n", X)

# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
print(melbourne_model.fit(X, y))

# Calculate the mean absolute error
predicted_home_prices = melbourne_model.predict(X)
print('predicted = ', predicted_home_prices)
print(mean_absolute_error(y, predicted_home_prices))

# split data into training and validation data, for both features and target
# Thr split is based on a random number generator. 
# Supplying a numeric value to the random_state argument 
# guarantees we get the same split every time 
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
print('VAL X = \n', val_X)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get pridected price on validation data
val_predictions = melbourne_model.predict(val_X)
print('val_predictions = \n', val_predictions)
print(mean_absolute_error(val_y, val_predictions))
