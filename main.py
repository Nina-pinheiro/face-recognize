import json

item = json.loads('[{"id":1, "text": "Item1"}')

for item in items:
    print(item['text'])
    