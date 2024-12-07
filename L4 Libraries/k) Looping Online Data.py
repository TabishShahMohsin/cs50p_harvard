import sys
import requests

if len(sys.argv)!=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])
# Gets the json file from the web and stores it in response
o=response.json()
# Converts the json file to a dictionary
print(o["results"][0]["trackName"])
# Checking the hirerchy
for something in o["results"]:
    #iterates through o["results"][i]
    print(something["trackName"])
    #prints o["results"][i]["trackName"]