```python
# This script creates a simple "Word Scrambler"!
# It takes a word from you and shows you a new word made from its letters.

import random # We need the 'random' module to shuffle the letters.

# Ask the user to type a word.
# The input() function gets text from the user.
original_word = input("Enter a word (no spaces please): ")

# Convert the word into a list of its individual letters.
# This is necessary because strings in Python cannot be easily shuffled directly.
letters = list(original_word)

# Use the random.shuffle() function to mix up the letters in the list.
# This changes the order of items *in place* within the 'letters' list.
random.shuffle(letters)

# Join the shuffled letters back together to form a new string (the scrambled word).
# The .join() method puts the elements of an iterable (like our list) together
# with the string it's called on as a separator (here, an empty string).
scrambled_word = "".join(letters)

# Print the original word and the newly scrambled word.
print(f"\nYour original word: {original_word}")
print(f"Your scrambled word: {scrambled_word}")

# Try running it multiple times with the same word to see different scrambles!
```
