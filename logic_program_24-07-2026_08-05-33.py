```python
# This script creates a simple "Word Scramble" game for a single word.

import random # We'll use this to shuffle the letters of a word.

# Define the secret word for the game. Beginners can easily change this!
secret_word = "python" 
# Convert the word into a list of characters, so we can shuffle them.
word_letters = list(secret_word) 

random.shuffle(word_letters) # Mix up the letters randomly.

# Join the shuffled letters back together to form the scrambled word.
scrambled_word = "".join(word_letters)

print("--- Welcome to Word Scramble! ---")
print("Unscramble the following letters to reveal the secret word.")
print(f"Your scrambled word is: {scrambled_word}") # Display the scrambled word to the player.

# Get the player's guess.
player_guess = input("What is your guess? ").lower() # .lower() converts input to lowercase for easy comparison.

# Check if the player's guess is correct.
if player_guess == secret_word:
    print("Congratulations! You guessed it right!")
else:
    print(f"Oops! That's not correct. The secret word was '{secret_word}'.")

print("--- Game Over! ---")
```
