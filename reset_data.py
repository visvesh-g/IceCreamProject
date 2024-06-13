
6
import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def delete_all_data(conn, table_name):
    """Delete all data from a specified table."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
        print(f"All data deleted from {table_name}.")
    except sqlite3.Error as e:
        print(f"Error deleting data from {table_name}: {e}")

def main():
    database = 'ice_cream_parlor.db'
    conn = create_connection(database)
    
    if conn is not None:
        delete_all_data(conn, 'user')
        delete_all_data(conn, 'ingredients')
        delete_all_data(conn, 'flavor')
        
    if conn:
        conn.close()

if __name__ == '__main__':
    main()
