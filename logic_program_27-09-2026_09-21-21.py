```python
# This script creates a simple "staircase" pattern using your chosen character!

# First, we ask the user to enter a single character.
# The 'input()' function gets text from the user.
user_character = input("Enter any single character to build your staircase: ")

# Next, we ask for the height of the staircase.
# 'input()' always returns a string, so we use 'int()' to convert it to a whole number.
staircase_height = int(input("How tall should your staircase be? (Enter a number, e.g., 5): "))

print("\n--- Here is your custom staircase! ---")

# We use a 'for' loop to repeat an action a certain number of times.
# 'range(1, staircase_height + 1)' creates numbers from 1 up to the height (inclusive).
for step_number in range(1, staircase_height + 1):
    # Inside the loop, we print the user's character.
    # Multiplying a string by a number repeats the string!
    # So, 'user_character * 3' would print the character three times.
    print(user_character * step_number)

print("------------------------------------")
print("Hope you enjoyed building your unique pattern!")
```
