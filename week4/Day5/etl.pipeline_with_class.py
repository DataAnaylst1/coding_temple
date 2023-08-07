import pandas as pd
import requests

class Cartoons:

    def __init__(self, filepath='https://api.disneyapi.dev/character'):
        self.url = filepath
        self.sql_url = 'postgresql://ithcdykt:ssKx4F2ElnpBKHa8-1dN_MqKnuupdyyV@hansken.db.elephantsql.com/ithcdykt'

    def disney(self):
        self.response = requests.get(self.url)
        self.my_character_data = self.response.json()['data']
        # Step 1: Create variable for each required column
        names = [self.my_character_data[x]['name'] for x in range(len(self.my_character_data))] # Name
        tv_shows = [self.my_character_data[x]['tvShows'] for x in range(len(self.my_character_data))] # Tv Shows
        allies = [self.my_character_data[x]['allies'] for x in range(len(self.my_character_data))] # Checked, no allies listed in dict
        enemies = [self.my_character_data[x]['enemies'] for x in range(len(self.my_character_data))] # No enemies listed in dict
        park_attractions = [self.my_character_data[x]['parkAttractions'] for x in range(len(self.my_character_data))] # Park Attractions
        # Step 2: Create dictionary with each available variable
        my_character_dict = {
        'names': names,
        'tv_shows': [', '.join(shows) if shows else ' ' for shows in tv_shows],
        'films': [','.join(film) if film else 0 for film in films],
        'shortFilms': [','.join(shorts) if shorts else 0 for shorts in short_films],
        'allies': [','.join(ally) if ally else ' ' for ally in allies],
        'enemies': [','.join(enemy) if enemy else ' ' for enemy in enemies],
        'park_attractions': [', '.join(attractions) if attractions else ' ' for attractions in park_attractions]
        }
        # Step 3: Convert Dictionary to DataFrame
        self.df = pd.DataFrame.from_dict(my_character_dict)
    def convert_to_csv(self):
        # Create a .csv file:
        self.df.to_csv('data/etl_pipeline.csv', index=False)
    # disney('https://api.disneyapi.dev/character')
if __name__ =='__main__':
    c = Cartoons('https://api.disneyapi.dev/character')
    print(c.disney())
    print(c.convert_to_csv)
    