#!/usr/bin/env python3
"""The SWAPI -  consuming API and make request
"""

import requests 
import json

# Basic infos - base_url, endpoint, url, response
base_url = "https://swapi.dev/api"
endpoint = "people/1/" #This fetch info about Luke
url = f"{base_url}/{endpoint}"

response = requests.get(url)
# print(response.status_code)
# lets Handle the Response

if response.status_code == 200: 
    ''' Meaning if return OK'''
    data = response.json() #convert the res -> dict
    pretty_data = json.dumps(data, indent=4)
    print(pretty_data)

else:
    print(f"Request failed with error code: {response.status_code}")