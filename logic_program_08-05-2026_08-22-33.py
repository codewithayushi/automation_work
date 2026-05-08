```python
# This script creates a tiny interactive story, like a very simple "Mad Libs".
# It asks you for a few words and then puts them into a sentence.

# We'll use the 'input()' function to get text from the user.
# Whatever the user types and presses Enter for will be stored in the variable.

# Ask for a noun (a person, place, or thing)
noun = input("Please give me a singular noun (e.g., 'dog', 'tree'): ")

# Ask for an adjective (a descriptive word)
adjective = input("Now, give me an adjective (e.g., 'sleepy', 'sparkling'): ")

# Ask for a verb (an action word) in the past tense
past_tense_verb = input("Finally, a verb in the past tense (e.g., 'ran', 'jumped'): ")

# Now we combine the words into a sentence.
# We use an f-string (formatted string literal) for easy embedding of variables.
# The 'f' before the opening quote makes it an f-string.
# Variables inside curly braces {} within the f-string are replaced by their values.
story = f"The {adjective} {noun} {past_tense_verb} into the sunset, carrying a sandwich."

# Print the completed story for the user to see.
print("\n--- Your Amazing Story ---")
print(story)
print("--------------------------")
```
