import requests
import sys
import json

if len(sys.argv) != 3:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

v = response.json()

for c in v ["results"]:
    print(c['artistName'], c['collectionName'], c['trackName'])