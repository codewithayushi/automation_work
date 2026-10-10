```python
# Import the 'random' module, which has tools for random operations.
# We'll use it to shuffle things later!
import random

# Ask the user to enter some text and store it in a variable.
# The 'input()' function pauses the script and waits for user typing.
user_input = input("Enter a word or a short phrase: ")

# Convert the input string into a list of individual characters.
# For example, "cat" becomes ['c', 'a', 't'].
# This makes it easy to move the letters around.
list_of_characters = list(user_input)

# Use the 'shuffle' function from the 'random' module.
# It rearranges the items in our list completely randomly.
random.shuffle(list_of_characters)

# Join the shuffled characters back together to form a new string.
# The "" before .join() means there's nothing between the characters.
scrambled_text = "".join(list_of_characters)

# Print the original text the user entered.
print(f"You entered: '{user_input}'")

# Print the new, scrambled version of the text.
print(f"Here's your text, all mixed up: '{scrambled_text}'")

# Add a simple check: what if the user didn't type anything?
# '.strip()' removes any spaces from the beginning or end of the input.
if not user_input.strip():
    print("It looks like you didn't enter any text! Try again next time.")

```
