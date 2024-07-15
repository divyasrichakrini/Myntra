import sqlite3

def add_collection(user_id, title, description):
    conn = sqlite3.connect('fashion_quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO collections (user_id, title, description)
    VALUES (?, ?, ?)
    ''', (user_id, title, description))
    conn.commit()
    conn.close()

def add_collection_item(collection_id, item_name, item_description):
    conn = sqlite3.connect('fashion_quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO collection_items (collection_id, item_name, item_description)
    VALUES (?, ?, ?)
    ''', (collection_id, item_name, item_description))
    conn.commit()
    conn.close()

def view_collections(user_id):
    conn = sqlite3.connect('fashion_quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id, title, description, date_created
    FROM collections
    WHERE user_id = ?
    ''', (user_id,))
    collections = cursor.fetchall()
    
    for collection in collections:
        print(f"\nCollection ID: {collection[0]}")
        print(f"Title: {collection[1]}")
        print(f"Description: {collection[2]}")
        print(f"Date Created: {collection[3]}")
        print("Items:")
        cursor.execute('''
        SELECT item_name, item_description
        FROM collection_items
        WHERE collection_id = ?
        ''', (collection[0],))
        items = cursor.fetchall()
        for item in items:
            print(f"  - {item[0]}: {item[1]}")
    
    conn.close()

def delete_collection(collection_id):
    conn = sqlite3.connect('fashion_quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM collection_items
    WHERE collection_id = ?
    ''', (collection_id,))
    cursor.execute('''
    DELETE FROM collections
    WHERE id = ?
    ''', (collection_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    user_id = 1  # Replace with the actual user ID

    while True:
        print("\n1. Add Collection")
        print("2. Add Collection Item")
        print("3. View Collections")
        print("4. Delete Collection")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            title = input("Enter collection title: ").strip()
            description = input("Enter collection description: ").strip()
            add_collection(user_id, title, description)
            print("Collection added successfully.")
        elif choice == '2':
            collection_id = int(input("Enter collection ID: ").strip())
            item_name = input("Enter item name: ").strip()
            item_description = input("Enter item description: ").strip()
            add_collection_item(collection_id, item_name, item_description)
            print("Item added to collection successfully.")
        elif choice == '3':
            view_collections(user_id)
        elif choice == '4':
            collection_id = int(input("Enter collection ID to delete: ").strip())
            delete_collection(collection_id)
            print("Collection deleted successfully.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
