import numpy as np
import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from matplotlib import pyplot as plt
from pdpbox import pdp, get_dataset, info_plots


data = pd.read_csv('data/FIFA.csv')

y = (data['Man of the Match'] == "Yes")
feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
X = data[feature_names]
X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=1)
tree_model = DecisionTreeClassifier(random_state=0, 
                                    max_depth=5, 
                                    min_samples_split=5).fit(X_train, y_train)

tree_graph = tree.export_graphviz(tree_model, out_file=None, feature_names=feature_names)
graphviz.Source(tree_graph)

# Create the data that we will plot
pdp_goals = pdp.pdp_isolate(model=tree_model, dataset=X_valid, 
                            model_features=feature_names, 
                            feature='Goal Scored')
# plot it 
pdp.pdp_plot(pdp_goals, 'Goal Scored')
plt.show()
