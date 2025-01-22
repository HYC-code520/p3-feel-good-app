from .models.mood_model import log_mood_to_db, view_mood_history
from .models.motivational_model import get_random_quote
from .models.animal_story_model import get_random_animal_story

def log_mood():
    """Prompt the user to log their mood and save it to the database."""
    try:
        mood = input("How are you feeling today? (e.g., happy, sad): ").strip()
        while not mood:
            print("Mood cannot be empty. Please try again.")
            mood = input("How are you feeling today? (e.g., happy, sad): ").strip()

        notes = input("Want to add any notes? (optional): ").strip()
        log_mood_to_db(mood, notes)
        print("Your mood has been logged!")
    except Exception as e:
        print(f"An error occurred while logging your mood: {e}")

def view_moods():
    """Retrieve and display the mood history from the database."""
    try:
        history = view_mood_history()
        if not history:
            print("No mood history found.")
        else:
            print("\nYour Mood History:")
            for record in history:
                print(f"- {record[0]}: {record[1]} ({record[2]})")
    except Exception as e:
        print(f"An error occurred while retrieving your mood history: {e}")

def get_quote():
    """Retrieve and display a random motivational quote."""
    try:
        print("\nHere's something to brighten your day:")
        print(get_random_quote())
    except Exception as e:
        print(f"An error occurred while retrieving a quote: {e}")

def get_animal_story():
    """Retrieve and display an inspiring animal story."""
    try:
        print("\nInspiring Animal Story:")
        print(get_random_animal_story())
    except Exception as e:
        print(f"An error occurred while retrieving an animal story: {e}")
