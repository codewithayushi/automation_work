```python
# This script creates a simple "magic 8-ball" style fortune teller.
# It will ask you a yes/no question and give a random answer!

import random # We need the 'random' module to pick an answer randomly.

# First, we define a list of possible answers.
# A list is a collection of items, and each item here is a string (text).
possible_answers = [
    "It is certain.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# We welcome the user and explain what the script does.
print("Welcome to the Python Fortune Teller!")
print("Ask me a yes/no question, and I'll reveal your fate...")

# Now, we get the user's question using the 'input()' function.
# The text inside input() is a prompt shown to the user.
user_question = input("Enter your question: ")

# To simulate the "magic," we pick one answer randomly from our list.
# 'random.choice()' takes a list and returns one random item from it.
chosen_answer = random.choice(possible_answers)

# Finally, we print the user's question (for context) and the chosen answer.
print("\nYou asked:", user_question)
print("The Fortune Teller says:", chosen_answer)

# This script demonstrates:
# - Importing modules (import random)
# - Creating and using lists (possible_answers)
# - Printing text to the console (print())
# - Getting input from the user (input())
# - Storing data in variables (user_question, chosen_answer)
# - Using a function from a module (random.choice())
```
