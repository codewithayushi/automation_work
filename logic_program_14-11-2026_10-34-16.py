```python
import random # Import the 'random' module to pick a random item

# Define a list of simple, daily "micro-challenges" or positive prompts
daily_prompts = [
    "Notice three beautiful things around you today.",
    "Send a short, positive message to a friend.",
    "Learn one new word and try to use it.",
    "Take a 5-minute break to simply breathe and relax.",
    "Drink an extra glass of water.",
    "Do one small act of kindness for someone.",
    "Write down one thing you're grateful for.",
    "Try a new healthy snack.",
    "Stretch for two minutes."
]

# Randomly select one prompt from the list
chosen_prompt = random.choice(daily_prompts)

# Print a friendly message and the selected prompt to the console
print("✨ Your Daily Micro-Challenge! ✨")
print("-----------------------------------")
print(f"Today, try to: {chosen_prompt}")
print("-----------------------------------")
print("Have a wonderful day!")

# This script gives you a small, positive task each time you run it.
```
