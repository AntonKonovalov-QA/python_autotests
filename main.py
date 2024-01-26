"""
Kolorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': 'c1042ad5f05f25e5041660d00d5e63bb'
}



response = requests.post(url=f'{URL}/pokemons', json={"name": "generate", "photo": "generate"}, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')

id = response.json()["id"]

response1 = requests.put(url=f'{URL}/pokemons', json={"pokemon_id": id, "name": "New Pocemon", "photo": "https://dolnikov.ru/pokemons/albums/011.png"}, headers=HEADER, timeout=5)
print(f'Статус код: {response1.status_code}. Сообщение: {response1.json()["message"]}')

response2 = requests.post(url=f'{URL}/trainers/add_pokeball', json={"pokemon_id": id}, headers=HEADER, timeout=5)
print(f'Статус код: {response2.status_code}. Сообщение: {response2.json()["message"]}')