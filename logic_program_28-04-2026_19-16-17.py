```python
# A simple script that generates a "secret message" based on user input.
# It demonstrates input, variables, string concatenation, and f-strings.

# Get the user's first name.
first_name = input("What is your first name? ")

# Get their favorite color.
favorite_color = input("What is your favorite color? ")

# Get a random number from the user.
# int() converts the input string to an integer, which is a number.
secret_number = int(input("Pick a lucky number (1-100): "))

# Create a "secret message" by combining the inputs.
# f-strings (formatted string literals) are a modern way to embed variables directly into strings.
secret_message = f"Hello, {first_name}! Your secret code is {favorite_color.upper()}-{secret_number * 7}."
# .upper() is a string method that converts all letters in 'favorite_color' to uppercase.
# 'secret_number * 7' performs a simple multiplication with the number.

# Print the generated secret message to the console.
print("\nHere is your unique secret message:")
print(secret_message)

# A final, simple message.
print("Keep it safe!")
```
