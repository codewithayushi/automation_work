```python
import random # Import the random module for shuffling

# This script takes a word, keeps its first and last letters,
# but shuffles all the letters in between!

# Ask the user to enter a word
user_word = input("Enter a word to scramble (at least 3 letters): ")

# Check if the word is too short to scramble meaningfully
if len(user_word) < 3:
    print("That word is too short for this cool scramble!")
else:
    # Get the first letter of the word
    first_letter = user_word[0]

    # Get the last letter of the word
    last_letter = user_word[-1]

    # Get all the letters in between the first and last
    # Convert them to a list so we can shuffle them
    middle_letters = list(user_word[1:-1])

    # Shuffle the list of middle letters randomly
    random.shuffle(middle_letters)

    # Join the shuffled middle letters back into a single string
    shuffled_middle = "".join(middle_letters)

    # Combine the first letter, shuffled middle, and last letter
    scrambled_word = first_letter + shuffled_middle + last_letter

    # Display the original and the new scrambled word
    print(f"\nOriginal word: {user_word}")
    print(f"Scrambled word: {scrambled_word}")

# Try entering words like "python", "programming", or "hello"!
```
