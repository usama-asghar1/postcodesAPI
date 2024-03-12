import json
import requests


class GETPostcodeParser:

    def __init__(self, postcode):
        url = f"https://api.postcodes.io/postcodes/{postcode}"
        self.postcode_info = self._get_json_from_url(url)
        self.status = self.postcode_info['status']
        self.result = self.postcode_info['result']
        self.postcode = self.result['postcode']
        self.region = self.result['region']
        self.longitude = self.result['longitude']
        self.latitude = self.result['latitude']

    def _get_json_from_url(self, url):
        res = requests.get(url)
        api_dict = res.json()
        return api_dict

    def write_json_file(self, filename):
        with open(filename, "w") as json_file:
            json.dump(self.postcode_info, json_file)

