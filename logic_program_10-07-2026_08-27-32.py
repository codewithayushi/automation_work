```python
# This script creates a simple "Word Scrambler" to play with text!

# First, we ask the user to type in a word or phrase.
# The 'input()' function waits for the user to type and press Enter.
user_input = input("Type a word or short phrase: ")

# Let's print the original input back to the user.
print(f"\nYou typed: '{user_input}'")

# Now, let's make it yell! The '.upper()' method converts all letters to uppercase.
print(f"In ALL CAPS: '{user_input.upper()}'")

# How about whispering? The '.lower()' method converts all letters to lowercase.
print(f"In all lowercase: '{user_input.lower()}'")

# A fun trick: reversing the string!
# [::-1] is a special way to create a reversed copy of a string or list.
print(f"Backwards: '{user_input[::-1]}'")

# Finally, let's count how many characters (letters, spaces, etc.) are in the input.
# The 'len()' function tells us the length of a string or other sequence.
print(f"Your input has {len(user_input)} characters.")

# This is the end of our little word game!
```
