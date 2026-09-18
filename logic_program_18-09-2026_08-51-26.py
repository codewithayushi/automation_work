```python
import random

# This script generates a personalized, encouraging message.

# Ask the user for their name
user_name = input("Hello! What's your name? ")

# Define a list of positive adjectives
adjectives = ["awesome", "brilliant", "creative", "determined", "resilient", "kind"]

# Define a list of encouraging actions or qualities
actions = [
    "keep up the great work",
    "shine brightly today",
    "believe in yourself",
    "tackle your goals",
    "make a difference",
    "learn something new"
]

# Randomly select one adjective and one action from the lists
chosen_adjective = random.choice(adjectives)
chosen_action = random.choice(actions)

# Print a personalized encouragement message using an f-string
print(f"\nHey {user_name}, you are truly {chosen_adjective}!")
print(f"Remember to {chosen_action}!")
print("Have a fantastic day!")
```
