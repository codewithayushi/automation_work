```python
# A simple script to create a "rainbow" phrase using colors!
# This introduces basic string manipulation, lists, and loops.

import random # We need this to pick random colors later

# Define a list of simple "color" characters for our rainbow effect.
# These will visually represent different parts of our "rainbow".
RAINBOW_COLORS = ['🟥', '🟧', '🟨', '🟩', '🟦', '🟪']

# Ask the user for a phrase they want to make colorful.
user_phrase = input("Enter a phrase to make it sparkle: ")

# Create an empty list to store our colored characters.
# We'll build the new phrase character by character.
colored_phrase_parts = []

# Loop through each character in the user's phrase.
# 'enumerate' helps us get both the index (position) and the character itself.
for index, char in enumerate(user_phrase):
    # If the character is a space, just add it as is (we don't color spaces).
    if char == ' ':
        colored_phrase_parts.append(' ')
    else:
        # For non-space characters, pick a color from our RAINBOW_COLORS.
        # We use the 'index' to cycle through colors, making a smooth transition.
        # The '%' (modulo) operator ensures we loop back to the start of the colors
        # list if the phrase is longer than the number of colors.
        color_index = index % len(RAINBOW_COLORS)
        selected_color = RAINBOW_COLORS[color_index]

        # Add the character, wrapped in its chosen "color" (emoji).
        # We put the color emoji BEFORE and AFTER the character for emphasis.
        colored_phrase_parts.append(f"{selected_color}{char}{selected_color}")

# Join all the colored parts back into a single string.
final_rainbow_phrase = "".join(colored_phrase_parts)

# Print the finished, colorful phrase!
print("\nHere's your sparkling rainbow phrase:")
print(final_rainbow_phrase)

# A little extra magic: a randomly chosen bonus color for fun!
bonus_color = random.choice(RAINBOW_COLORS)
print(f"\n{bonus_color} Keep coding! {bonus_color}")
```
