```python
# This script generates a unique, fun username based on your favorite animal and number!

import random # We need the 'random' module to pick a random adjective.

# Ask the user for their favorite animal
animal = input("What's your favorite animal? ").strip().lower() # .strip() removes spaces, .lower() makes it lowercase

# Ask for their lucky number
try:
    number = int(input("What's your lucky number? ")) # Convert the input string to an integer
except ValueError:
    print("That's not a valid number. Using 777 instead.")
    number = 777 # Default if user enters non-numeric input

# Create a list of cool adjectives
adjectives = ["swift", "cosmic", "sparkling", "mystic", "golden", "silent", "brave", "ancient", "vibrant"]

# Pick a random adjective from the list
chosen_adjective = random.choice(adjectives)

# Combine everything to create a unique username
# We'll use an f-string for easy formatting.
# The modulo operator (%) ensures the number is always positive if they entered a negative.
unique_username = f"{chosen_adjective}{animal.capitalize()}{abs(number % 1000)}"

# Print the newly generated username
print(f"\nYour unique username could be: {unique_username}")

# Try running it multiple times with different inputs!
```
