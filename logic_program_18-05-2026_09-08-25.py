```python
# This script generates a unique "text art" pattern based on user input.

# First, we ask the user for a single character to use in our pattern.
# The input() function reads text from the console.
pattern_char = input("Enter a single character for your pattern (e.g., *, #, @): ")

# Next, we ask for a number to determine the size/complexity of the pattern.
# We convert the input string to an integer using int() because we'll use it for counting.
pattern_size_str = input("Enter a small whole number (e.g., 3, 5, 7) for pattern size: ")

# Basic validation: ensure the user entered a digit.
# The while loop will keep asking until a valid number is entered.
while not pattern_size_str.isdigit():
    print("Oops! That wasn't a number. Please try again.")
    pattern_size_str = input("Enter a small whole number for pattern size: ")

pattern_size = int(pattern_size_str)

print("\nHere's your custom pattern:")

# This is the main loop that builds the top half of the pattern.
# The 'range(start, stop)' function generates numbers from 'start' up to (but not including) 'stop'.
# Here, 'i' will go from 0 up to 'pattern_size - 1'.
for i in range(pattern_size):
    # Calculate the number of leading spaces needed for the current row.
    # This creates the indent, making the pattern narrow at the top.
    num_spaces = i * 2

    # Calculate the number of characters for the current row.
    # The pattern starts wide and gets narrower.
    # (pattern_size - i) * 2 - 1 ensures we always have an odd number of characters.
    num_chars = (pattern_size - i) * 2 - 1

    # Construct the row string: spaces followed by the user's character repeated.
    # String multiplication (e.g., " " * 3) repeats the string.
    row_output = (" " * num_spaces) + (pattern_char * num_chars)

    # Print the constructed row.
    print(row_output)

# This loop builds the bottom half of the pattern, mirroring the top.
# We iterate 'j' from 1 up to 'pattern_size - 1'.
for j in range(1, pattern_size):
    # Calculate spaces for the bottom half; it mirrors the top's character count.
    # The number of spaces decreases as 'j' increases.
    num_spaces = (pattern_size - j - 1) * 2

    # Calculate characters for the bottom half; it mirrors the top's character count.
    # The number of characters increases as 'j' increases.
    num_chars = (j + 1) * 2 - 1

    # Construct and print the row for the bottom half.
    row_output = (" " * num_spaces) + (pattern_char * num_chars)
    print(row_output)

print("\nPattern generation complete!")
```
