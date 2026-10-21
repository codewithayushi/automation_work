```python
# Ask the user for a single character to use in the pattern.
pattern_char = input("Enter a single character for your pattern (e.g., *, #, @): ")

# Ask the user for the maximum width of the pattern.
# We convert the input to an integer because input() always returns a string.
try:
    max_width = int(input("Enter a small whole number for the maximum width (e.g., 5, 10): "))
    # Ensure the width is at least 1 for the pattern to display.
    if max_width < 1:
        max_width = 1
except ValueError:
    # If the user enters something that's not a number, set a default width.
    print("That wasn't a valid number. Defaulting max_width to 5.")
    max_width = 5

print("\n--- Your Expanding & Contracting Pattern ---")

# Loop to build up the pattern, line by line.
# 'range(1, max_width + 1)' generates numbers from 1 up to 'max_width'.
for current_length in range(1, max_width + 1):
    # Print the chosen character, repeated 'current_length' times.
    print(pattern_char * current_length)

# Loop to shrink the pattern back down.
# 'range(max_width - 1, 0, -1)' generates numbers from 'max_width - 1' down to 1.
# The '-1' step tells the range to count downwards.
for current_length in range(max_width - 1, 0, -1):
    # Print the chosen character, repeated 'current_length' times.
    print(pattern_char * current_length)

print("--- Pattern complete! ---")
```
