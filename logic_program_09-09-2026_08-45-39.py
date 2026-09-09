```python
# Import the 'random' module.
# This module provides functions for generating random numbers and making random choices.
import random

# Define a list of positive adjectives.
# A list is an ordered collection of items. Each item here is a string (text).
adjectives = [
    "sparkling",
    "brilliant",
    "charming",
    "fantastic",
    "wonderful",
    "awesome",
    "vibrant",
    "stellar"
]

# Define another list, this time with encouraging nouns or concepts.
nouns = [
    "spirit",
    "mind",
    "smile",
    "effort",
    "day",
    "presence",
    "perspective",
    "journey"
]

# Use 'random.choice()' to select one random item from the 'adjectives' list.
# The selected item is stored in the 'chosen_adjective' variable.
chosen_adjective = random.choice(adjectives)

# Similarly, select one random item from the 'nouns' list.
chosen_noun = random.choice(nouns)

# Create a personalized motivational message using an f-string.
# An f-string allows you to embed variables directly inside string literals by
# placing an 'f' before the opening quote and writing variables in curly braces {}.
message = f"You have a {chosen_adjective} {chosen_noun} today!"

# Print a decorative header to the console.
print("--- Your Daily Boost ---")

# Print the dynamically generated motivational message.
print(message)

# Print a decorative footer.
print("------------------------")
```
