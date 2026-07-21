```python
# This script creates a personalized "magic number" based on user input!

# First, we ask the user for their favorite number.
# The `input()` function gets text from the user.
# `int()` converts that text into a whole number.
favorite_number_str = input("Enter your favorite whole number: ")
favorite_number = int(favorite_number_str)

# Next, we ask for their favorite color.
# We'll use the length of this word in our calculation.
favorite_color = input("Enter your favorite color (e.g., blue, green): ")

# Calculate the "color value" based on the number of letters in the color
color_value = len(favorite_color)

# Now, we perform a unique calculation to find the "magic number".
# We use basic arithmetic: multiplication, addition, and the modulo operator (%).
# The modulo operator gives the remainder after division, making the number a bit mysterious!
magic_number = (favorite_number * color_value + 7) % 100

# We'll also reverse a part of the color for an extra touch!
# This slices the color from the second character onwards, and then reverses it using [::-1].
reversed_color_part = favorite_color[1:][::-1]

# Finally, we print the results in an exciting way!
# The `f-string` (formatted string literal) makes it easy to embed variables.
print("\n--- Your Magic Results ---")
print(f"Your chosen favorite number: {favorite_number}")
print(f"The length of your favorite color ('{favorite_color}'): {color_value}")
print(f"A reversed part of your color for extra magic: '{reversed_color_part}'")
print(f"Your unique MAGIC NUMBER is: {magic_number}!")
print("--------------------------")
```
