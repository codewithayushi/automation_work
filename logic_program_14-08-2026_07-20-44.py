```python
import random # This module helps us pick random things
import string # This module provides useful strings like all letters, digits, etc.

# --- Simple Random Acronym Generator ---
# This script asks for a sentence and creates a random "acronym" from it.

# Ask the user to type in a sentence
# The input() function gets text from the user
sentence = input("Type a sentence (e.g., 'Hello World Python'): ")

# Split the sentence into individual words
# The split() method breaks a string by spaces into a list of words
words = sentence.split()

# Check if there are any words to process
if not words:
    print("No words found in the sentence. Cannot generate acronym.")
else:
    # Initialize an empty list to store the characters for our acronym
    acronym_chars = []

    # Loop through each word in the list of words
    for word in words:
        # Check if the word is not empty
        if word:
            # Randomly pick a character from the current word
            # random.choice() picks one random item from a sequence (like a word)
            random_char = random.choice(word)
            # Add the chosen character (converted to uppercase) to our list
            acronym_chars.append(random_char.upper())

    # Join all the selected characters together to form the final acronym
    # The join() method concatenates items of an iterable with a separator (here, an empty string)
    random_acronym = "".join(acronym_chars)

    # Print the original sentence and the generated random acronym
    print("\nOriginal Sentence:", sentence)
    print("Your Random Acronym:", random_acronym)

```
