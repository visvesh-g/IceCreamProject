document.addEventListener('DOMContentLoaded', function() {
    const cartItemsList = document.getElementById('cartList');

    // Populate cart items from localStorage when the page loads
    populateCartItems();

    // Function to populate cart items
    function populateCartItems() {
        cartItemsList.innerHTML = ''; // Clear previous cart items
        const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
        cartItems.forEach((flavorName, index) => {
            const listItem = document.createElement('li');
            listItem.textContent = flavorName;

            // Create a remove button (cross icon)
            const removeButton = document.createElement('button');
            removeButton.innerHTML = '&#10006;'; // Cross icon
            removeButton.classList.add('removeButton');
            removeButton.addEventListener('click', function() {
                removeFromCart(index); // Pass index of clicked item to removeFromCart function
                populateCartItems(); // Refresh cart display after removal
            });

            // Append remove button to list item
            listItem.appendChild(removeButton);

            // Append list item to cart items list
            cartItemsList.appendChild(listItem);
        });
    }

    // Function to remove item from cart and localStorage
    function removeFromCart(index) {
        let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
        cartItems.splice(index, 1); // Remove item at given index
        localStorage.setItem('cartItems', JSON.stringify(cartItems)); // Update localStorage
    }
});
