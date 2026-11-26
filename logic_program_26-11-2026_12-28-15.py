```python
# This script takes your favorite color and draws a simple pattern with it!

# First, we ask the user for their favorite color.
# The 'input()' function lets us get text from the user.
favorite_color = input("What is your favorite color? ")

# Next, we ask for a number. This will determine how many times we repeat the pattern.
# 'input()' always returns text, so we use 'int()' to convert it to a whole number.
repeat_count = int(input("Enter a small number (e.g., 1 to 5): "))

# We can also get a simple symbol to use in our pattern.
pattern_symbol = input("Enter a simple symbol (e.g., *, #, @): ")

# Now, let's create a decorative line using the color.
# String multiplication (color * number) repeats the string.
decorative_line = favorite_color * 10

# Print the top decorative line.
print(decorative_line)

# This loop will print our pattern 'repeat_count' number of times.
# A 'for' loop is perfect for repeating actions.
for i in range(repeat_count):
    # Inside the loop, we use an f-string to easily combine text and variables.
    # We print the symbol, the color, and then the symbol again.
    # The 'i' variable from the loop tells us which repetition we are on (0, 1, 2...).
    print(f"{pattern_symbol} My favorite is {favorite_color.upper()} {pattern_symbol}")

# Print the bottom decorative line, same as the top.
print(decorative_line)

# A final message to the user, using their color again.
print(f"Isn't {favorite_color} lovely?")
```
