# Postcodes API

The aim of this project was to demonstrate communication with open Postcodes API and store the information to a JSON file.

- GETPostcodeParser - GET Request performed by inputing a URL and a JSON file will be created

```
api.postcodes.io/postcodes/{:postcode}
```
* The class will accept a postcode as an input and provide the attributes to be printed as the result
* The class has a .write_json_file method which can be instanciated to output a JSON file 
