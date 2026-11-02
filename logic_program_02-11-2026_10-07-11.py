```python
# This script simulates a very simple "magic 8-ball" to answer yes/no questions.
# It uses the 'random' module to pick a different answer each time.

import random

# List of possible answers the magic 8-ball can give.
# These are strings, which are sequences of characters.
possible_answers = [
    "It is certain.",
    "Without a doubt.",
    "Yes, definitely.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good."
]

# 1. Ask the user to type their question.
# The input() function gets text from the user.
user_question = input("Ask the Magic 8-Ball a yes/no question: ")

# 2. Check if the user actually typed something.
# The 'if' statement allows the program to make decisions.
# len() gives us the length of the string.
if len(user_question) == 0:
    print("You didn't ask a question! Try again.")
else:
    # 3. The user asked a question, so let's pick a random answer.
    # random.choice() picks one item randomly from a list.
    chosen_answer = random.choice(possible_answers)

    # 4. Print the chosen answer.
    # f-strings (formatted string literals) make it easy to embed variables.
    print(f"\nYour question: {user_question}")
    print(f"Magic 8-Ball says: {chosen_answer}")

# To run this script:
# 1. Save it as a .py file (e.g., magic_8_ball.py).
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Type: python magic_8_ball.py
# 5. Press Enter and answer the prompt!
```
