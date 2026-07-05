```python
# Script: Whimsical Word Mixer

# This script takes a word and shuffles its letters to create a fun, new word!
# It's a great way to learn about strings, lists, and the 'random' module.

# Import the 'random' module to help us shuffle the letters.
import random

# Ask the user to input a word.
# The input() function gets text from the user.
original_word = input("Enter a word (e.g., 'python', 'hello', 'sunshine'): ")

# Convert the word into a list of its individual characters.
# This makes it easy to shuffle them.
letters = list(original_word)

# Shuffle the order of the letters in the list randomly.
# The random.shuffle() function modifies the list in place.
random.shuffle(letters)

# Join the shuffled letters back together to form a new word.
# The .join() method creates a string from a list of characters.
mixed_word = "".join(letters)

# Print the original word and the new, mixed-up word.
# f-strings (formatted string literals) are a modern way to embed variables in strings.
print(f"\nYour original word was: '{original_word}'")
print(f"Your whimsical mixed word is: '{mixed_word}'")

# A little closing message.
print("\nHope you had fun mixing words!")
```
