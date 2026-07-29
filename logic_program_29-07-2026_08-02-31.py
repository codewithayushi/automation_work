```python
# A unique Python script for beginners: The "Echo Shape" printer.
# This script asks for a character and a size, then prints a symmetrical shape.

# Get a character from the user to build the shape.
# input() reads text from the console.
shape_char = input("Enter a single character for your shape (e.g., *, #, @): ")

# Ensure we only use the first character if the user typed more.
# This makes the script more robust for beginners who might type multiple characters.
shape_char = shape_char[0] if shape_char else '*' # Default to '*' if empty input

# Get an integer from the user for the size of the shape.
# int() converts the input text into a whole number.
# We'll assume the user enters a valid number for simplicity.
shape_size_str = input("Enter a size for your shape (a small positive number, e.g., 3, 5, 7): ")

try:
    shape_size = int(shape_size_str)
    # Ensure the size is positive. If not, default to 3.
    if shape_size <= 0:
        print("Size must be positive. Defaulting to 3.")
        shape_size = 3
except ValueError:
    # Handle cases where the user doesn't enter a valid number.
    print("Invalid size entered. Defaulting to 3.")
    shape_size = 3

print("\nHere's your Echo Shape:")

# Part 1: Build the shape upwards (growing rows)
# A 'for' loop is used to repeat actions a specific number of times.
# range(1, shape_size + 1) generates numbers from 1 up to 'shape_size'.
for i in range(1, shape_size + 1):
    # String multiplication: 'char' * number repeats the character 'number' times.
    # print() displays the result to the console.
    print(shape_char * i)

# Part 2: Build the shape downwards (shrinking rows)
# range(shape_size - 1, 0, -1) generates numbers from 'shape_size - 1' down to 1.
# The third argument, -1, tells range to count backwards.
for i in range(shape_size - 1, 0, -1):
    print(shape_char * i)

# The script finishes after printing the shape.
print("\nHope you enjoyed your custom shape!")
```
