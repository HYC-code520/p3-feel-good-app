from .helpers import (
    log_mood,
    get_quote,
    get_animal_story
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            log_mood()  # Log your mood
        elif choice == "2":
            view_moods()  # View mood history
        elif choice == "3":
            get_quote()  # Get a motivational quote
        elif choice == "4":
            get_animal_story()  # Learn an inspiring animal story
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("\nWelcome to the Mood & Motivation Journal!")
    print("1. Log Your Mood")
    print("2. View Mood History")
    print("3. Get a Boost of Positivity")
    print("4. Learn an Inspiring Animal Story")
    print("0. Exit")

if __name__ == "__main__":
    main()
