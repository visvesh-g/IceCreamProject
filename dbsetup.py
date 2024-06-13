import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def create_tables(conn):
    """Create necessary tables if they don't exist."""
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        allergens TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flavor (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        ingredient_ids TEXT
    )''')

    conn.commit()

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
        create_tables(conn)

        # Insert users
        insert_user(conn, 'Alice', '')
        insert_user(conn, 'Bob', '')

        # Insert ingredients
        insert_ingredient(conn, 'Peanuts')
        insert_ingredient(conn, 'Dairy')
        insert_ingredient(conn, 'Shellfish')

        # Insert flavors
        insert_flavor(conn, 'Chocolate Peanut Butter', '1,2')
        insert_flavor(conn, 'Shrimp Alfredo', '3')

    if conn:
        conn.close()

if __name__ == '__main__':
    main()
