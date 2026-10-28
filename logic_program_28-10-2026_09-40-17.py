```python
# This script generates a simple, symmetrical ASCII art "pyramid" or "diamond" shape.
# You can easily change its size and the character it uses!

# --- Configuration Section ---
# Set the maximum width of the pyramid's base (must be an odd number for perfect symmetry).
# Try values like 5, 7, 9!
pyramid_base_width = 7

# Choose the character to build the pyramid with.
# Experiment with different characters like '#', 'o', 'X', or even '$'!
pyramid_character = '*'

# --- Drawing Logic Section ---

print("--- Your Unique Pyramid ---")

# Calculate the number of rows for the top half (or full pyramid if it's a simple triangle)
# This uses integer division (//) to make sure it works correctly for odd numbers.
num_rows = (pyramid_base_width + 1) // 2

# Loop to draw the top half of the pyramid (widening rows)
for i in range(num_rows):
    # Calculate how many characters to print for the current row
    # It starts with 1 character and increases by 2 each row (1, 3, 5, ...)
    current_chars = (2 * i) + 1

    # Calculate how many spaces are needed on each side to center the characters
    # This ensures the pyramid looks balanced
    leading_spaces = (pyramid_base_width - current_chars) // 2

    # Print the row: spaces + characters + spaces
    # We use string multiplication (' ' * N) to repeat spaces N times
    # and string concatenation (+) to join them together
    print(' ' * leading_spaces + pyramid_character * current_chars)

# Loop to draw the bottom half of the pyramid (narrowing rows), if base width > 1
# This loop starts from the row before the widest part and goes down
# For example, if num_rows was 4, it would loop for i = 2, 1, 0
for i in range(num_rows - 2, -1, -1):
    current_chars = (2 * i) + 1
    leading_spaces = (pyramid_base_width - current_chars) // 2
    print(' ' * leading_spaces + pyramid_character * current_chars)

print("--- Done Drawing! ---")

```
