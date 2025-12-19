const breedSelect = document.getElementById('breeds');
const showCatBtn = document.getElementById('show-cat-btn');
const img = document.getElementById('cat-image');
const msg = document.getElementById('no-image-msg');
const desc = document.getElementById('cat-description');
const favBtn = document.getElementById('fav-btn');

let currentImageId = null;
let isFavourite = null;
let currentFavouriteId = null;

// Passes Abyssinian breed id (First breed in the selector) to image loader
document.addEventListener('DOMContentLoaded', () => {
    const initialBreedId = breedSelect.value;
    loadCatImage(initialBreedId);
});

// If button clicked passes the selected breed id to the image loader
showCatBtn.addEventListener('click', () => {
    const breedId = breedSelect.value;
    loadCatImage(breedId);
});

// Loads an image accoridng to the breed selected
async function loadCatImage(breedId) {

    try {
        const response = await fetch(`/${breedId}`);
        const data = await response.json();

        if (data.length === 0) {
            currentImageId = null
            img.style.display = 'none';
            msg.textContent = 'No images found for this breed.';
            msg.style.display = 'block';
            desc.textContent = '';
            favBtn.classList.add('disabled')
            favBtn.disabled = true
            return;
        }

        const image = data[0];
        img.src = image.url;

        img.onload = () => {
            msg.style.display = 'none';
            img.style.display = 'block';
            // gets breed description if available
            if (desc) {
                desc.textContent = image['breeds'][0]['description'];
            }
        }

        // check if image is in favourites, and change the button accordingly
        currentImageId = image.id;
        isFavourite = 'favourite' in image;          
    
        favBtn.classList.remove('disabled')
        favBtn.disabled = false
        if (isFavourite) {
            currentFavouriteId = image.favourite;
            favBtn.textContent = '😭 Remove favourite';
        } else {
        currentFavouriteId = null;
        favBtn.textContent = '💙 Favourite';
        }


    } catch (error) {
        msg.textContent = 'Error fetching image.';
        msg.style.display = 'block';
        favBtn.classList.add('disabled')
        favBtn.disabled = true

        console.error(error);
    }
}


// Add favorite and remove favorite

favBtn.addEventListener('click', async () => {
    if (!currentImageId) {
        return;
    }

    if (!currentFavouriteId) {
        const res = await fetch('/add_favourite', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image_id: currentImageId })
        });
        const data = await res.json();
        currentFavouriteId = data.id;
        favBtn.textContent = '😭 Remove favourite';
    } else {
        await fetch(`/remove_favourite/${currentFavouriteId}`, { method: 'DELETE' });
        currentFavouriteId = null;
        favBtn.textContent = '💙 Favourite';
    }
});
