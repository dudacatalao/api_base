import requests

url = 'https://rickandmortyapi.com/api/character/20'

request = requests.get(url)

data = request.json()

nome = data[ 'name']

print(data)