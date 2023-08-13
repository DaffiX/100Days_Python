#!/usr/bin/env python3
"""some endpoint in SWAPI support pagination. The response will contain `next` field if more data available. USE LOOP to fetch all data
"""
import requests 

base_url = "https://swapi.dev/api"
endpoint = "people/"
url = f"{base_url}/{endpoint}"

while url:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        for character in data["results"]: # swapi keyword
            print(character["name"])

        url = data["next"] # move to next page of result
        #visualize the pagination 
        print(f"Fetched data from : {url}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        break