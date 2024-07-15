import sqlite3

def setup_database():
    # Connect to SQLite database (it will create the database if it doesn't exist)
    conn = sqlite3.connect('fashion_quiz.db')
    cursor = conn.cursor()

    # Create a table for storing quiz questions
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        answer TEXT NOT NULL,
        date_added DATE DEFAULT (DATE('now'))
    )
    ''')

    # Create a table for storing user collections
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS collections (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        date_created DATE DEFAULT (DATE('now'))
    )
    ''')

    # Create a table for storing collection items
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS collection_items (
        id INTEGER PRIMARY KEY,
        collection_id INTEGER NOT NULL,
        item_name TEXT NOT NULL,
        item_description TEXT,
        FOREIGN KEY (collection_id) REFERENCES collections (id)
    )
    ''')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
