#!/usr/bin/env python3

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    page = int(request.args.get('page', 1))
    base_url = "https://swapi.dev/api"
    endpoint = "people/"
    url = f"{base_url}/{endpoint}?page={page}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        characters = data["results"]
        total_pages = data["count"] // len(characters) + 1
        # print(characters)  # Print characters to check the data
    else:
        return f"Request failed with status code: {response.status_code}"

    return render_template('index.html', characters=characters, page=page, total_pages=total_pages)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0')