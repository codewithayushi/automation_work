# Import the 'random' module to choose items randomly.
import random

# A list of quirky, positive messages or "whimsical facts."
whimsy_messages = [
    "Your shoelaces are probably tied just right today!",
    "Somewhere, a squirrel is thinking about you fondly.",
    "You have the perfect amount of sparkle for a Tuesday!",
    "A tiny invisible unicorn just high-fived you.",
    "Your imagination is secretly powering a small cloud.",
    "Today is a great day for making a new discovery (even if it's just a dust bunny)."
]

# Get the user's name, making it optional.
# .strip() removes any accidental spaces at the start or end.
user_name = input("What's your name? (Press Enter if you prefer not to say) ").strip()

# Choose one random message from our list.
chosen_message = random.choice(whimsy_messages)

# Print a personalized greeting if a name was provided.
# This uses an 'f-string' for easy text formatting.
if user_name:
    print(f"\nHello, {user_name}!")
else:
    print("\nHello there, friend!")

# Print the chosen whimsical message.
print(chosen_message)

# A final playful closing message.
print("\nKeep being awesome!")
