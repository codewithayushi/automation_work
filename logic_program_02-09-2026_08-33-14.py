```python
# This script is a fun "Word Scramble Generator" for beginners!

# 1. Get a word from the user.
# The 'input()' function lets the user type something into the console.
# Whatever they type is stored as text (a 'string') in the 'user_word' variable.
user_word = input("Enter your favorite word: ")

# 2. Get a 'secret number' from the user.
# We use 'int()' to convert the user's input (which is text) into a whole number.
# This number will be used to make our scramble unique.
secret_number = int(input("Enter a secret number (e.g., your lucky number): "))

# --- Let's start scrambling and revealing some word magic! ---

# 3. Find the length of the word.
# The 'len()' function tells us how many characters are in a string.
word_length = len(user_word)
print(f"\nYour word '{user_word}' has {word_length} letters.")

# 4. Create a "reversed version" of the word.
# The `[::-1]` is a clever Python trick to reverse any sequence, like a string!
reversed_word = user_word[::-1]
print(f"Your word spelled backward is: {reversed_word}")

# 5. Extract a 'mystery letter' from your word based on your secret number.
# We use the modulo operator (%) to ensure the 'secret_index' always stays within
# the valid range of your word's length. This prevents errors if the secret_number is too big.
# For example, if word_length is 5 and secret_number is 7, then 7 % 5 is 2.
# So, it will pick the character at index 2 (the third letter).
secret_index = secret_number % word_length
mystery_letter = user_word[secret_index]
print(f"Your 'mystery letter' from the word (based on your secret number) is: '{mystery_letter}'")

# 6. Generate a simple "Scramble Code" using parts of your word.
# This combines the first letter, the mystery letter, and the last letter of the original word.
# We also make the first letter uppercase using '.upper()' just for fun!
scramble_code = user_word[0].upper() + mystery_letter + user_word[word_length - 1]
print(f"Your unique 'Scramble Code' is: {scramble_code}")

# --- Run this script multiple times with different words and numbers to see different results! ---
```
