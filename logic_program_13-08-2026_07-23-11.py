```python
# --- Welcome to the Super Simple Secret Message Decoder! ---

import random # This line imports the 'random' module, which helps us pick random things.

# This script creates a very basic "secret code" for a word you enter.
# It works by shifting letters and adding a random number.
# It's not secure at all, just for fun and learning!

# Ask the user for a word they want to encode.
# .strip() removes any extra spaces from the beginning or end.
# .lower() converts the word to all lowercase for easier processing.
original_word = input("Enter a word to make a secret code (e.g., 'hello'): ").strip().lower()

# Check if the user actually entered something.
if not original_word:
    print("Oops! You didn't enter a word. Try again!")
else:
    # Let's pick a random "shift" number.
    # This number will determine how much each letter changes.
    shift_amount = random.randint(3, 7) # Picks a random whole number between 3 and 7 (inclusive).

    # We'll build our secret message letter by letter.
    secret_message = [] # Start with an empty list to store our encoded letters.

    # Loop through each letter in the original word.
    for char in original_word:
        # Check if the character is an alphabet letter.
        # We'll only encode letters, other characters (like spaces, numbers) will stay as they are.
        if 'a' <= char <= 'z':
            # Convert the letter to its ASCII (numerical) value.
            # 'a' is 97, 'b' is 98, etc.
            char_code = ord(char)

            # Apply the shift!
            # We subtract 'ord('a')' to make 'a' become 0, 'b' become 1, etc.
            # Then we add the shift_amount.
            # The modulo operator (%) ensures the letter "wraps around" if it goes past 'z'.
            # For example, if 'z' (25) + shift_amount is 27, 27 % 26 is 1, which corresponds to 'b'.
            shifted_code = ((char_code - ord('a') + shift_amount) % 26) + ord('a')

            # Convert the new numerical value back to a character.
            shifted_char = chr(shifted_code)
            secret_message.append(shifted_char) # Add the shifted letter to our list.
        else:
            # If it's not a letter, just add it as is.
            secret_message.append(char)

    # Join all the letters in the list to form the final secret string.
    final_secret_code = "".join(secret_message)

    # Print the original word, the shift amount, and the secret message.
    print(f"\nOriginal word: '{original_word}'")
    print(f"Secret shift used: {shift_amount}") # This is part of the 'key' to decode!
    print(f"Your secret message: '{final_secret_code}'")
    print("\nTo decode, you'd need to shift each letter back by the 'Secret shift used' number!")

```
