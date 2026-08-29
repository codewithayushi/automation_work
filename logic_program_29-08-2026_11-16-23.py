```python
# This script creates a simple "Word Scrambler" game!
# It will take a word from you and jumble its letters.

import random # We need the 'random' module to shuffle letters

# Get a word from the user
# input() reads text from the keyboard
# .strip() removes any extra spaces around the word
# .lower() converts the word to lowercase for consistency
original_word = input("Enter a word you'd like to scramble: ").strip().lower()

# Check if the user entered something
if not original_word: # If the string is empty
    print("Oops! You didn't enter a word. Let's try scrambling 'python' instead.")
    original_word = "python" # Provide a default word

# Convert the word into a list of its individual letters
# This is necessary because strings in Python are "immutable" (cannot be changed directly)
# but lists are "mutable" (can be changed, like shuffling)
letters = list(original_word)

# Shuffle the list of letters randomly
random.shuffle(letters)

# Join the shuffled letters back into a single string
# .join() is a string method that takes an iterable (like our list of letters)
# and concatenates its elements using the string it's called on as a separator.
# Here, an empty string "" means no separator.
scrambled_word = "".join(letters)

# Print the original and scrambled words
print(f"\nOriginal word: {original_word}")
print(f"Scrambled word: {scrambled_word}")

# A little challenge for the user!
print("\nCan you unscramble it back?")
```
