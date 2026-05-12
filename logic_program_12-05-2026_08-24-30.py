```python
# A simple "Fortune Cookie" script!
# It will give you a random piece of wisdom or a silly prediction.

import random # This line imports the 'random' module, which helps us pick things randomly.

# Create a list of fortunes.
# A list is an ordered collection of items (in this case, strings of text).
fortunes = [
    "You will find happiness in unexpected places.",
    "A journey of a thousand miles begins with a single step.",
    "Beware of the man who doesn't like cats.",
    "Your future is bright, wear sunglasses.",
    "Don't eat yellow snow.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Opportunity knocks, but temptation pounds on the door.",
    "You will soon be sitting on top of the world.",
    "A pleasant surprise is waiting for you.",
    "Patience is a virtue, unless you're trying to catch a fly.",
    "The best way to predict the future is to create it.",
    "Don't forget to smile today!"
]

# Ask the user if they want a fortune.
# The 'input()' function gets text from the user.
# We convert the input to lowercase for easier checking.
user_input = input("Want a fortune? (yes/no): ").lower()

# Check the user's response using an 'if' statement.
# 'if', 'elif' (else if), and 'else' help us make decisions in our code.
if user_input == "yes":
    # If the user said 'yes', pick a random fortune from our list.
    # 'random.choice(list_name)' picks one item randomly from the list.
    chosen_fortune = random.choice(fortunes)

    # Print the chosen fortune to the console.
    print("\nYour fortune is:", chosen_fortune)
elif user_input == "no":
    # If the user said 'no'.
    print("\nOkay, maybe next time!")
else:
    # If the user typed anything else.
    print("\nI didn't understand that. Come back when you're ready!")

# The script ends here.
```
