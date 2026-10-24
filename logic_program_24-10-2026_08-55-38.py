```python
# This script creates a 'mirror' pattern from a word you enter,
# showing how string slicing and loops can create visual effects.

# 1. Ask the user to enter a word
# The input() function gets text from the user.
user_word = input("Enter a word: ")

# 2. Get the length of the word
# The len() function tells us how many characters are in a string.
word_length = len(user_word)

# 3. Print the word character by character, building up
# This loop goes from 0 up to (but not including) word_length.
print("\n--- Building up ---")
for i in range(word_length):
    # Slice the word from the beginning (index 0) up to the current index (i+1).
    # This prints progressively longer parts of the word.
    print(user_word[0 : i + 1])

# 4. Print the word character by character, receding
# This loop goes from 1 up to (but not including) word_length.
print("\n--- Receding ---")
for i in range(1, word_length):
    # Slice the word from the current index (i) to the end.
    # This prints progressively shorter parts of the word, from the middle out.
    print(user_word[i : word_length])

# 5. Print the word character by character, building up in reverse
# This loop goes from (word_length - 1) down to 0, decrementing by 1 each time.
print("\n--- Building up (Reverse) ---")
for i in range(word_length - 1, -1, -1):
    # Slice the word from the current index (i) to the end.
    # This prints parts of the word starting from the end and moving left.
    print(user_word[i : word_length])

# 6. Print the word character by character, receding in reverse
# This loop goes from (word_length - 1) down to 0, decrementing by 1 each time.
print("\n--- Receding (Reverse) ---")
for i in range(word_length - 1, -1, -1):
    # Slice the word from the beginning (index 0) up to the current index (i+1).
    # This prints progressively shorter parts of the word from the start.
    print(user_word[0 : i + 1])
```
