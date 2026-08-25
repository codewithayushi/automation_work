```python
# A unique, short Python script for beginners!
# This script creates a simple, repeating visual pattern based on your input.

# Ask the user for a character to use in the pattern.
# This character will be repeated to form the lines.
pattern_symbol = input("Enter a single character (e.g., *, #, @): ")

# Ask the user for a small number to determine the pattern's size.
# This number controls how many rows the pattern will have.
pattern_rows_str = input("Enter a small whole number (e.g., 3, 5, 7): ")

# Convert the input string (pattern_rows_str) into an integer.
# We need it as a number to use in our loops.
pattern_rows = int(pattern_rows_str)

print("\nHere is your custom pattern:")

# Loop to create the first half of the pattern (growing lines).
# 'i' will go from 1 up to 'pattern_rows'.
for i in range(1, pattern_rows + 1):
    # Print the 'pattern_symbol' repeated 'i' times.
    # The .center() method helps align the pattern visually.
    print((pattern_symbol * i).center(pattern_rows * 2))

# Loop to create the second half of the pattern (shrinking lines).
# 'i' will go from 'pattern_rows - 1' down to 1.
for i in range(pattern_rows - 1, 0, -1):
    # Print the 'pattern_symbol' repeated 'i' times.
    print((pattern_symbol * i).center(pattern_rows * 2))

print("\nPattern complete! Hope you enjoyed creating it.")
```
