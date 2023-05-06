import requests
import json

#request a PokeApi
req = requests.get('https://www.pokeapi.co/api/v2/pokemon/bulbasaur')
if req.status_code == 200:
    print("Conectado con la API de manera satisfactoria")

response = json.loads(req.content)
print("El mejor pokemon es: " + response['name'])
req2 = requests.get('https://pokeapi.co/api/v2/type/12/')
type = json.loads(req2.content)
print("Su primer tipo es: " + type['name'])

req3 = requests.get('https://pokeapi.co/api/v2/type/4/')
type2 = json.loads(req3.content)
print("Su primer tipo es: " + type2['name'])

req4 = requests.get('https://pokeapi.co/api/v2/ability/34/')
hab = json.loads(req4.content)
print("Su habilidad oculta es: " + hab['name'])
