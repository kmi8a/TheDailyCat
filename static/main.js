const breedSelect = document.getElementById('breeds');
const showCatBtn = document.getElementById('show-cat-btn');
const img = document.getElementById('cat-image');

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

        const image = data[0];
        img.src = image.url;

        img.onload = () => {
            img.style.display = 'block';
        }

    } catch (error) {
        msg.textContent = 'Error fetching image.';
        msg.style.display = 'block';
        console.error(error);
    }
}