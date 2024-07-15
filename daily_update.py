import sqlite3

def add_daily_question():
    # Connect to SQLite database
    conn = sqlite3.connect('fashion_quiz.db')
    cursor = conn.cursor()
    
    # New question to be added (you can change the question each day or fetch it from an API/file)
    new_question = (
        "Who designed the wedding dress for Kate Middleton?", 
        "A. Alexander McQueen", 
        "B. Stella McCartney", 
        "A"
    )
    
    # Insert the new question into the database
    cursor.execute('''
    INSERT INTO questions (question, option_a, option_b, answer)
    VALUES (?, ?, ?, ?)
    ''', new_question)
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_daily_question()
