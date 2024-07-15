def welcome_message():
    print("Welcome to the Fashion Enthusiasts Community!")
    print("Here you can discuss fashion, share style tips, and stay updated with the latest trends.")
    print("Type 'exit' to leave the community.\n")

def main():
    welcome_message()
    while True:
        user_input = input("Share your thoughts or ask a question: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Thanks for visiting the Fashion Enthusiasts Community.")
            break
        else:
            print(f"User: {user_input}")
            print("Community: Thank you for sharing! Feel free to continue the discussion or ask more questions.\n")

if __name__ == "__main__":
    main()