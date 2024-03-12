import json
import requests


class POSTPostcodeParser:

    def __init__(self, payload):
        self.payload = payload
        self.postcode_info = self._get_postcode_info()

    def _get_postcode_info(self):
        res = requests.post("https://api.postcodes.io/postcodes", data=self.payload)
        api_dict = res.json()
        return api_dict

    def save_to_json_file(self, filename):
        with open(filename, "w") as json_file:
            json.dump(self.postcode_info, json_file)