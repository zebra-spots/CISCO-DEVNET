"""
The following program imports the json and yaml libraries, uses PyYAML to parse a YAML file, extract and
print data values, and output a JSON version of the file. It uses the yaml library safe_load() method to parse
the file stream and normal Python data references to extract values from the resulting Python data structure.
It then uses the json library dumps() function to serialize the Python data back out as JSON.
"""

# Import the json and yaml libraries
import json
import yaml

# Use the Python with statement to open myfile.yaml and set it to the variable name yaml_file. 
# Then use the yaml.safe_load method to load the YAML file into a string set to the variable name ouryaml
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

# Add a print statement for ouryaml to see that it is now a Python dictionary
#print(ouryaml)

# Add print statements that display the token value and how many seconds until the token expires.
#print("The access token is {}".format(ouryaml['access_token']))
#print("The token expires in {} seconds.".format(ouryaml['expires_in']))

# Add a print statement to add two blank lines after the previous output. 
print("\n\n")
# Add a statement to print ouryaml as JSON data by using the dumps() method of the json library
# Add the indent parameter to prettify the JSON data
print(json.dumps(ouryaml, indent=4))
