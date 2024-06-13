import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file} successfully")
    except sqlite3.Error as e:
        print(e)
    return conn

def insert_user(conn, name, allergens=None):
    """Insert a new user into the user table."""
    sql = 'INSERT INTO user (name, allergens) VALUES (?, ?)'
    cur = conn.cursor()
    cur.execute(sql, (name, allergens))
    conn.commit()
    return cur.lastrowid

def insert_ingredient(conn, name):
    """Insert a new ingredient into the ingredients table."""
    sql = 'INSERT INTO ingredients (name) VALUES (?)'
    cur = conn.cursor()
    cur.execute(sql, (name,))
    conn.commit()
    return cur.lastrowid

def insert_flavor(conn, name, ingredient_ids):
    """Insert a new flavor into the flavor table."""
    sql = 'INSERT INTO flavor (name, ingredient_ids) VALUES (?, ?)'
    cur = conn.cursor()
    cur.execute(sql, (name, ingredient_ids))
    conn.commit()
    return cur.lastrowid

def main():
    database = 'ice_cream_parlor.db'
    conn = create_connection(database)
    
    if conn is not None:

        # Insert users
        insert_user(conn, 'User', '') #User default Allergens

        # Insert ingredients
        insert_ingredient(conn, 'Peanuts')
        insert_ingredient(conn, 'Dairy')
        insert_ingredient(conn, 'Shellfish')
        insert_ingredient(conn, 'Butter')
        insert_ingredient(conn, 'Cream')
        # Insert flavors
        insert_flavor(conn, 'Chocolate Peanut Butter', '1,2')
        insert_flavor(conn, 'Mango Icecream', '5')

    if conn:
        conn.close()

if __name__ == '__main__':
    main()