# Seasonal Flavors Ice Cream Parlor

Seasonal Flavors ice cream parlor is a simple application for managing an ice cream parlor's flavors and user allergies. The app allows users to search for ice cream flavors, add allergens, and highlight flavors that contain ingredients to which they are allergic. Users can also give suggestions, which will be worked on later by the system.

## Project Structure

### Main Application
- **app.py**: The main Flask application file that handles routing, database operations, and business logic.

### Database Setup
- **dbsetup.py**: Script for creating the database schema and tables.
- **initialise_data.py**: Script for inserting initial data into the database.
- **reset_data.py**: Script for deleting all data from the tables.

### Templates
- **templates/index.html**: The main page template that displays the list of flavors and handles user interactions.
- **templates/cart.html**: Template for the cart page.
- **templates/suggestions.html**: Template for the suggestions page.
- **templates/allergens.html**: Template for the allergens page.

### Static Files
- **static/style.css**: The main stylesheet for the application.
- **static/js/script.js**: JavaScript file that handles client-side interactions.
- **static/js/cart.js**: JavaScript file that handles added cart items by users.
- **static/js/suggestions.js**: JavaScript file that handles user suggestions.

## Features
1. **Flavor Search/Filter**: Allows users to search for flavors by name.
2. **Add Allergens**: Users can add allergens to their profile.
   - Note: After adding the allergens, refresh the page so that allergens get added for that particular flavor (highlighted in red).
3. **Highlight Allergic Flavors**: Flavors containing allergens are highlighted in red, while safe flavors are highlighted in green.
4. **User Management**: Manage user data, including allergens.
5. **Ingredient Management**: Manage ingredients and their association with flavors.
6. **Cart Management**: Add flavors to a cart for potential purchase.
7. **Suggestions**: Suggest new flavors to the parlor.

## Setup Instructions

### Requirements
- Python 3.x
- Flask
- SQLite3

### Database Initialization

1. **Create and Initialize Database**:
   - Run `dbsetup.py` to create the database file and initialize the necessary tables.

2. **Insert Initial Data**:
   - Run `initialise_data.py` to insert sample data into the tables to demonstrate the application's functionality.

3. **Reset Data**:
   - Run `reset_data.py` to delete all data from the tables.

### Running the Application

1. **Install Dependencies**:
   ```bash
   pip install flask
   ```
2. **Run the Flask App**:
   ```bash
   python app.py
   ```
3. **Open the Application**:
   - Open a web browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Contributing

Feel free to fork this project, submit issues and pull requests, or contribute in any way you see fit.

## License

This project is licensed under the MIT License.

## Unique Features

1. **Allergen Highlighting**: Flavors containing allergens are visually highlighted in red to alert users to potential allergens.
2. **User-Specific Allergens**: Users can add their allergens to their profile, allowing the application to personalize allergen alerts based on individual preferences.
3. **Dynamic Flavor List**: The flavor list dynamically updates based on user interactions, such as search/filter queries and allergen additions.
