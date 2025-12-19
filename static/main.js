const breedSelect = document.getElementById('breeds');
const showCatBtn = document.getElementById('show-cat-btn');
const img = document.getElementById('cat-image');
const msg = document.getElementById('no-image-msg');

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
            return;
        }

        const image = data[0];
        img.src = image.url;

        img.onload = () => {
            msg.style.display = 'none';
            img.style.display = 'block';
        }

    } catch (error) {
        msg.textContent = 'Error fetching image.';
        msg.style.display = 'block';
        console.error(error);
    }
}