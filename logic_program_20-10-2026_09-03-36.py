```python
# Import the random module to use its shuffling capabilities
import random

# Get a word or phrase from the user
user_input = input("Enter a word or a short phrase: ")

# Convert the input string into a list of individual characters
# This allows us to reorder them
character_list = list(user_input)

# Randomly shuffle the order of characters in the list
random.shuffle(character_list)

# Join the shuffled characters back together to form a new string
mixed_up_string = "".join(character_list)

# Display the original input and the newly mixed-up version
print(f"Original: '{user_input}'")
print(f"Mixed-up: '{mixed_up_string}'")
```
