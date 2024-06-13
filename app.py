from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def create_connection():
    conn = sqlite3.connect('ice_cream_parlor.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_flavors():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, ingredient_ids FROM flavor")
    flavors = cursor.fetchall()
    
    # Get all ingredients
    cursor.execute("SELECT id, name FROM ingredients")
    ingredients = {row['id']: row['name'] for row in cursor.fetchall()}
    
    flavor_list = []
    for flavor in flavors:
        ingredient_ids = flavor['ingredient_ids'].split(',')
        flavor_ingredients = [ingredients[int(i)] for i in ingredient_ids]
        flavor_list.append({
            'name': flavor['name'],
            'ingredients': flavor_ingredients
        })
    
    conn.close()
    return flavor_list

def get_user_allergens():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT allergens FROM user")
    user_allergens = [allergen for row in cursor.fetchall() for allergen in row['allergens'].split(', ')]
    conn.close()
    return set(user_allergens)  # Return unique allergens

@app.route('/')
def home():
    flavors = get_flavors()
    user_allergens = get_user_allergens()
    
    # Mark each flavor as "allergic" or "suggested"
    for flavor in flavors:
        flavor_allergens = set(flavor['ingredients']).intersection(user_allergens)
        if flavor_allergens:
            flavor['status'] = 'allergic'
            flavor['allergens'] = list(flavor_allergens)
        else:
            flavor['status'] = 'suggested'
    
    return render_template('index.html', flavors=flavors)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')

@app.route('/add_allergen', methods=['POST'])
def add_allergen():
    allergen = request.json.get('allergen')
    if allergen:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT allergens FROM user")
        existing_allergens = [allergen for row in cursor.fetchall() for allergen in row['allergens'].split(', ')]
        
        if allergen not in existing_allergens:
            cursor.execute("INSERT INTO user (name, allergens) VALUES (?, ?)", ("default_user", allergen))
            conn.commit()
        conn.close()
        return jsonify({'message': 'Allergen added successfully'}), 200
    else:
        return jsonify({'error': 'Invalid allergen data'}), 400

@app.route('/allergens')
def allergens():
    allergen_list = get_user_allergens()
    return render_template('allergens.html', allergens=allergen_list)

if __name__ == '__main__':
    app.run(debug=True)
