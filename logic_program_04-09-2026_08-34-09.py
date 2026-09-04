```python
# This script is a fun "Magic 8-Ball" style decision maker.
# It will answer any yes/no question you ask it!

# First, we need to import the 'random' module.
# This module allows us to pick things randomly.
import random

# Here we create a list of possible answers.
# A list is a collection of items, enclosed in square brackets [].
possible_answers = [
    "It is certain.",
    "Absolutely not.",
    "Yes, definitely!",
    "Reply hazy, try again.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook good.",
    "Signs point to yes."
]

# Now, we ask the user for their question.
# The input() function displays a message and waits for the user to type something.
# Whatever the user types is stored in the 'user_question' variable.
user_question = input("Ask your yes/no question (e.g., 'Will it rain today?'): ")

# Next, we pick a random answer from our list.
# random.choice() takes a list and returns one random item from it.
magic_answer = random.choice(possible_answers)

# Finally, we print the chosen answer to the user.
# The print() function displays text or variable values on the screen.
print(f"The Magic 8-Ball says: {magic_answer}")

# That's it! Try running the script multiple times with different questions.
```
