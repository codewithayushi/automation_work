```python
# This script creates a simple "character pyramid" based on user input.

# Get a single character from the user to build the pyramid.
pyramid_char = input("Enter a single character to build your pyramid: ")

# Get the desired height of the pyramid from the user.
# The 'int()' function converts the user's text input into a whole number.
try:
    pyramid_height = int(input("How tall should your pyramid be (e.g., 5-10)? "))
except ValueError:
    # Handle cases where the user doesn't enter a valid number.
    print("Invalid height. Please enter a whole number.")
    exit() # Exit the script if the input is bad.

# Ensure the height is positive for a meaningful pyramid.
if pyramid_height <= 0:
    print("Pyramid height must be a positive number.")
    exit()

# Loop through each row of the pyramid, starting from 1 up to the specified height.
# 'range(1, pyramid_height + 1)' generates numbers like 1, 2, 3, ..., up to 'pyramid_height'.
for current_row_number in range(1, pyramid_height + 1):
    # Calculate the number of spaces needed before the characters to center the row.
    # More spaces are needed for top rows, fewer for bottom rows.
    leading_spaces = " " * (pyramid_height - current_row_number)
    
    # Calculate the number of characters for the current row.
    # The pattern is 1 char for row 1, 3 for row 2, 5 for row 3, etc.
    # This is calculated as (current_row_number * 2 - 1).
    characters_in_row = pyramid_char * (current_row_number * 2 - 1)
    
    # Print the current row by combining the leading spaces and the characters.
    print(leading_spaces + characters_in_row)
```
