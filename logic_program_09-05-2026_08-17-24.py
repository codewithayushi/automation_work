```python
# A tiny script to generate a random "mood message" for your day!

import random

# List of positive and encouraging messages
mood_messages = [
    "Today is a great day to learn something new!",
    "Believe in yourself and all that you are.",
    "Your potential is endless. Keep going!",
    "A journey of a thousand miles begins with a single step.",
    "Spread kindness like confetti today!",
    "Embrace the challenges, they make you stronger.",
    "You are capable of amazing things.",
    "Don't forget to smile!"
]

# Ask the user for their name to personalize the message
user_name = input("Hello there! What's your name? ")

# Choose a random message from our list
daily_message = random.choice(mood_messages)

# Print a personalized message to the console
print(f"\nHey {user_name}! Here's a thought for your day:")
print(f"✨ {daily_message} ✨")

# A little reminder at the end
print("\nHave a fantastic day!")
```
