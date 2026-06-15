```python
# Import the 'random' module to help us pick things randomly
import random

# A list of friendly and quirky greetings
greetings = [
    "Hello", "Hi there", "Greetings", "Hey", "Howdy", "Salutations", "Aloha"
]

# A list of interesting and unique objects
objects = [
    "cosmic pineapple", "sleepy cloud", "whispering teapot",
    "dancing sock", "pixelated rainbow", "glowing pebble",
    "invisible bicycle", "velvet robot", "echoing spoon"
]

# A list of whimsical actions
actions = [
    "is floating by", "is dreaming loudly", "is solving mysteries",
    "is having an adventure", "is waving hello", "is silently giggling",
    "is coding Python"
]

# Randomly choose one greeting from our 'greetings' list
chosen_greeting = random.choice(greetings)

# Randomly choose one object from our 'objects' list
chosen_object = random.choice(objects)

# Randomly choose one action from our 'actions' list
chosen_action = random.choice(actions)

# Combine these chosen words into a unique, whimsical sentence
# We use an f-string for easy insertion of variables into a string
whimsical_sentence = f"{chosen_greeting}! A {chosen_object} {chosen_action}."

# Print the generated sentence to the console
print("Here's your unique whimsical message:")
print(whimsical_sentence)

# Run the script again to get a different, unique message!
```
