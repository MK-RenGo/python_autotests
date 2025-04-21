import requests

URL = 'https://api.pokemonbattle-stage.ru/v2'
TOKEN = 'a4d8929394e0486014f535030b7f93ad'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

name_change = {
    "pokemon_id": "8832",
    "name": "name name name",
    "photo_id": 2
}

add_pokeball = {
    "pokemon_id": "8832"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.text)'''   # Создать покемона

'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = name_change) 
print(response_create.text)'''  # Изменить покемона

'''response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pokeball) 
print(response_create.text)'''  # поймать в покебол