```python
# Welcome to the "Mystery Message Scrambler"!
# This script takes your secret message and scrambles it for fun.

# First, we ask the user for their message.
# The 'input()' function pauses the script and waits for you to type.
original_message = input("Type your secret message: ")

# Next, we'll create a scrambled version of the message.
# We'll do this by reversing the message.
# [::-1] is a special way to slice a string that reverses it completely.
scrambled_message = original_message[::-1]

# Now, let's make it a little more unique.
# We'll take every second character from the reversed message.
# This makes it even harder to read!
# [::2] means "start at the beginning, go to the end, take every 2nd character".
super_scrambled_message = scrambled_message[::2]

# Finally, we'll print the original message and its scrambled version.
# The 'print()' function displays text on the screen.
# We're using f-strings (formatted string literals) for easy printing.
print(f"\nYour original message was: '{original_message}'")
print(f"Your secret scrambled message is: '{super_scrambled_message}'")

# A little hint for the secret decoder:
# To make it slightly harder, we only kept parts of the reversed message!
print("\nKeep this secret!")
```
