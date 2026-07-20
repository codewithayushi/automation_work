```python
# A simple "Magic 8-Ball" game!
# Ask a question and get a mystical answer.

import random # We need this to pick a random answer.

# A list of possible answers the 8-ball can give.
# Lists are ordered collections of items.
possible_answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
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
print("Welcome to the Magic 8-Ball!")
print("Ask a yes/no question, or type 'quit' to exit.")

# This 'while True' loop keeps the game running indefinitely
# until a 'break' statement is encountered.
while True:
    # Get input from the user. The text inside input() is a prompt.
    user_question = input("\nWhat is your question? ")

    # Check if the user wants to quit the game.
    # .lower() converts the input to lowercase, so 'Quit' or 'QUIT' also work.
    if user_question.lower() == 'quit':
        print("Goodbye!")
        break # This statement exits the 'while True' loop.
    # Check if the user entered an empty question (or just spaces).
    # .strip() removes leading/trailing whitespace.
    elif not user_question.strip():
        print("Please ask a question!")
        continue # This skips the rest of the current loop iteration and starts the next one.
    else:
        # random.choice() picks one random item from the list.
        magic_answer = random.choice(possible_answers)
        # An f-string (formatted string literal) allows embedding expressions inside string literals.
        print(f"Magic 8-Ball says: {magic_answer}")
```
