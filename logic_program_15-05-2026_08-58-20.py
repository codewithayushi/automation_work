```python
# This script creates a simple, personalized "word art" based on your input!

# 1. Ask the user to enter a word they want to turn into art.
# The 'input()' function gets text from the user.
user_word = input("Enter a short word to decorate: ")

# 2. Ask the user for a simple character to use as a border.
border_char = input("Enter a single character for the border (e.g., #, *, -): ")

# 3. Get the length of the word.
# This helps us make the border line the correct size.
word_length = len(user_word)

# 4. Create the top and bottom border line.
# We multiply the border character by the word's length plus a little extra for padding.
border_line = border_char * (word_length + 4) # +4 adds 2 chars on each side

# 5. Print the word art!
# We use f-strings for easy and clear formatting.

# Print the top border.
print(border_line)

# Print the word itself, framed by the border character.
# The f-string places the border character, then a space, the word, another space, and the border character again.
print(f"{border_char} {user_word} {border_char}")

# Print the bottom border.
print(border_line)

# A friendly message to end the script.
print("Your unique word art is complete!")
```
