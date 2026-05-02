```python
# This script checks if a word or phrase is a palindrome.
# A palindrome reads the same forwards and backwards.

# Get input from the user.
user_input = input("Enter a word or phrase: ")

# Clean the input:
# 1. Remove all spaces.
# 2. Convert everything to lowercase to ignore case.
cleaned_input = user_input.replace(" ", "").lower()

# Reverse the cleaned input string using slicing.
# [start:end:step] - a step of -1 reverses the string.
reversed_input = cleaned_input[::-1]

# Compare the cleaned original string with its reversed version.
if cleaned_input == reversed_input:
    # If they are the same, it's a palindrome.
    print(f"'{user_input}' IS a palindrome!")
else:
    # Otherwise, it's not a palindrome.
    print(f"'{user_input}' IS NOT a palindrome.")
```
