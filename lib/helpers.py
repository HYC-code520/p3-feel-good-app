from .models.mood_model import log_mood_to_db, view_mood_history
from .models.motivational_model import get_random_quote
from .models.animal_story_model import get_random_animal_story

# General feeling options
GENERAL_FEELINGS = ["Good", "Bad", "Mixed", "Neutral"]

# Detailed emotion options
DETAILED_EMOTIONS = [
    "Admiration → Feeling impressed by someone or something.",
    "Adoration → Deep love or affection.",
    "Aesthetic Appreciation → Liking how something looks or feels.",
    "Amusement → Finding something funny or entertaining.",
    "Anger → Feeling mad or upset.",
    "Anxiety → Feeling nervous or worried.",
    "Awe → Feeling amazed or inspired.",
    "Awkwardness → Feeling uncomfortable or out of place.",
    "Boredom → Feeling uninterested or tired of something.",
    "Calmness → Feeling relaxed and peaceful.",
    "Confusion → Feeling unsure or puzzled.",
    "Craving → Strongly wanting something.",
    "Disgust → Feeling grossed out or repulsed.",
    "Empathic Pain → Feeling sad because someone else is hurting.",
    "Entrancement → Being totally focused or fascinated.",
    "Excitement → Feeling thrilled or very happy.",
    "Fear → Feeling scared or afraid.",
    "Horror → Extreme fear or shock.",
    "Interest → Wanting to learn more or pay attention.",
    "Joy → Feeling really happy.",
    "Nostalgia → Missing or remembering the past fondly.",
    "Relief → Feeling better after being worried or stressed.",
    "Romance → Feeling love or attraction.",
    "Sadness → Feeling unhappy or down.",
    "Satisfaction → Feeling pleased or content.",
    "Surprise → Feeling caught off guard, good or bad."
]

def log_mood():
    """Prompt the user to log their mood in detail and save it to the database."""
    try:
        # Step 1: Ask for general feeling
        print("\nHow are you feeling today?")
        for i, feeling in enumerate(GENERAL_FEELINGS, 1):
            print(f"{i}. {feeling}")
        
        general_choice = input("Choose a number (1-4): ").strip()
        while general_choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please choose a number between 1 and 4.")
            general_choice = input("Choose a number (1-4): ").strip()
        
        general_feeling = GENERAL_FEELINGS[int(general_choice) - 1]

        # Step 2: Ask for detailed emotions
        print("\nCan you tell me about it a little bit more? Choose from the following emotions:")
        for i, emotion in enumerate(DETAILED_EMOTIONS, 1):
            print(f"{i}. {emotion}")
        
        detailed_choices = input(
            "Choose one or more numbers (comma-separated, e.g., 1,5,9): "
        ).strip().split(",")
        detailed_emotions = []
        for choice in detailed_choices:
            if choice.isdigit() and 1 <= int(choice) <= len(DETAILED_EMOTIONS):
                detailed_emotions.append(DETAILED_EMOTIONS[int(choice) - 1].split(" →")[0])
        
        if not detailed_emotions:
            print("You didn't select any detailed emotions. Logging the general feeling only.")
        
        # Step 3: Ask for additional notes
        notes = input("Want to add any notes? (optional): ").strip()

        # Combine detailed emotions
        mood_description = f"{', '.join(detailed_emotions)}"
        log_mood_to_db(general_feeling, mood_description, notes)
        print("Your mood has been logged!")

    except Exception as e:
        print(f"An error occurred while logging your mood: {e}")


def view_moods():
    """Retrieve and display mood history."""
    try:
        mood_history = view_mood_history()
        if mood_history:
            print("\nYour Mood History:")
            for entry in mood_history:
                timestamp, mood, notes = entry
                notes_text = f" (Notes: {notes})" if notes else ""
                print(f"- {timestamp}: {mood}{notes_text}")
        else:
            print("No mood history found.")
    except Exception as e:
        print(f"An error occurred while retrieving mood history: {e}")

        
def get_quote():
    """Retrieve and display a motivational quote."""
    from .models.motivational_model import get_random_quote
    try:
        quote = get_random_quote()
        print("\nHere's something to brighten your day:")
        print(f"\"{quote}\"")
    except Exception as e:
        print(f"An error occurred while retrieving a quote: {e}")

def get_animal_story():
    """Retrieve and display an inspiring animal story."""
    from .models.animal_story_model import get_random_animal_story
    try:
        story = get_random_animal_story()
        print("\nInspiring Animal Story:")
        print(story)
    except Exception as e:
        print(f"An error occurred while retrieving an animal story: {e}")
