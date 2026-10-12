```python
# This script helps you generate a simple 'story' based on your input.
# It demonstrates how to get user input and combine it into a sentence.

# --- Step 1: Get information from the user ---

# Ask the user for a name and store it in a variable called 'name'.
# The input() function waits for the user to type something and press Enter.
name = input("Enter a main character's name: ")

# Ask for an adjective and store it in 'adjective'.
adjective = input("Enter an adjective (e.g., 'sleepy', 'brave', 'sparkling'): ")

# Ask for a noun and store it in 'noun'.
noun = input("Enter a plural noun (e.g., 'cats', 'mountains', 'dreams'): ")

# Ask for a verb and store it in 'verb'.
verb = input("Enter a verb ending in -ing (e.g., 'running', 'singing', 'flying'): ")

# Ask for a number and convert it to an integer.
# The int() function converts text (like "5") into a number (like 5).
number = int(input("Enter a small whole number: "))

# --- Step 2: Construct and display the story ---

print("\n--- Your Adventure Story ---") # Print a title with newlines for spacing

# Use an f-string (formatted string literal) to easily combine text and variables.
# Variables inside curly braces {} are replaced with their values.
story = f"Once upon a time, there was a {adjective} hero named {name}."
print(story)

story_part2 = f"{name} loved to go {verb} with their {number} magical {noun}."
print(story_part2)

print("\nEnd of story!") # A concluding message
```
