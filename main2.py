import requests
import json

response = requests.get('http://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])

