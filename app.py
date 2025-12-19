from flask import Flask, render_template, jsonify
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


if __name__ == '__main__':
    app.run(debug=True)