```python
# This script tells you a simple "fortune" by picking a random message.

import random # We need the 'random' module to pick things randomly.

# This is a list of possible fortune messages.
fortunes = [
    "You will find happiness in unexpected places.",
    "A new opportunity awaits you soon.",
    "Be kind to others, and good things will follow.",
    "Your hard work will pay off.",
    "Today is a good day to learn something new.",
    "Adventure is just around the corner.",
    "Listen to your intuition."
]

print("Welcome to the Mystical Fortune Teller!") # Greet the user.

# Ask the user to press Enter to reveal their fortune.
# The script will pause here until the user presses Enter.
input("Press Enter to reveal your destiny...")

# Pick one fortune randomly from our list of fortunes.
your_fortune = random.choice(fortunes)

print("\n--- Your Fortune ---") # Print a decorative line for the output.
print(your_fortune) # Display the chosen fortune to the user.
print("--------------------") # Print another decorative line.
```
