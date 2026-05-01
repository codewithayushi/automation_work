```python
# A tiny program to generate a simple "ASCII art" landscape based on user input.

# Welcome message for the user.
print("Let's create a small pixel landscape!")

# Ask the user how tall they want the main 'mountain' or 'peak' to be.
# input() gets text, int() converts it to a whole number.
# We also make sure the input is stripped of any extra spaces.
peak_height = int(input("How tall should the mountain be? (1-10): ").strip())

# Ask for a character to build the mountain.
mountain_char = input("What character should the mountain be made of? (e.g., ^, #, M): ").strip()

# Ask for a character to represent the 'sky'.
sky_char = input("What character should the sky be made of? (e.g., -, ., ~): ").strip()

# Make sure the height is within a reasonable range for beginners.
if 1 <= peak_height <= 10:
    print("\nHere is your landscape:")

    # First, draw the sky above the mountain.
    # We'll draw 2 rows of sky, using string multiplication.
    print(sky_char * 20) # A fixed width for simplicity
    print(sky_char * 20)

    # Now, draw the mountain itself.
    # We use a 'for' loop to draw each row of the mountain.
    # The 'range(peak_height)' means the loop runs 'peak_height' times.
    for i in range(1, peak_height + 1):
        # Calculate how many spaces are needed on each side to center the mountain.
        # The mountain gets wider as 'i' increases.
        spaces = peak_height - i
        # Calculate how many mountain characters are needed for the current row.
        # It's always an odd number: 1, 3, 5, ...
        mountain_segment_width = (i * 2) - 1

        # Print the row: spaces + mountain characters + spaces.
        print(" " * spaces + mountain_char * mountain_segment_width + " " * spaces)

    # Finally, draw a simple 'ground' line below the mountain.
    print("=" * 20) # A fixed width ground line

else:
    # If the input was outside the desired range, print an error.
    print("\nSorry, that height is out of range. Please choose between 1 and 10.")

print("\n--- Landscape generation complete! ---")
```
