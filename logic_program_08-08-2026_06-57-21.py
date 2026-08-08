# --- Tiny Text Art Generator ---
# This script creates a simple triangular pattern using a character you choose.

# Ask the user for a single character to use in the art.
# Example: If user enters '*', the art will be made of stars.
art_char = input("Enter a single character for your art (e.g., *, #, @): ")

# Optional: If the user types more than one character, just take the first one.
if len(art_char) > 1:
    print("Just taking the first character you entered for consistency.")
    art_char = art_char[0] # Selects only the first character

# Ask the user for the size of the art (how tall the main peak of the triangle will be).
# This input needs to be converted from text to a whole number.
try:
    art_size = int(input("Enter the size of your art (a small whole number, e.g., 5): "))
except ValueError:
    # If the user doesn't enter a valid number, catch the error and set a default size.
    print("That's not a valid whole number. Defaulting size to 3.")
    art_size = 3 # Fallback value

# Ensure the size is at least 1, to prevent empty art or errors with range().
if art_size < 1:
    print("Size must be at least 1. Setting size to 1.")
    art_size = 1

print("\n--- Here is your tiny text art ---")

# Part 1: Growing triangle (from 1 up to art_size lines)
# The 'range(1, art_size + 1)' generates numbers from 1 up to 'art_size'.
for i in range(1, art_size + 1):
    # Print the chosen character 'i' times on each line.
    # Example: If i is 3, it prints '***'
    print(art_char * i)

# Part 2: Shrinking triangle (from art_size-1 down to 1 lines)
# We start from 'art_size - 1' because the 'art_size' line was already printed above.
# The 'range(start, stop, step)' with a negative step counts downwards.
# It goes from 'art_size - 1' down to (but not including) 0.
for i in range(art_size - 1, 0, -1):
    # Print the chosen character 'i' times on each line.
    # Example: If i is 2, it prints '**'
    print(art_char * i)

print("--- Art generated! ---")
