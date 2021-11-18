import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns


def load_file(file_name:str):
    """ Uploading a file for reading """
    filepath = f"./data/{file_name}"
    data = pd.read_csv(filepath, index_col="Date", parse_dates=True)
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


spotify_data = load_file("spotify.csv")
plt.figure(figsize=(14, 6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of fuck u")
sns.lineplot(data=spotify_data['Despacito'], label='Despacito')
plt.xlabel("Dateee")
plt.show()
