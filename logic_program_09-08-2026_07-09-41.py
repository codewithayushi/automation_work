```python
# Import the 'random' module to enable random selections.
import random

# Define a list of fun, imaginative fortunes.
# Each item in the list is a string of text.
fortunes = [
    "A friendly cat will share its wisdom with you today.",
    "You will discover a secret passage behind a bookshelf.",
    "A tiny robot will thank you for being you.",
    "Your next snack will be surprisingly delicious.",
    "You'll find a forgotten coin in an old pocket.",
    "The clouds will form a shape just for you.",
    "A new, interesting thought will spark in your mind.",
    "You will hear your favorite song unexpectedly.",
    "Something beautiful will catch your eye today.",
    "A small act of kindness will brighten someone's day (maybe yours!)."
]

# Print a welcoming message for the user.
print("🔮 Welcome to the Whimsical Fortune Teller! 🔮")

# Use the 'random.choice()' function to pick one fortune from the list.
# The chosen fortune is stored in the 'my_fortune' variable.
my_fortune = random.choice(fortunes)

# Print the randomly selected fortune to the user.
print("\nYour unique fortune for today is:")
print(f"🌟 {my_fortune} 🌟")

# Print a closing message.
print("\nMay your day be filled with delightful surprises!")
```
