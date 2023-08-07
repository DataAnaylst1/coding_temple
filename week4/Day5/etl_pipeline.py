import pandas as pd
import requests, json
def disney(filepath):
    # def upload_filepaith(filepath): # create a filepath to upload the API object
    url = 'https://api.disneyapi.dev/character'
    response = requests.get(url)
    # Now, to store required fields from API into a DataFrame
    my_character_data = response.json()['data']
    # Step 1: Create variable for each required column
    names = [my_character_data[x]['name'] for x in range(len(my_character_data))] # Name
    tv_shows = [my_character_data[x]['tvShows'] for x in range(len(my_character_data))] # Tv Shows
    allies = [my_character_data[x]['allies'] for x in range(len(my_character_data))] # Checked, no allies listed in dict
    enemies = [my_character_data[x]['enemies'] for x in range(len(my_character_data))]
    films = [my_character_data[x]['films'] for x in range(len(my_character_data))] # films listed in dict
    short_films = [my_character_data[x]['shortFilms'] for x in range(len(my_character_data))]
    park_attractions = [my_character_data[x]['parkAttractions'] for x in range(len(my_character_data))] # Park Attractions
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
    df = pd.DataFrame.from_dict(my_character_dict)
    df
    # Create a .csv file:
    df.to_csv('data/etl_pipeline.csv', index=False)
disney('https://api.disneyapi.dev/character')