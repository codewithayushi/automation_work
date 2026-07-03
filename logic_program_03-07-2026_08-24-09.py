```python
# This script is a simple "Magic 8-Ball" style program.
# It gives a random answer to a yes/no question.

import random # We need the 'random' module to pick a random answer.

print("Welcome to the Python Magic 8-Ball!")
print("Ask me a yes/no question, and I'll give you an answer.")
print("Type 'quit' to exit at any time.")

# A list of possible answers the Magic 8-Ball can give.
answers = [
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

# Start an infinite loop to keep asking questions until the user quits.
while True:
    # Get the user's question as input.
    user_question = input("\nWhat is your question? (or type 'quit'): ")

    # Check if the user wants to quit.
    if user_question.lower() == 'quit':
        print("Goodbye! Thanks for playing with the Magic 8-Ball.")
        break # Exit the loop if 'quit' is typed.
    
    # Check if the user actually typed a question (not just empty input).
    elif not user_question.strip():
        print("Please ask a question!")
        continue # Skip to the next iteration of the loop.

    # Pick a random answer from our 'answers' list.
    # random.choice() is a great way to pick a random item from a list.
    random_answer = random.choice(answers)

    # Print the chosen random answer to the user.
    print(f"The Magic 8-Ball says: {random_answer}")

```
