```python
# This script takes a word from the user,
# performs a series of simple string transformations,
# and then prints the "magical" result.

# Step 1: Ask the user for a word
# The input() function gets text from the user.
original_word = input("Enter a word to transform: ")

# Step 2: Reverse the word
# String slicing [::-1] creates a reversed copy of the string.
reversed_word = original_word[::-1]

# Step 3: Get the first character of the original word
# String indexing [0] gets the character at position 0 (the first one).
first_char = original_word[0]

# Step 4: Get the last character of the reversed word
# String indexing [-1] gets the character at the last position.
last_char_reversed = reversed_word[-1]

# Step 5: Repeat the first character a few times
# String multiplication (*) repeats a string.
repeated_first_char = first_char * 3

# Step 6: Combine parts to create a "magical" word
# String concatenation (+) joins strings together.
# We'll put the repeated first char, then the reversed word, then the last char of the reversed word.
magical_word = repeated_first_char + reversed_word + last_char_reversed

# Step 7: Print the original word and the transformed magical word
# f-strings (formatted string literals) make it easy to embed variables into strings.
print(f"\nYour original word was: '{original_word}'")
print(f"And your magical word is: '{magical_word}'")

# A little concluding message
print("\nTransformation complete! ✨")
```
