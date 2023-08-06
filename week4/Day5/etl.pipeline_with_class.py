import pandas as pd
import requests

class Cartoons:

    def __init__(self, filepath='https://api.disneyapi.dev/character'):
        self.url = filepath

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
        'tv_shows': tv_shows,
        'park_attractions': park_attractions}
        # Step 3: Convert Dictionary to DataFrame
        self.df = pd.DataFrame.from_dict(my_character_dict)
        # Create a .csv file:
        self.df.to_csv('data/etl_pipeline.csv', index=False)
    disney('https://api.disneyapi.dev/character')