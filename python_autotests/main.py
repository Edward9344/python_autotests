import requests

HOST = 'https://api.pokemonbattle-stage.me:9101'
token = '5af27b427e705fe7f2a3c71624a2fdf4'
pokemon_id = '1909'

# Запрос на создание покемонв
responce = requests.post(url=f'{HOST}/pokemons', json={
                        'name': 'Жмых',
                        'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
                        },
                        headers={'Content-types': 'application/json',
                                 'trainer_token': f'{token}'})

print(responce.status_code, responce.reason, responce.text)

# Запрос на изменение имени покемона
responce = requests.put(url=f'{HOST}/pokemons', json={
                        'pokemon_id': f'{pokemon_id}',
                        'name': 'bababa',
                        'photo': 'https://dolnikov.ru/pokemons/albums/008.png'
                        },
                        headers={'Content-types':'application/json',
                                 'trainer_token': f'{token}'})

print(responce.status_code, responce.reason, responce.text)

# Запрос на добаление покемона в покебол
responce = requests.post(url=f'{HOST}/trainers/add_pokeball', json={
                        'pokemon_id': f'{pokemon_id}'
                        },
                        headers={'Content-types': 'application/json',
                                 'trainer_token': f'{token}'})

print(responce.status_code, responce.reason, responce.text)