```python
# Import the 'random' module to make choices randomly
import random

# Define a list of possible characters to use in our unique pattern
pattern_symbols = ['*', '#', '@', '&', ' ', '.', '+', '-']

# Ask the user for a number to determine the size of the pattern
# The 'input()' function gets text, and 'int()' converts it to a whole number
grid_size = int(input("Enter a small number for pattern size (e.g., 5-10): "))

# Print a clear separator line
print("\n--- Your Unique Pattern ---")

# Outer loop: This loop controls how many rows our pattern will have
# 'range(grid_size)' means it will repeat 'grid_size' times
for row_index in range(grid_size):
    # Initialize an empty string for the current row's characters
    current_row_string = ""

    # Inner loop: This loop controls how many symbols are in each row
    # It also repeats 'grid_size' times, creating a square grid
    for col_index in range(grid_size):
        # Use 'random.choice()' to pick a random symbol from our list
        chosen_symbol = random.choice(pattern_symbols)
        # Add the randomly chosen symbol to our current row string
        current_row_string = current_row_string + chosen_symbol

    # After the inner loop finishes (meaning the row is complete), print the row
    print(current_row_string)

# Print a final message after the entire pattern is generated
print("---------------------------\nPattern complete! Run again for a new one.")
```
