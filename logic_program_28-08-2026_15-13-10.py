```python
# This script creates a simple "magic eight ball" style fortune teller!

# First, we need to ask the user a question.
question = input("Ask the Magic Orb a yes/no question: ")

# Next, we define a list of possible answers the Orb can give.
possible_answers = [
    "It is certain.",
    "Without a doubt.",
    "Yes, definitely.",
    "Reply hazy, try again.",
    "Ask again later.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# To pick a random answer, we need the 'random' module.
import random

# Now, we use random.choice() to select one answer from our list.
magic_answer = random.choice(possible_answers)

# Finally, we print the chosen answer back to the user.
print(f"The Magic Orb says: {magic_answer}")
print("May your day be filled with wonder!")
```
