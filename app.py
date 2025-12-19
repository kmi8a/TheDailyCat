from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import requests
import os
import sys
import random

ENV_FILE = '.env'

# Load environment variables from .env file
load_dotenv()
CAT_API = os.getenv('CAT_KEY')

if not CAT_API:
    print('CAT_KEY is not set in your environment. Please create a .env file with your API key.')
    sys.exit(1)


app = Flask(__name__)


# Homepage
@app.route('/')
def home():

    url='https://api.thecatapi.com/v1/breeds'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        breeds = response.json()

        return render_template('index.html', breeds=breeds)
    
    except Exception:
        return render_template('index.html', breeds=[])


# Shows favorite images
@app.route('/favs')
def favs():

    url = 'https://api.thecatapi.com/v1/favourites'
    headers = {'x-api-key': CAT_API}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        response = response.json()

        images = [x['image']['url'] for x in response]
        random.shuffle(images)

        return render_template('favs.html', images=images, error=None)
    
    except Exception:
        return render_template('favs.html', images=[], error="Unable to load favourites from The Cat API")


# Gets a random image for the selected breed
@app.route('/<breed_id>')
def get_random_image(breed_id):
    url = f'https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}'
    headers = {'x-api-key': CAT_API}

    response = requests.get(url, headers=headers)

    return jsonify(response.json())


# Add to favourites
@app.route('/add_favourite', methods=['POST'])
def add_favourite():
    data = request.get_json()
    image_id = data.get('image_id')

    url = 'https://api.thecatapi.com/v1/favourites'
    headers = {'x-api-key': CAT_API}
    payload = {'image_id': image_id}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        response.raise_for_status()

        return jsonify(response.json())
    except Exception:
        return jsonify({})


# Remove favourite
@app.route('/remove_favourite/<fav_id>', methods=['DELETE'])
def remove_favourite(fav_id):
    url = f'https://api.thecatapi.com/v1/favourites/{fav_id}'
    headers = {'x-api-key': CAT_API}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()

        return jsonify({'deleted': True})
    except Exception:
        return jsonify({})


if __name__ == '__main__':
    app.run(debug=True)