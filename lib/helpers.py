from colorama import init, Fore, Style
from .models.mood_model import log_mood_to_db, view_mood_history
from .models.motivational_model import get_random_quote_by_category
from .models.animal_story_model import get_random_animal_story_by_type

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



# Initialize colorama
init(autoreset=True)

first_ascii_art = Fore.CYAN + """
˚∧＿∧  　+        —̳͟͞͞💗
(  •‿• )つ  —̳͟͞͞ 💗         —̳͟͞͞💗 +
(つ　 <                —̳͟͞͞💗
｜　 _つ      +  —̳͟͞͞💗         —̳͟͞͞💗 ˚
`し´
"""+ Style.RESET_ALL

second_ascii_art = Fore.MAGENTA + """
┊        ┊       ┊       ♡        ┊
┊        ┊       ┊                ˚  ♡
┊        ┊       ♡       ⋆             +
♡    ⋆  ┊    .
     +     ♡
""" + Style.RESET_ALL

third_ascii_art = "\033[2m" + Fore.WHITE + """
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░  How are you   ░░█
█░░   Feeling?     ░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""" + Style.RESET_ALL

fourth_ascii_art = Fore.MAGENTA + """
⧣₊˚﹒✦₊  ⧣₊˚  𓂃★    ⸝⸝ ⧣₊˚﹒✦₊  ⧣₊˚
      /)    /)
    (｡•ㅅ•｡)〝₎₎ Intro template! ✦₊ ˊ˗ 
. .╭∪─∪────────── ✦ ⁺.
. .┊ ◟﹫ Name : 
. .┊﹒𐐪 Age : 
. .┊ꜝꜝ﹒Pronouns : 
. .┊ ⨳゛Sexuality : 
. .┊ ◟ヾ Likes : 
. .┊﹒𐐪 Dislikes : 
. .┊ ◟﹫ Extra : 
   ╰─────────────  ✦ ⁺.
⧣₊˚﹒✦₊  ⧣₊˚  𓂃★    ⸝⸝ ⧣₊˚﹒✦₊  ⧣₊˚
""" + Style.RESET_ALL

top_line_ascii_art = Fore.MAGENTA + """
⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢
﹉﹉﹉﹉﹉﹉୨♡୧﹉﹉﹉﹉﹉
""" + Style.RESET_ALL

long_line_ascii_art = Fore.WHITE+ """
★・・・・・・・★・・・・・・・・★・・・・・・・★・・・・・・・★
""" + Style.RESET_ALL


striaght_star_line_ascii_art = Fore.WHITE + """
★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★
""" + Style.RESET_ALL

heart_line_ascii_art = Fore.MAGENTA + """
꒰꒰・┄┄┄┄・♡・┄┄┄┄・꒱꒱
""" + Style.RESET_ALL


successful_log_text_box_ascii_art = Fore.GREEN + """
╔════════.·:·.❀ ✿ ❀.·:·.════════╗
✿   Your Mood Has Been Logged!  ✿
╚════════.·:·.❀ ✿ ❀.·:·.════════╝
""" + Style.RESET_ALL

emoji_heart_line_ascii_art = Fore.WHITE + """
⋆⛧*┈┈┈┈┈┈┈┈﹤୨ ❤️ ୧﹥ ┈┈┈┈┈┈┈┈*⛧⋆ 
""" + Style.RESET_ALL


def log_mood():
    print(third_ascii_art)
    """Prompt the user to log their mood in detail and save it to the database."""
    try:
        # Step 1: Ask for general feeling
        # print("\nHow are you feeling today?")
        for i, feeling in enumerate(GENERAL_FEELINGS, 1):
            print(f"{i}. {feeling}")
        
        general_choice = input("Choose a number (1-4): ").strip()
        while general_choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please choose a number between 1 and 4.")
            general_choice = input("Choose a number (1-4): ").strip()
        
        general_feeling = GENERAL_FEELINGS[int(general_choice) - 1]

        # Step 2: Ask for detailed emotions
        print(long_line_ascii_art)
        print("\n♡ Can you tell me a little bit more? Choose from the following emotions:")
        print(heart_line_ascii_art)
        for i, emotion in enumerate(DETAILED_EMOTIONS, 1):
            print(f"{i}. {emotion}")
        print(heart_line_ascii_art)
        
        detailed_choices = input(
            "♡ Choose one or more numbers (comma-separated, e.g., 1,5,9): "
        ).strip().split(",")
        detailed_emotions = []
        for choice in detailed_choices:
            if choice.isdigit() and 1 <= int(choice) <= len(DETAILED_EMOTIONS):
                detailed_emotions.append(DETAILED_EMOTIONS[int(choice) - 1].split(" →")[0])
        
        # Combine detailed emotions
        mood_description = ", ".join(detailed_emotions) if detailed_emotions else "None provided"

        # Step 3: Ask for additional notes
        print(long_line_ascii_art)
        notes = input("♡ Is there something on your mind or anything specific that’s making you feel this way? (optional): ").strip()

        # Step 4: Ask for positive reflections
        print(long_line_ascii_art)
        positive_reflection = input("♡ Did something positive happen today that you’d like to celebrate or reflect on? (optional): ").strip()
        
        # Append the positive reflection to notes
        if positive_reflection:
            notes += f" | Positive Reflection: {positive_reflection}" if notes else f"Positive Reflection: {positive_reflection}"

        # Log the mood into the database
        log_mood_to_db(general_feeling, mood_description, notes)
        print(successful_log_text_box_ascii_art)
        # print("Your mood has been logged!")

    except Exception as e:
        print(f"An error occurred while logging your mood: {e}")


def view_moods():
    """Retrieve and display mood history."""
    try:
        mood_history = view_mood_history()
        if mood_history:
            print("\nYour Mood History:")
            print(heart_line_ascii_art)
            for entry in mood_history:
                timestamp, mood, notes = entry
                notes_text = f" (Notes: {notes})" if notes else ""
                print(f"- {timestamp}: {mood}{notes_text}")
            print(heart_line_ascii_art)
        else:
            print("No mood history found.")

    except Exception as e:
        print(f"An error occurred while retrieving mood history: {e}")

        
def get_quote():
    """Prompt the user for a category and display a quote from that category."""
  
    # List of categories
    CATEGORIES = [
        "Calming",
        "Empathetic",
        "Encouraging",
        "General",
        "Gratitude-Inspired",
        "Hopeful",
        "Humorous",
        "Motivational",
        "Overcoming Challenges",
        "Reflective",
        "Self-Love",
        "Uplifting"
    ]
    
    try:
        # Step 1: Prompt the user for a category
        print(long_line_ascii_art)
        print("\n♡ What kind of inspiration do you need today?")
        print("\n♡ Choose from the list below to match your mood or boost your spirits!")
        print(heart_line_ascii_art)
        for i, category in enumerate(CATEGORIES, 1):
            print(f"{i}. {category}")
        print(heart_line_ascii_art)
        choice = input("Choose a number (1-12): ").strip()
        while not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
            print("Invalid choice. Please choose a valid number from the list.")
            choice = input("Choose a number (1-12): ").strip()
        
        selected_category = CATEGORIES[int(choice) - 1]
        
        # Step 2: Retrieve a quote from the selected category
        quote = get_random_quote_by_category(selected_category)
        print(striaght_star_line_ascii_art)
        print(f"\nHere's a {selected_category.lower()} quote to brighten your day:")
        print(first_ascii_art)
        
        print(f"\033[1;3;40;46m\"{quote}\"\033[0m")


        print(striaght_star_line_ascii_art)
    except Exception as e:
        print(f"An error occurred while retrieving a quote: {e}")


def get_animal_story():
    """Retrieve and display an inspiring animal story based on user's choice."""
    from .models.animal_story_model import get_random_animal_story_by_type

    # List of animals
    ANIMALS = [
        "ape", "bear", "butterfly", "camel", "cat", "cheetah", "cow", "dog", 
        "dolphin", "elephant", "lamb", "octopus", "otter", "penguin", "rat", "squirrel", "tiger"
    ]

    try:
        # Step 1: Prompt the user to select an animal
        print(long_line_ascii_art)
        print("\n♡ Which kind of animal's story would you like to hear? Choose from the list below:")
        print(heart_line_ascii_art)
        for i, animal in enumerate(ANIMALS, 1):
            print(f"{i}. {animal.capitalize()}")
        print(heart_line_ascii_art)
        choice = input("♡ Choose a number from the list: ").strip()
        while not choice.isdigit() or not (1 <= int(choice) <= len(ANIMALS)):
            print("Invalid choice. Please choose a valid number from the list.")
            choice = input("Choose a number from the list: ").strip()
        
        selected_animal = ANIMALS[int(choice) - 1]

        # Step 2: Retrieve a random story for the selected animal
        story = get_random_animal_story_by_type(selected_animal)
        if story:
            print(f"\nHere's an inspiring story about a {selected_animal}:")
            print(first_ascii_art)
            print(f"\033[1;3;40;46m\"{story}\"\033[0m")
        else:
            print(f"Sorry, we couldn't find any stories about {selected_animal}s right now. Try another!")

    except Exception as e:
        print(f"An error occurred while retrieving an animal story: {e}")
