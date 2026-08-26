```python
# Import the 'random' module to use its random selection functions
import random

# Define a list of possible actions or choices
actions = ["rock", "paper", "scissors", "lizard", "Spock"]

# Ask the user for their name to personalize the output
player_name = input("Hello there! What's your name? ")

# Print a greeting message including the player's name
print(f"Welcome, {player_name}! Let's play a little game.")

# Use the random.choice() function to select one item from the 'actions' list
computer_choice = random.choice(actions)

# Print out what the "computer" (script) has chosen
print(f"I'm thinking... I choose: {computer_choice}!")

# Give the player a hint of what they could choose
print(f"You could have chosen from: {', '.join(actions)}")

# A simple closing message
print("Hope you had fun!")
```
