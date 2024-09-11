import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a1ebd56f5be70dd67fea39bbed7b255'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
body_pokemons = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_name = {
    "pokemon_id": "69980",
    "name": "Динозавр"
}

body_pokeball = {
    "pokemon_id": "69980"
}

response_pokemons = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response_pokemons.text)

response_name = requests.put (url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

response_pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
