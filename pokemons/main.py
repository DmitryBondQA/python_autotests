import requests

host = 'https://api.pokemonbattle.me:9104'
token = 'bd3ecd721b71b1294ebdbfecd6b731e3'

'''response = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {'Content-Type': 'application/json',
              'trainer_token' : token})'''

'''response = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6091",
    "name": "bondQA",
    "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}, headers = {'Content-Type': 'application/json',
              'trainer_token' : token})'''

response = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6091"
}, headers = {'Content-Type': 'application/json',
              'trainer_token' : token})

print(response.text)