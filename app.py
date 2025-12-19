from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import requests
import os
import sys

ENV_FILE = '.env'

# Load environment variables from .env file
load_dotenv()
CAT_API = os.getenv('CAT_KEY')

if not CAT_API:
    print('CAT_KEY is not set in your environment. Please create a .env file with your API key.')
    sys.exit(1)


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(url='https://api.thecatapi.com/v1/breeds')
    breeds = response.json()
    return render_template('index.html', breeds=breeds)


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

    response = requests.post(url, json=payload, headers=headers)
    return jsonify(response.json())

# Remove favourite
@app.route('/remove_favourite/<fav_id>', methods=['DELETE'])
def remove_favourite(fav_id):
    url = f'https://api.thecatapi.com/v1/favourites/{fav_id}'
    headers = {'x-api-key': CAT_API}

    response = requests.delete(url, headers=headers)
    return jsonify({'deleted': True})


if __name__ == '__main__':
    app.run(debug=True)