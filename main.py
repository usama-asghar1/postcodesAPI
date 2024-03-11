import requests
import json

res = requests.get("https://api.postcodes.io/postcodes/se288at")
api_dict = res.json()

with open("new_json_file.json", "w") as json_file:
    json.dump(api_dict, json_file)

