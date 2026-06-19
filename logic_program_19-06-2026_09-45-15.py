```python
# This script simulates a Magic 8-Ball.
# It gives a random answer to any yes/no question you ask!

import random # We need this module to pick a random item from a list.

# Here's a list (a collection) of all possible answers the Magic 8-Ball can give.
possible_answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
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

# Print a welcome message to the user.
print("🔮 Welcome to the Mystical Magic 8-Ball! 🔮")
print("Ask me any yes/no question, and I shall reveal its answer.")

# Get the user's question. The question itself doesn't affect the answer,
# it just makes the interaction more fun!
user_question = input("\nWhat is your question? (Press Enter when done): ")

# Choose one random answer from our 'possible_answers' list.
# 'random.choice()' is perfect for this.
the_magic_answer = random.choice(possible_answers)

# Print the chosen answer back to the user.
print("\nThe Magic 8-Ball says...")
print(f"✨ {the_magic_answer} ✨")

print("\nThank you for consulting the 8-Ball!")
```
