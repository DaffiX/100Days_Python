#!/usr/bin/env python3
''' Fetch data from an API but get authorized first with API key
'''
import requests 

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# replace DEMO_KEY with your own key if generated 
api_key = "DEMO_KEY"
query_params = {"api_key":api_key, "earth_date":"2023-07-01"}

response = requests.get(endpoint, params = query_params)
print(response)

# use .json() => converts to dictionary so we can iterate 
response.json()
photos = response.json()["photos"]
print(f"Found {len(photos)} photos")

print(photos[5]["img_src"])
