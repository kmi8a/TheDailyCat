# THE DAILY CAT

### CODE THE DREAM pre-work assignment

## Description:

### A Flask web app that lets users browse cat breeds with a short description, view random images, and save their favorite cats using TheCatAPI.

### Features:

+ View cat breeds and fetch descriptions and random images per breed using the Breeds endpoint
+ Add/remove favorites using TheCatAPI Favourites endpoint
+ Dedicated “Favourites” page
+ Flask backend + JavaScript frontend
+ Environment variables for secure API keys

### Installation and setup:

1. Clone the repository (https://github.com/kmi8a/The-Daily-Cat.git)
2. Create a .env file in the project root (CAT_API=your_cat_api_key)
3. Install requirements (listed on requirements.txt)
4. Run the Flask app (python app.py)

### Project sctructure

```text
The-Daily-Cat/
│
├── app.py
├── requirements.txt
├── .env
├── static/
│   └── main.js
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── favs.html
│
└── README.md
```

### The key technologies and libraries utilized to implement the app include:

+ Python
+ Flask
+ JavaScript
+ Jinja
+ Bootstrap
+ HTML
+ CSS

## Using the App

To begin using the app, you need your own API key from the Cat API (https://thecatapi.com/), then follow the steps listed in "Installation and Setup". After launching, you will see a picture of an Abyssinian cat (the first breed in alphabetical order), a short description for the breed and a breed selector that lets you choose from all the breeds listed. Once you pick a breed, click the "Show me a cat!" button and a new picture and description corresponding to that breed will appear on the screen.

On every picture, there’s a button marked "💙 Favorite" that allows you to mark the current picture as a personal favorite. If a picture is already marked as a favorite, the button changes to a very sad "😭 Remove favourite" so you know you can remove it.

Lastly, there’s a separate page that shows all the pictures you’ve marked as favorites in a carousel, making it easy to scroll through and enjoy all your favorite cats.


