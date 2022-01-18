import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Read the data
data = pd.read_csv('data/AER_credit_card_data.csv', 
                   true_values=['yes'], false_values=['no'] )

# Select target
y = data.card

# Select predictors
X = data.drop(['card'], axis=1)

print('Number of rows in the dataset:', X.shape[0])
print(X.head())

my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_scores = cross_val_score(my_pipeline, X, y, cv=5, scoring='accuracy')

print(f"Cross-validation accuracy: {cv_scores.mean()}")

expenditures_cardholders = X.expenditure[y]
expenditures_noncardholders = X.expenditure[~y]

print(expenditures_cardholders)
print(expenditures_noncardholders)
