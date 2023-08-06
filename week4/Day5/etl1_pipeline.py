# Import statements:
import requests, json, pandas as pd

# Loaded in data from API object for all characters
url = 'https://api.disneyapi.dev/character'
response = requests.get(url)
print(response)
print(response.json())
my_character_data = response.json()['data']
names = [my_character_data[x]['name'] for x in range(len(my_character_data))]
tv_shows = [my_character_data[x]['tvShows'] for x in range(len(my_character_data))]
# my_character_data = response.json()['data']
# names = [my_character_data[x]['name'] for x in range(len(my_character_data))]
# names
# my_character_data = pd.DataFrame.from_dict(my_character_data)
# removal = my_character_data.columns
# for item in removal[0]:
#     my_character_data.drop(item, axis=1, inplace=True)
# for item in removal[4]:
#     my_character_data.drop(item, axis=1, inplace=True)
# for item in removal[8]:
#     my_character_data.drop(item, axis=1, inplace=True)
# for item in removal[10:]:
#     my_character_data.drop(item, axis=1, inplace=True)
# my_character_data.columns
allies = [my_character_data[x]['allies'] for x in range(len(my_character_data))] # Checked, no allies listed in dict
enemies = [my_character_data[x]['enemies'] for x in range(len(my_character_data))] #no enemies listed in dict
park_attractions = [my_character_data[x]['parkAttractions'] for x in range(len(my_character_data))]
my_character_dict = {
    'names': names,
    'tv_shows': tv_shows,
    'allies': allies,
    'enemies': enemies,
    'park_attractions': park_attractions
}
df = pd.DataFrame.from_dict(my_character_dict)
df 
# df1 = df.groupby(['names'])

