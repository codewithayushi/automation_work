# This script creates a personalized, decorative text banner!
# It teaches input, string length, string multiplication, and f-strings.

# 1. Ask the user for their main message
# The input() function gets text from the user.
message = input("Enter a short message or your name: ")

# 2. Ask for a character to use as the border decoration
# This allows for some customization.
border_char = input("Enter a single character for the border (e.g., *, #, =): ")

# 3. Calculate the length needed for the border lines
# len() gets the number of characters in a string.
# We add 4 for: 2 spaces around the message, 2 border characters on the ends.
border_length = len(message) + 4

# 4. Print the top border line
# String multiplication repeats a character or string.
print(border_char * border_length)

# 5. Print the line containing the message itself
# An f-string (formatted string literal) is a clean way to combine variables and text.
# It places the border character, a space, the message, another space, and the border character.
print(f"{border_char} {message} {border_char}")

# 6. Print the bottom border line (same as the top one)
print(border_char * border_length)

# A final message to the user
print("\nYour custom banner is complete!")
