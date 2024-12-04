# Poupular package: not so limited to python
# Application programming interface
# It can have python files and functions
# Usually services, that we can talk to
# Most live on the internet
# Can write a code that pretends to be a browser
    # Connects to the 3rd-party service and dowloads data that we can incorporate in our program
# Popular package for doing so is request
    # Allows to make web requests
    # Can automate the retrievel of http/https
    # pypi.org/project/requests
#pip3 install requests --target /Users/tabishshahmohsin/desktop/pythoncs50/L4\ Libraries
# Apple has its own itune service:
# Eg: https://itunes.apple.com/search?entity=song&limit=1&term=weezer
    # Can manually construct this by using the documentatin for apple's API
    #search? identifies that we are seeking to search
    #entity=song implies that we are looking for a song(not an album/playlist)
    #limit=1 asks it to retrieve info about a single song.
    # term=weezer means pipoints the band
    # If we go to that website and open the file
        # The file is written in JavaScipt Object Notation(JSON)
        # Though it's related to JavaScript
        # Nowadays, it's used as a language agnostic format for data exchange
        # Formated using [],(),"",{},:, etc.
# We can write a code to pretend it to be a browser to get the same data
import requests
# In order to make the HTTP requests
import sys
# To use the command line arguments
# If wanted to search the specs instead of the artist
import json
# This lib comes with python
#To format json files, increasing their readibility
if len(sys.argv)!=2:
    sys.exit()  # Keeping it simple for now
response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json()) #python request library converts the json file reutrned by apple into a dictionary
# This is ugly and unreadable
print("\n"*7)
y=json.dumps(response.json(), indent=2)
print(y, "\n"*7)
print(response.json()["results"][0]["trackName"])
# indent will make easier to understand
# Usign dumps() for pretty printing
#dumping a string => dumps()
# You can try to understand the json file by this
    # Track the brackets
    # Then, backtrack it, and understand how to point to the required data



