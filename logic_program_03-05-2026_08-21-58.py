```python
# This script creates a simple "Word Scramble Game" for a beginner.

import random # 'random' is a built-in Python module that helps us with random actions.

print("Welcome to the Super Scrambler Game!")
print("Unscramble the word to win!")

# Here we define a list of words. A list is an ordered collection of items.
words = ["python", "code", "challenge", "beginner", "script"]

# random.choice() picks one word randomly from our 'words' list.
chosen_word = random.choice(words)

# We convert the chosen word into a list of characters.
# Example: "python" becomes ['p', 'y', 't', 'h', 'o', 'n']
word_as_list = list(chosen_word)

# random.shuffle() shuffles the order of items directly within the list.
# Now, 'word_as_list' contains the scrambled letters.
random.shuffle(word_as_list)

# We join the shuffled letters back into a single string to display the scrambled word.
# Example: ['h', 'p', 'y', 'o', 't', 'n'] becomes "hpyotn"
scrambled_word = "".join(word_as_list)

print(f"\nYour scrambled word is: {scrambled_word}") # f-strings (formatted string literals) are a modern way to embed expressions inside string literals.

# We ask the user to guess the original word using the input() function.
# input() pauses the script and waits for the user to type something and press Enter.
user_guess = input("What do you think the original word was? ").lower() # .lower() converts the user's input to lowercase, making our comparison case-insensitive.

# We use an 'if-else' statement to check if the user's guess is correct.
if user_guess == chosen_word: # This compares the user's guess with the original word.
    print("Congratulations! You unscrambled it correctly!")
else: # If the condition in 'if' is False, the code in 'else' block is executed.
    print(f"Sorry, that's not quite right. The correct word was: {chosen_word}")

print("\nThanks for playing!")
```
