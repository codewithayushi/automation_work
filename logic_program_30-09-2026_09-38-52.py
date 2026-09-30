```python
import random

# This script helps you find a simple moment of digital zen!

# Define a dictionary where keys are moods and values are lists of related affirmations/activities.
zen_options = {
    "calm": [
        "Take three deep breaths. Inhale peace, exhale stress.",
        "Observe a cloud for one minute (or imagine one).",
        "Listen to the quietest sound you can hear.",
        "Gently stretch your neck and shoulders."
    ],
    "focus": [
        "Pick one small task and commit to it for 10 minutes.",
        "Close your eyes and visualize a clear path forward.",
        "Write down three things you need to do, then prioritize one.",
        "Eliminate one distraction from your immediate environment."
    ],
    "joy": [
        "Recall a happy memory and savor it.",
        "Smile at yourself in a reflection.",
        "Think of one thing you are grateful for.",
        "Hum a favorite, cheerful tune."
    ]
}

# Define a list of "lucky" digital colors.
digital_colors = ["cyan", "magenta", "yellow", "lime green", "lavender", "peach"]

# --- Let's start the Zen experience! ---

# Ask the user for their name to personalize the message.
user_name = input("Hello, digital friend! What's your name? ")

# Inform the user about the available moods.
print("\nChoose your desired 'zen mood' for today:")
print("  - calm")
print("  - focus")
print("  - joy")

# Loop until the user provides a valid mood.
while True:
    chosen_mood = input("Type your choice (calm, focus, or joy): ").strip().lower() # .strip() removes whitespace, .lower() makes it case-insensitive
    if chosen_mood in zen_options:
        break # Exit the loop if the mood is valid
    else:
        print("Oops! That's not a valid mood. Please try again.")

# Select a random zen affirmation/activity based on the chosen mood.
selected_zen_activity = random.choice(zen_options[chosen_mood])

# Generate a random "digital fortune" number between 1 and 99.
digital_fortune_number = random.randint(1, 99)

# Pick a random "lucky digital color".
lucky_digital_color = random.choice(digital_colors)

# Print the personalized zen message using an f-string (formatted string literal).
print(f"\n✨ Greetings, {user_name}! For your '{chosen_mood}' mood today:")
print(f"--- Your Digital Zen Moment: {selected_zen_activity}")
print(f"--- Your Digital Fortune Number: {digital_fortune_number}")
print(f"--- Today's Lucky Digital Color: {lucky_digital_color}")

print("\nMay your digital journey be peaceful and inspiring!")
```
