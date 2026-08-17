```python
# This script creates a unique expanding and contracting text pattern
# using a character and size chosen by the user.

# Get a single character from the user for the pattern.
# The input() function gets text from the user.
pattern_char = input("Enter a single character for your pattern (e.g., * or #): ")

# Get the maximum size for the pattern from the user.
# We use try-except to handle cases where the user might not enter a number.
try:
    max_size = int(input("Enter the maximum pattern size (e.g., 5 for a 5-line high pattern): "))
    # Ensure the size is at least 1, otherwise adjust it.
    if max_size < 1:
        print("Size must be at least 1. Setting size to 1.")
        max_size = 1
except ValueError:
    # If conversion to int fails (e.g., user types "hello"), print an error and exit.
    print("That's not a valid number for size! Please run the script again and enter a number.")
    exit() # This stops the script from running further.

print("\nHere is your unique pattern:")

# --- Part 1: Build the pattern upwards (expanding lines) ---
# The 'range(1, max_size + 1)' generates numbers from 1 up to max_size.
# For example, if max_size is 3, current_line_length will be 1, then 2, then 3.
for current_line_length in range(1, max_size + 1):
    # Print the pattern character repeated 'current_line_length' times.
    # String multiplication like 'char * 3' results in 'characharachar'.
    print(pattern_char * current_line_length)

# --- Part 2: Build the pattern downwards (contracting lines) ---
# The 'range(max_size - 1, 0, -1)' generates numbers from max_size - 1 down to 1.
# For example, if max_size is 3, current_line_length will be 2, then 1.
for current_line_length in range(max_size - 1, 0, -1):
    # Print the pattern character repeated 'current_line_length' times.
    print(pattern_char * current_line_length)

# A final message to indicate the script has finished.
print("\nPattern complete!")
```
