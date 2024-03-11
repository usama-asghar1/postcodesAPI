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


postcode_se288at = PostcodeParser("new_json_file.json")

print(postcode_se288at.status)
print(postcode_se288at.result)
print(postcode_se288at.postcode)
print(postcode_se288at.region)
print(postcode_se288at.longitude)
print(postcode_se288at.latitude)
