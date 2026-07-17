```python
# Script: The "Mirror Number" Generator
# This script takes a number from the user,
# then creates a new number by concatenating the original number
# with its digits reversed.

# Get input from the user. input() returns a string.
user_number_str = input("Enter a positive whole number: ")

# Reverse the string of the number.
# Slicing with [::-1] creates a reversed copy of the string.
reversed_number_str = user_number_str[::-1]

# Concatenate the original number string with its reversed version.
# This creates our unique "mirror number".
mirror_number_str = user_number_str + reversed_number_str

# Display the original and the new mirror number.
print(f"Your original number was: {user_number_str}")
print(f"Your unique mirror number is: {mirror_number_str}")

# You can even convert it to an integer if you want to do math with it!
# For example, to check its type:
# print(f"Type of mirror_number_str: {type(mirror_number_str)}")
# mirror_number_int = int(mirror_number_str)
# print(f"Mirror number as integer: {mirror_number_int}")
# print(f"Type of mirror_number_int: {type(mirror_number_int)}")
```
