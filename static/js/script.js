document.addEventListener('DOMContentLoaded', function() {
    const flavorList = document.getElementById('flavorList');
    const addButton = document.getElementById('addButton');
    const addInput = document.getElementById('add');

    // Add event listener for "Add to Cart" buttons
    flavorList.addEventListener('click', function(event) {
        if (event.target.classList.contains('addToCartButton')) {
            const listItem = event.target.parentNode;
            const flavorName = listItem.textContent.trim().replace('Add to Cart', '');
            console.log('Flavor added to cart:', flavorName);
            addToCart(flavorName); // Call function to add flavor to cart
        }
    });

    // Function to add flavor to cart and store in localStorage
    function addToCart(flavorName) {
        let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
        cartItems.push(flavorName); // Add flavor to cartItems array
        localStorage.setItem('cartItems', JSON.stringify(cartItems)); // Update localStorage
        alert(`${flavorName} added to cart`);
    }

    // Add event listener for "Add Item" button
    addButton.addEventListener('click', function() {
        const allergen = addInput.value.trim();
        if (allergen !== '') {
            // Send allergen to server
            fetch('/add_allergen', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ allergen: allergen })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Optionally update UI
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    // Add event listener for search input
    const flavorSearchInput = document.getElementById('flavorSearch');
    flavorSearchInput.addEventListener('input', function(event) {
        const searchTerm = event.target.value.trim().toLowerCase();
        const allFlavors = Array.from(flavorList.querySelectorAll('li'));

        allFlavors.forEach(flavor => {
            const flavorName = flavor.textContent.trim().toLowerCase();
            if (flavorName.includes(searchTerm)) {
                flavor.style.display = 'block';
            } else {
                flavor.style.display = 'none';
            }
        });
    });
});
