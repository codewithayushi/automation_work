# This unique script creates a simple, customizable text art star using a character and size you choose!

# --- Part 1: Get user input ---

# Ask the user for a single character to build the star with.
# The input() function gets text from the user.
# We store the user's input in the 'star_character' variable.
star_character = input("Enter a single character to build your star (e.g., '*', '#', '@'): ")

# Ask the user for a size for the star.
# We use int() to convert the input text into a whole number (integer),
# because we will use this number for counting in loops.
# A small number like 3, 4, or 5 works best for a simple star shape.
star_size = int(input("Enter a small number for the star's size (e.g., 3, 4, 5): "))

# --- Part 2: Print the top half of the star (including the widest row) ---

# This 'for' loop iterates from 1 up to 'star_size'.
# In each iteration, 'i' will represent the current row number, helping us
# decide how many spaces and characters to print.
for i in range(1, star_size + 1):
    # Calculate the number of leading spaces for the current row.
    # As 'i' increases (we go down the star), the number of spaces decreases.
    # For a 'star_size' of 3:
    # i=1 -> 2 spaces
    # i=2 -> 1 space
    # i=3 -> 0 spaces
    spaces = " " * (star_size - i)
    
    # Calculate the number of star characters for the current row.
    # The number of characters increases by 2 each row (1, 3, 5, etc.).
    # The formula (2 * i - 1) gives us these odd numbers.
    # For a 'star_size' of 3:
    # i=1 -> 1 character
    # i=2 -> 3 characters
    # i=3 -> 5 characters
    characters = star_character * (2 * i - 1)
    
    # Print the full row: first the spaces, then the characters.
    print(spaces + characters)

# --- Part 3: Print the bottom half of the star (excluding the widest row, which is already printed) ---

# This 'for' loop iterates downwards, from 'star_size - 1' down to 1.
# It uses three arguments: range(start, stop, step).
# 'star_size - 1' is the starting row (e.g., if size is 3, start at 2).
# '0' is the stop point (exclusive, so it stops before 0, meaning it includes 1).
# '-1' is the step, meaning it counts down.
for i in range(star_size - 1, 0, -1):
    # Calculate the number of leading spaces for the current row.
    # As 'i' decreases (we go down the star's bottom half), the number of spaces increases.
    # This logic is the same as the top half, ensuring symmetry.
    spaces = " " * (star_size - i)
    
    # Calculate the number of star characters for the current row.
    # This logic is also the same as the top half, ensuring symmetry.
    characters = star_character * (2 * i - 1)
    
    # Print the full row.
    print(spaces + characters)

# --- End of script ---
# You can try running this again with different characters and sizes!
# What if you tried a different character like 'o' or '$' and a size of 4?
