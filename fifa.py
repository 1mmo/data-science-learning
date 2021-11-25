import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns


def load_file(file_name:str):
    """ Uploading a file for reading """
    filepath = f"./data/{file_name}"
    data = pd.read_csv(filepath, index_col="Id")
    get_five(data)
    return data

def get_five(data) -> None:
    """ Print the first 5 rows of the data """
    first_five = data.head()
    last_five = data.tail()
    print(f'Первые: \n {first_five}')
    print(f'Последние: \n {last_five}')


#fifa_data = load_file(file_name="fifa.csv")
#print(plt.figure(figsize=(16, 6)))
#print(sns.lineplot(data=fifa_data))
#print(type(fifa_data))

"""
spotify_data = load_file("spotify.csv")
plt.figure(figsize=(14, 6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of fuck u")
sns.lineplot(data=spotify_data['Despacito'], label='Despacito')
plt.xlabel("Dateee")
plt.show()
"""

"""
flight_data = load_file("flight_delays.csv")
print(flight_data)
plt.figure(figsize=(14, 7))
plt.title("Average Arrival Delay for Each Airline by Month")
sns.heatmap(data=flight_data, annot=True)
plt.xlabel("Airline")
plt.show()
"""

"""
insurance_data = load_file("insurance.csv")
plt.figure(figsize=(16, 6))
plt.title("Just")
#sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)
#sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges']) 
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'],
                hue=insurance_data['smoker'])
plt.show()
"""


#iris_data = load_file('iris.csv')
iris_set_data = load_file("iris_setosa.csv")
iris_ver_data = load_file("iris_versicolor.csv")
iris_vir_data = load_file("iris_virginica.csv")
#plt.figure(figsize=(16, 6))
#plt.title("Flowers")
#sns.displot(a=iris_data['Petal Length (cm)'], kde=False)
#sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
#sns.jointplot(x=iris_data['Petal Length (cm)'], 
#              y=iris_data['Sepal Width (cm)'],
#             kind='kde')


""" COLOR_CODED PLOTS """

"""
sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)
plt.title("Histogram of Petal Lengths, by Species")
plt.legend()
plt.show()
"""

""" KDE PLOTS FOR EACH SPECIES """
sns.kdeplot(data=iris_set_data["Petal Length (cm)"], label="Iris-setosa", shade=True)
sns.kdeplot(data=iris_ver_data["Petal Length (cm)"], label="Iris-setosa", shade=True)
sns.kdeplot(data=iris_vir_data["Petal Length (cm)"], label="Irits-setosa", shade=True)
plt.title("Distribution of Petal Lengths, by Species")
plt.show()
