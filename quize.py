
import sqlite3
import random

def get_daily_questions():
    # Connect to SQLite database
    conn = sqlite3.connect('fashion_quiz.db')
    cursor = conn.cursor()
    
    # Retrieve 5 random questions from the database
    cursor.execute('''
    SELECT question, option_a, option_b, answer
    FROM questions
    ORDER BY RANDOM()
    LIMIT 5
    ''')
    questions = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return questions

def run_quiz(questions):
    score = 0
    
    for q in questions:
        question, option_a, option_b, answer = q
        print(question)
        print(f"A. {option_a}")
        print(f"B. {option_b}")
        user_answer = input("Enter the correct option (A or B): ").strip().upper()
        
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {answer}.")
        print()
    
    print(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    print("Welcome to the Fashion Quiz!")
    questions = get_daily_questions()
    run_quiz(questions)
