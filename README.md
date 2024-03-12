# Postcodes API

The aim of this project was to demonstrate communication with open Postcodes API and store the information to a JSON file. The project also contains testing using the unittest framework.

<details>
  <summary>GETPostcodeParser - GET Request performed by inputting a postcode</summary>         
    <p>   
      
```
api.postcodes.io/postcodes/{:postcode}
```
  * The class will accept a postcode as an input and provide the option for the attributes to be printed as the result
  * The class has a .write_json_file method which can be instanciated to output a JSON file
  * Unit test to ensure the correct status code is being returned from the response of the API call.
    
    </p>
</details>

<details>
  <summary>POSTPostcodeParser - POST Request performed by inputting a payload of multiple postcodes </summary>         
    <p>   
      
```
api.postcodes.io/postcodes
```
```
{
  "postcodes" : ["postcode1", "postcode2", "postcode3"]
}
```
  * The class will accept a payload as an input and provide an option to get postcode details for an individual postcode through the postcode_details method
  * The class has a .write_json_file method which can be instanciated to output a JSON file for the whole payload
    
    </p>
</details>
