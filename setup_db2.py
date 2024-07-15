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

    # Sample questions
    sample_questions = [
        ("Who is known as the father of haute couture?", "A. Christian Dior", "B. Charles Frederick Worth", "B"),
        ("Which designer is famous for the wrap dress?", "A. Diane von Fürstenberg", "B. Vivienne Westwood", "A"),
        ("In which decade did the miniskirt become popular?", "A. 1950s", "B. 1960s", "B"),
        ("Which country is renowned for its traditional kimono?", "A. China", "B. Japan", "B"),
        ("Who is the designer behind the brand Off-White?", "A. Virgil Abloh", "B. Alexander Wang", "A"),
        ("Which iconic fashion designer is credited with popularizing the little black dress?", "A. Coco Chanel", "B. Elsa Schiaparelli", "A"),
        ("Which fabric is made from the fibers of the cocoon of the mulberry silkworm?", "A. Silk", "B. Cotton", "A"),
        ("The famous 'New Look' was created by which designer in 1947?", "A. Christian Dior", "B. Yves Saint Laurent", "A"),
        ("Which fashion movement in the 1960s was characterized by bold patterns and vibrant colors?", "A. Mod", "B. Bohemian", "A"),
        ("Which 1990s fashion trend involved wearing oversized flannel shirts?", "A. Grunge", "B. Hip-Hop", "A")
    ]

    # Insert sample questions into the database
    cursor.executemany('''
    INSERT INTO questions (question, option_a, option_b, answer)
    VALUES (?, ?, ?, ?)
    ''', sample_questions)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
