```python
# This script creates a tiny, personalized "magic message" based on your input!

# First, we'll ask the user for a few words.
# The 'input()' function gets text from the user.
favorite_color = input("What is your favorite color? ")
animal_type = input("Name a type of animal (plural, e.g., 'kittens'): ")
action_verb = input("Give me an action verb (e.g., 'dancing'): ")
adjective_word = input("Think of an interesting adjective (e.g., 'sparkling'): ")

# Now, we'll combine these words into a mystical message.
# We're using an f-string (formatted string literal) which makes it easy
# to embed variables directly into the text.
magic_message = f"""
The ancient spirits whisper:
"Seek the {adjective_word} {favorite_color} light,
where {animal_type} are {action_verb} in the night.
Your future is as bright as a star!"
"""

# Finally, we print the completed message to the console.
# The '\n' at the beginning and end of the first print statement adds an empty line
# for better readability before and after the message.
print("\n--- Your Daily Cosmic Insight ---")
print(magic_message)
print("---------------------------------\n")

# Try running it again with different words for a new message!
```
