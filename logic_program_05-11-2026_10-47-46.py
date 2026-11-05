```python
# This script tells you if a number is even or odd.
# It's a simple example of getting input, using variables, and making decisions.

# First, we print a welcome message to the user.
print("Welcome to the Even or Odd Checker!")

# Ask the user to enter a whole number.
# The 'input()' function gets text from the user.
# We then convert that text into an integer (a whole number) using 'int()'.
# This allows us to perform mathematical operations on it.
try:
    user_number = int(input("Please enter a whole number: "))

    # The '%' operator is called the "modulo" operator.
    # It gives us the remainder of a division.
    # If a number divided by 2 has a remainder of 0, it's even.
    # Otherwise, it's odd.
    if user_number % 2 == 0:
        # If the remainder is 0, the number is even.
        # We use an f-string to easily include the variable 'user_number' in our message.
        print(f"The number {user_number} is EVEN.")
    else:
        # If the remainder is not 0 (it will be 1 for whole numbers), the number is odd.
        print(f"The number {user_number} is ODD.")

# This 'except' block handles cases where the user doesn't enter a valid number.
# It's good practice to anticipate errors for a better user experience.
except ValueError:
    print("That's not a valid whole number! Please try again with a number.")

print("Thank you for using the Even or Odd Checker!")
```
