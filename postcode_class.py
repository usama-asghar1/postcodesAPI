import json


class PostcodeParser:

    def __init__(self, postcode_file):
        postcode_info = self._open_json_file(postcode_file)
        self.status = postcode_info['status']
        self.result = postcode_info['result']
        self.postcode = self.result['postcode']
        self.region = self.result['region']
        self.longitude = self.result['longitude']
        self.latitude = self.result['latitude']

    def _open_json_file(self, file):
        with open(file) as postcode_file:
            return json.load(postcode_file)


