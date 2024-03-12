from url_parser import *

postcode = input("Input a postcode\n")
parser = APIURLParser(postcode)

print(parser.postcode)
print(parser.status)
print(parser.postcode)
print(parser.region)
print(parser.longitude)
print(parser.latitude)



