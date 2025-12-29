# Import the json and yaml libraries
import json
import yaml

# use the json.load method to load the JSON file into a string set to the variable name ourjson
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

#print(ourjson)

# Add print statements that display the token value and how many seconds until the token expire
#print("The access token is: {}".format(ourjson['access_token']))
#print("The token expires in: {}".format(ourjson['expires_in']))

# Output the parsed JSON data in a YAML data format
print("\n\n---")
print(yaml.dump(ourjson))
