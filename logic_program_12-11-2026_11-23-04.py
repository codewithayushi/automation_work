```python
# This script creates a simple "Word Scrambler" game for a beginner.
# It shuffles the letters of a word and challenges the user to guess the original word.

import random # We import the 'random' module to shuffle letters.

# Define the secret word for the game.
secret_word = "python"

# Convert the word into a list of its individual letters.
# This is necessary because strings in Python are immutable (cannot be changed directly).
letters = list(secret_word)

# Shuffle the order of the letters in the list.
random.shuffle(letters)

# Join the shuffled letters back into a single string to display the scrambled word.
scrambled_word = "".join(letters)

# Greet the user and show them the scrambled word.
print("Welcome to the Word Scrambler!")
print("Unscramble the following word to win:")
print(f"Scrambled word: {scrambled_word}") # f-strings are a great way to embed variables in strings!

# Ask the user for their guess.
user_guess = input("Your guess: ").lower() # .lower() converts input to lowercase for easier comparison.

# Check if the user's guess is correct.
if user_guess == secret_word:
    print("Congratulations! You guessed it!")
else:
    print(f"Sorry, that's incorrect. The correct word was '{secret_word}'.")

print("Thanks for playing!")
```
