import json


with open('148.json') as art_file:
    art = json.load(art_file)
    print(art['description'])