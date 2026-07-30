# A fun script to play with your name and see some Python magic!

# --- Part 1: Get User Input ---
# The 'input()' function asks the user to type something.
# '.strip()' removes any extra spaces from the beginning or end of what they type.
your_name = input("Hello, wonderful person! What's your name? ").strip()

# --- Part 2: Handle an Empty Name ---
# This 'if' statement checks if the 'your_name' variable is empty (meaning the user just pressed Enter).
# If it's empty, we assign a default name.
if not your_name:
    print("Oops! No name entered. Let's call you 'Mystery Seeker'!")
    your_name = "Mystery Seeker"

# --- Part 3: Name Length Fun ---
# The 'len()' function calculates how many characters are in a string.
name_length = len(your_name)
# An f-string (formatted string literal) allows us to easily embed variables into a string.
print(f"\nDid you know your name, '{your_name}', has {name_length} letters?")

# --- Part 4: A Playful Name Transformation ---
# We'll create a new version of the name with characters alternating between uppercase and lowercase.
bouncy_name = ""
# A 'for' loop iterates over each item in a sequence (like characters in a string).
# 'enumerate' gives us both the 'index' (position) and the 'char' (character) for each step.
for index, char in enumerate(your_name):
    # The '%' (modulo) operator gives the remainder of a division.
    # If the index is even (0, 2, 4...), we convert the character to uppercase.
    if index % 2 == 0:
        bouncy_name += char.upper()
    # Otherwise (if the index is odd), we convert the character to lowercase.
    else:
        bouncy_name += char.lower()

print(f"Here's your name, getting a bit bouncy: {bouncy_name}")

# --- Part 5: A Simple Repeating Pattern ---
# This 'if' checks if the name is long enough to have a distinct first and last letter.
if name_length >= 2:
    # String indexing: [0] gets the first character, [-1] gets the last character.
    first_char = your_name[0]
    last_char = your_name[-1]
    # We create a small pattern and use '*' to repeat it 3 times.
    # '.strip()' removes any trailing space from the multiplication.
    pattern = (first_char + "*" + last_char + " ") * 3
    print(f"And a little repeating pattern for you: {pattern.strip()}")
elif name_length == 1:
    # If the name is just one letter, we repeat it a few times.
    print(f"Just one letter! Here it is, amplified: {your_name[0] * 5}")
# No 'else' needed here, as the 'Mystery Seeker' case handles empty names.

# --- Part 6: Farewell Message ---
print("\nHope you enjoyed seeing your name in a new light!")
