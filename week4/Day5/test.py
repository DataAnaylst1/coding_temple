import pandas as pd, requests
new_data = []
url = 'https://api.disneyapi.dev/character'
response = requests.get(url)
print(response)
print(response.json())
my_character_data = response.json()['data']

def get_character_info(data):
    """
    Input: response object from API
    Takes the response and creates a dictionary containing the fields we want from the racer's information
    Output: List object containing a dictionary for each racer in the response object
    """
    new_data = []
    for character in data:
        character_dict ={}
        character_name = f'{character["Driver"]["givenName"]} {character["Driver"]["familyName"]}'

        character_dict[character_name] = {
            'first_name' : character['Driver']['givenName'],
            'last_name' : character['Driver']['familyName'],
            'position' : character['position'],
            'wins' : character['wins'],
            'DOB' : character['Driver']['dateOfBirth'],
            'nationality' : character['Driver']['nationality'],
            'constructor' : character['Constructors'][0]['name']
        }
        new_data.append(character_dict)
    return new_data

get_character_info(my_character_data)