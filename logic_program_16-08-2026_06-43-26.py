```python
# A simple script to create a personalized text pattern!

# Ask the user for their favorite character.
# We use .strip() to remove any accidental spaces around the input.
favorite_char = input("Enter your favorite single character (e.g., *, #, @): ").strip()

# Make sure we only use the first character if the user entered more.
# This prevents unintended long patterns and teaches basic string indexing.
if len(favorite_char) == 0:
    favorite_char = "*" # Default if user enters nothing
else:
    favorite_char = favorite_char[0]

# Ask the user for a word or phrase.
user_word = input("Enter a short word or phrase: ").strip()

# Ask how many times they want the pattern to repeat.
# We convert the input string to an integer using int().
num_repetitions_str = input("How many times should the pattern repeat? (Enter a number, e.g., 5): ").strip()

# Handle cases where the user might not enter a valid number.
# For simplicity, we'll just set a default if it's not a number.
try:
    num_repetitions = int(num_repetitions_str)
    if num_repetitions < 1: # Ensure at least one repetition
        num_repetitions = 1
except ValueError:
    print("That wasn't a number. Defaulting to 3 repetitions.")
    num_repetitions = 3 # Default value if conversion fails

print("\n--- Your Custom Pattern ---")

# Loop 'num_repetitions' times to create the pattern.
# 'i' will go from 0 up to (but not including) num_repetitions.
for i in range(num_repetitions):
    # Calculate how many 'favorite_char' to print before the word.
    # This creates an increasing indent effect.
    indent_chars = favorite_char * i

    # Print the pattern: indent, followed by the word, followed by the indent in reverse.
    # We use string concatenation (+) and string multiplication (*) here.
    # The [::-1] is a neat trick to reverse a string!
    print(f"{indent_chars}{user_word}{indent_chars[::-1]}")

print("---------------------------\n")

# A little extra message for fun!
print("Hope you liked your unique pattern!")
```
