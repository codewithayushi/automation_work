```python
# This is a fun, short script to create a custom "banner" for any word!
# It's a great way to see how Python handles text and user input.

# 1. Get input from the user.
# The 'input()' function displays a message and waits for the user to type something
# and press Enter. Whatever they type is stored as a string in our variables.

# Ask the user for the word they want to put in the banner.
user_word = input("Enter a word or short phrase for your banner: ")

# Ask the user for a single character to use as the banner's border.
# Examples: '*', '#', '=', '@'
border_char = input("Enter a single character to use for the banner's border (e.g., *, #): ")

# A small check to make sure the border character is actually a single character.
# If not, we'll just use a default asterisk '*' for simplicity.
if len(border_char) != 1:
    print("Oops! You entered more than one character for the border. Using '*' by default.")
    border_char = "*"

# 2. Calculate banner dimensions.
# We need to know how long the user's word is to make the banner borders fit.
# The 'len()' function tells us the number of characters in a string.
word_length = len(user_word)

# The total width of our banner will be:
# 1 (left border character) + 1 (space) + word_length + 1 (space) + 1 (right border character)
# So, total_width = word_length + 4
banner_width = word_length + 4

# 3. Print the banner!
# The 'print()' function displays text on the console.

# Print the top border line.
# We use string multiplication (e.g., '*' * 5 results in '*****') to create a line
# of our chosen border character, repeated 'banner_width' times.
print(border_char * banner_width)

# Print the middle line, which contains the user's word.
# An f-string (formatted string literal) is a convenient way to embed variables
# directly into a string. We put the border character, a space, the user's word,
# another space, and then the border character again.
print(f"{border_char} {user_word} {border_char}")

# Print the bottom border line (which is identical to the top border).
print(border_char * banner_width)

# A friendly message to show the script has finished!
print("\nEnjoy your custom banner! 🎉")
```
