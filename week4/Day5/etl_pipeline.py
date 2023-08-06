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
    enemies = [my_character_data[x]['enemies'] for x in range(len(my_character_data))] # No enemies listed in dict
    park_attractions = [my_character_data[x]['parkAttractions'] for x in range(len(my_character_data))] # Park Attractions
    # Step 2: Create dictionary with each available variable
    my_character_dict = {
    'names': names,
    'tv_shows': tv_shows,
    'park_attractions': park_attractions}
    # Step 3: Convert Dictionary to DataFrame
    df = pd.DataFrame.from_dict(my_character_dict)
    # Create a .csv file:
    df.to_csv('data/etl_pipeline.csv', index=False)
disney('https://api.disneyapi.dev/character')