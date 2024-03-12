from postcode_class import *
from payload_class import *
import json
import requests

# postcode = "se181bb"
# parser = GETPostcodeParser(postcode)
# parser.write_json_file("se181bb_json.json")
#
# print(parser.postcode)
# print(parser.status)
# print(parser.postcode)
# print(parser.region)
# print(parser.longitude)
# print(parser.latitude)

# payload = {"postcodes": ["se181bb", "se288at"]}
#
# res = requests.post("https://api.postcodes.io/postcodes", data=payload)
# api_dict = res.json()
# with open("post_json_file.json", "w") as json_file:
#     json.dump(api_dict, json_file)

payload = {"postcodes": ["se181bb", "se288at"]}
postcode_parser = POSTPostcodeParser(payload)
postcode_parser.save_to_json_file("post_json_file.json")

