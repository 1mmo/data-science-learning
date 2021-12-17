import pandas as pd
from sklearn.tree import DecisionTreeRegressor


melbourne_file_path = "data/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.head())
print(melbourne_data.describe())
print(melbourne_data.columns)
melboure_data = melbourne_data.dropna(axis=0) # dropna drops missing values
y = melbourne_data.Price
print(y)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 
                      'Lattitude', 'Longtitude']
x = melbourne_data[melbourne_features]
print(x.describe())
print(x.head())
melbourne_model = DecisionTreeRegressor(random_state=1)
# Fit model
melbourne_model.fit(x, y)
print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))
print("Real price")
print(y.head())
