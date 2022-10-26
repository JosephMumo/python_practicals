import requests
import json

pokemon = input("Which pokemon do you want:? ")
pokemon = pokemon.lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

req = requests.get(url)
if req.status_code == 200:
    data = req.json()
    print(f"{data['height']}")
else:
    print("Enter a valid pokemon")
