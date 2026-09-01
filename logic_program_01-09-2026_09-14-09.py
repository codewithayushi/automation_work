```python
# This script creates a simple, fun "magic number" prediction game.
# It's great for beginners to learn input, output, variables, and basic math.

# 1. Ask the user for their favorite number.
# The `input()` function gets text from the user.
# `int()` converts that text into a whole number, so we can do math.
favorite_number = int(input("Enter your favorite whole number (e.g., 7): "))

# 2. Perform a series of mathematical operations on their number.
# This sequence is designed to always lead to the same final number, regardless of the start.

# Add 5 to the number.
magic_number = favorite_number + 5

# Multiply the result by 2.
magic_number = magic_number * 2

# Subtract 4 from that.
magic_number = magic_number - 4

# Divide the new result by 2.
magic_number = magic_number // 2 # Use // for integer division (no decimals).

# Finally, subtract their original favorite number.
magic_number = magic_number - favorite_number

# 3. Print out the 'predicted' magic number.
# The `print()` function displays text and variables to the user.
# An f-string (formatted string literal) makes it easy to embed variables.
print(f"\nThinking of your number, I predict the final result is: {magic_number}!")

# 4. A little explanation for fun.
print("Isn't that neat? It always ends up being 3!")
print("Try running the script again with a different starting number!")
```
