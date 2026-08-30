```python
# This script creates a simple "magic phrase" by combining two words!

# Ask the user for their first word
first_word = input("Think of an adjective (e.g., 'sparkling', 'sleepy'): ")

# Ask for a second word
second_word = input("Now, think of a noun (e.g., 'whisper', 'mountain'): ")

# Combine the words with a dash in between
magic_phrase = first_word + "-" + second_word

# Convert the combined phrase to all uppercase letters for dramatic effect
magic_phrase_loud = magic_phrase.upper()

# Print out the secret magic phrase!
print("\nYour unique magic phrase is:")
print(magic_phrase_loud + "!")

# A little extra message based on the length of the phrase
if len(magic_phrase_loud) > 15:
    print("Wow, that's a powerful phrase!")
else:
    print("A short and sweet phrase, indeed!")
```
