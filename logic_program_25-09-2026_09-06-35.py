```python
# This script creates a simple "Word Scrambler"!
# It takes a word from you and mixes up its letters randomly.

import random # We need the 'random' module to shuffle the letters.

print("--- Welcome to the Word Scrambler! ---")
print("I'll take your word and mix up its letters.")

# Ask the user to enter a word.
# The input() function waits for the user to type something and press Enter.
user_word = input("Please enter a word: ")

# Convert the word into a list of characters.
# For example, "hello" becomes ['h', 'e', 'l', 'l', 'o'].
letters = list(user_word)

# Shuffle the list of letters randomly.
# The random.shuffle() function modifies the list in place.
random.shuffle(letters)

# Join the shuffled letters back into a single string.
# The .join() method is used on a string (here, an empty string "")
# to combine elements of an iterable (our 'letters' list).
scrambled_word = "".join(letters)

# Print the original and the scrambled word.
# An f-string (formatted string literal) is used for easy embedding of variables.
print(f"\nYour original word: {user_word}")
print(f"Your scrambled word: {scrambled_word}")

print("\n--- Scrambling complete! ---")
```
