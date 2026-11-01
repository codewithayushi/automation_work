```python
# This script generates a simple, custom pattern using a character you choose!

# --- Step 1: Get input from the user ---

# The 'input()' function displays a message to the user and waits for them to type something.
# Whatever the user types is stored as a 'string' (text) in the 'user_char' variable.
# '.strip()' is a useful string method that removes any accidental spaces from
# the beginning or end of the text the user types.
user_char = input("Enter a single character (like '*', '#', or 'x') to draw with: ").strip()

# --- Step 2: Validate and prepare the character for drawing ---

# This 'if-elif-else' block allows the script to make decisions based on user input.

# Check if the user didn't enter anything at all (the string is empty).
if not user_char:
    print("You didn't enter a character! Using '*' as the default.")
    user_char = '*'  # Assign '*' to user_char if it was empty.
# Check if the user entered more than one character.
elif len(user_char) > 1:
    # 'len()' is a function that tells us how many items (characters, in this case)
    # are in a sequence (like a string).
    # 'user_char[0]' uses 'indexing' to get only the *first* character from their input.
    print(f"You entered multiple characters. Using only the first one: '{user_char[0]}'")
    user_char = user_char[0] # Update user_char to be just the first character.
# If none of the above conditions are true, it means the user entered a single character,
# so 'user_char' is already good to go.
else:
    print(f"Great! Let's draw with '{user_char}'.")


# --- Step 3: Draw the pattern using the chosen character ---

# We use 'print()' multiple times to output each line of the pattern.
# 'f-strings' (formatted string literals, starting with 'f' before the quote)
# are an easy way to include variables directly inside your print message.
# Example: f"Hello, {name}!"
#
# The '*' operator, when used with a string and a number, repeats the string
# that many times! Example: "a" * 3 results in "aaa"

# Top part of the pattern
print(f"  {user_char}")         # Two spaces, then one character
print(f" {user_char * 3}")     # One space, then three characters
print(f"{user_char * 5}")      # No spaces, then five characters

# Bottom part of the pattern
print(f" {user_char * 3}")     # One space, then three characters
print(f"  {user_char}")         # Two spaces, then one character

# --- Step 4: A concluding message ---
# The '\n' creates a new line, making the output cleaner.
print("\nEnjoy your custom pattern!")
```
