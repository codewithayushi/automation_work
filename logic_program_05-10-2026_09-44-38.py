```python
# This script creates a personalized "magic message" using your name and a random choice!

import random # We need the 'random' module to pick a message

# 1. Greet the user and ask for their name
print("Hello there!")
user_name = input("What's your name? ") # Get user's name as input

# 2. Prepare a list of possible "magic messages"
magic_messages = [
    "You will discover something amazing today!",
    "A hidden talent of yours will shine brightly.",
    "Expect a delightful surprise very soon.",
    "Your kindness will make a big difference.",
    "Adventure awaits you just around the corner!"
]

# 3. Choose one message randomly from the list
chosen_message = random.choice(magic_messages) # random.choice() picks one item

# 4. Display the personalized magic message
print(f"\nHello, {user_name}! Here is your magic message:") # Use an f-string for easy formatting
print(chosen_message)

print("\nHave a wonderful day!") # End with a friendly farewell
```
