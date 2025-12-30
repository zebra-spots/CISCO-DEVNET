# Imports
import requests
import urllib.parse

# Variables that will be sent in the request
route_url = "https://graphhopper.com/api/1/route?"
key = input("Enter API key: ") # User to input API key from https://graphhopper.com/dashboard/api-keys
#key = " " # Invalid key test string

# Create geocoding function
def geocoding (location, key):
    # prompt user to input location again if invalid
    while location == "":
        location = input("Enter the location again: ")
    
    # Variables for crafting URL and response statuses
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    
    # Because the keys state and country are not available for all locations 
    # the if statements are used to assign the desired strings for the variable new_loc 
    # and return the value assigned to new_loc
    # and if statement tests for a successful API request and the hits results is not empty.
    if json_status == 200 and len(json_data["hits"]) !=0:
        json_data = requests.get(url).json()
        lat=(json_data["hits"][0]["point"]["lat"])
        lng=(json_data["hits"][0]["point"]["lng"])
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""
        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        print("Geocoding API URL for " + new_loc + "(Location Type: " + value + ")\n" + url)

    else:
        lat="null"
        lng="null"
        new_loc=location
        if json_status != 200:
            print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])

    return json_status,lat,lng,new_loc

# Calling function, storing output and printing
while True:
    # User can choose vehicle profile
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Vehicle profiles available on Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("car, bike, foot")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    profile=["car", "bike", "foot"]
    vehicle = input("Enter a vehicle profile from the list above: ")
    print("\n")
    # Quit menu
    if vehicle == "quit" or vehicle == "q":
        break
    elif vehicle in profile:
        # Choose vehicle if it is in the list of vehicles
        vehicle = vehicle
    else:
        # Default to car
        vehicle = "car"
        print("No valid vehicle profile was entered. Using the car profile.")
    
    # User input for starting location
    loc1 = input("Starting Location: ")
    if loc1.lower() == "quit" or loc1.lower() == "q":
        break
    orig = geocoding(loc1, key)
    # User input for destination
    loc2 = input("Destination: ")
    if loc2.lower() == "quit" or loc2.lower() == "q":
        break
    dest = geocoding(loc2, key)

    print("===============================================")
    # if statement to check if the geocoding function returns a successful status for both locations
    if orig[0] == 200 and dest[0] == 200:
        # request the routing information for the Graphhopper Routing API and print out the URL for validation using JSONView
        op="&point="+str(orig[1])+"%2C"+str(orig[2])
        dp="&point="+str(dest[1])+"%2C"+str(dest[2])
        paths_url = route_url + urllib.parse.urlencode({"key":key, "vehicle":vehicle}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print("Routing API Status: " + str(paths_status) + "\nRouting API URL:\n" + paths_url)

    # Display trip summary information
    print("\n=================================================")
    print("Directions from " + orig[3] + " to " + dest[3] + " by " + vehicle) 
    print("=================================================\n")

    if paths_status == 200:
        # Convert trip summary to miles / km / hours / mins / seconds 
        miles = (paths_data["paths"][0]["distance"])/1000/1.61
        km = (paths_data["paths"][0]["distance"])/1000
        sec = int(paths_data["paths"][0]["time"]/1000%60)
        min = int(paths_data["paths"][0]["time"]/1000/60%60)
        hr = int(paths_data["paths"][0]["time"]/1000/60/60)

        # Display trip summary information
        print("Distance Traveled: {0:.1f} miles / {1:.1f} km".format(miles, km))
        print("Trip Duration: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
        print("=================================================")

        # for loop to iterate through the instructions JSON data
        for each in range(len(paths_data["paths"][0]["instructions"])):
            path = paths_data["paths"][0]["instructions"][each]["text"]
            distance = paths_data["paths"][0]["instructions"][each]["distance"]
            print("{0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000,
            distance/1000/1.61))
        print("=============================================")

    else:
        # Display error message
        print("Error message: " + paths_data["message"])
        print("***********************************************")