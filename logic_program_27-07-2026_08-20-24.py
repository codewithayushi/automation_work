```python
# This script creates a simple "Word Mirror" effect.
# It takes a word from the user and prints it followed by its reverse,
# separated by a simple character, demonstrating basic string manipulation.

# Ask the user to enter a word.
# The 'input()' function gets text from the user.
user_word = input("Enter a word to see its mirror: ")

# Check if the user actually entered something.
# This is a good practice to avoid errors with empty input.
if user_word:
    # Reverse the word using string slicing.
    # [::-1] is a common Python trick to reverse sequences.
    reversed_word = user_word[::-1]

    # Create the mirror effect by concatenating the original word, a separator, and the reversed word.
    # The f-string (formatted string literal) is a modern way to embed variables in strings.
    mirror_effect = f"{user_word} | {reversed_word}"

    # Print the resulting mirror effect to the console.
    print(mirror_effect)

    # You can also show a slightly different mirror with a different separator.
    print(f"Another view: {user_word}--{reversed_word}")

else:
    # If the user didn't enter anything, print a message.
    print("You didn't enter a word!")

# End of script. Simple and fun for a beginner!
```
