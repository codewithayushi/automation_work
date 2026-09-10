```python
# This script is a simple "Mystery Word Guesser" game!
# The computer thinks of a word, and you try to guess it letter by letter.

import random # We need the 'random' module to pick a word unpredictably.

# --- Configuration for the game ---

# A list of words the computer can choose from.
# You can add or remove words here! Make sure they are all lowercase.
WORDS = ["python", "apple", "banana", "coding", "mystery", "challenge", "begin", "script"]

# The maximum number of incorrect guesses allowed.
MAX_GUESSES = 6

# --- Game Logic Starts Here ---

# Function to choose a random word from our list.
def choose_random_word(word_list):
    """Picks a random word from the provided list."""
    return random.choice(word_list)

# Function to display the current state of the word (e.g., 'p _ t h _ n').
def display_word_progress(word, guessed_letters):
    """
    Creates a string showing the word with unguessed letters as underscores.
    Example: display_word_progress("apple", ['a', 'p']) would return "app_ _"
    """
    displayed = "" # Start with an empty string.
    for letter in word: # Go through each letter in the secret word.
        if letter in guessed_letters: # If this letter has been guessed...
            displayed += letter # ...add the letter to our display string.
        else: # If the letter has NOT been guessed...
            displayed += "_ " # ...add an underscore and a space instead.
    return displayed

# --- Main part of the game ---

print("Welcome to the Mystery Word Guesser!")
print(f"You have {MAX_GUESSES} chances to guess the word.")

# The computer chooses a secret word.
secret_word = choose_random_word(WORDS)

# We need to keep track of letters the user has guessed.
guessed_letters = [] # This is an empty list to store all unique guessed letters.

# We also need to count incorrect guesses.
incorrect_guesses_count = 0

# The main game loop! It continues until the user wins or runs out of guesses.
while incorrect_guesses_count < MAX_GUESSES:
    # Show the player their current progress.
    current_display = display_word_progress(secret_word, guessed_letters)
    print(f"\nWord: {current_display}")
    print(f"Guessed letters so far: {', '.join(sorted(guessed_letters))}") # Shows guessed letters, sorted alphabetically.
    print(f"Incorrect guesses left: {MAX_GUESSES - incorrect_guesses_count}")

    # Get a guess from the player.
    # .lower() converts input to lowercase to handle 'A' or 'a' the same.
    # .strip() removes any accidental spaces around the input.
    guess = input("Guess a letter: ").lower().strip()

    # --- Input Validation ---
    if not guess.isalpha(): # Check if the input is an alphabet character.
        print("Please enter a letter, not a number or symbol.")
        continue # Skip the rest of this loop iteration and ask again.

    if len(guess) != 1: # Check if the input is a single letter.
        print("Please guess only one letter at a time.")
        continue

    if guess in guessed_letters: # Check if this letter has already been guessed.
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue
    # --- End Input Validation ---

    # Add the valid new guess to our list of guessed letters.
    guessed_letters.append(guess)

    # Check if the guessed letter is in the secret word.
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses_count += 1 # Increment the incorrect guesses counter.

    # Check if the player has guessed all letters (won the game).
    # We create a set of letters from the secret word and check if all
    # those letters are present in our list of guessed letters.
    # A set is like a list, but it only stores unique items and is good for checking membership.
    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nCongratulations! You guessed the word: {secret_word}")
        break # Exit the loop because the game is won.

# After the loop ends, check if the player ran out of guesses.
else: # This 'else' block runs if the 'while' loop finishes normally (without a 'break').
    print("\nOh no! You ran out of guesses.")
    print(f"The secret word was: {secret_word}")
    print("Better luck next time!")

print("\nThanks for playing!")
```
