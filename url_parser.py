import json
import requests
from postcode_class import PostcodeParser


class APIURLParser(PostcodeParser):
    def __init__(self, postcode):
        url = f"https://api.postcodes.io/postcodes/{postcode}"
        postcode_info = self._get_json_from_url(url)
        super().__init__(postcode_info)

    def _get_json_from_url(self, url):
        res = requests.get(url)
        api_dict = res.json()
        with open("json_file.json", "w") as json_file:
            json.dump(api_dict, json_file)
        return "json_file.json"

