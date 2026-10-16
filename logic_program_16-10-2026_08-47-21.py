```python
# This script is a simple "Magic Number Guesser" game.
# It picks a secret number, and you try to guess it!

import random # The 'random' module helps us pick a random number.

# 1. Greet the player and get their name.
# The 'input()' function asks the user for text and stores it in a variable.
player_name = input("Hello, adventurer! What is your name? ")
print(f"Welcome, {player_name}! Let's play a guessing game.") # f-strings allow easy embedding of variables in strings.

# 2. Pick a secret number.
# 'random.randint(1, 10)' generates a random whole number between 1 and 10 (inclusive).
secret_number = random.randint(1, 10)
print("I'm thinking of a secret number between 1 and 10.")
print("Can you guess what it is?")

# 3. Get the player's guess.
# We use a 'while' loop to keep asking until the guess is correct.
# 'int()' is used to convert the input string into a whole number (integer).
guess = 0 # Initialize guess to a value that won't match the secret number initially.
guess_count = 0 # Keep track of how many guesses the player makes.

while guess != secret_number: # The loop continues as long as the guess is NOT equal to the secret number.
    try: # 'try-except' block helps handle potential errors, like if the user types text instead of a number.
        player_guess = input("Take a guess (enter a number): ")
        guess = int(player_guess) # Convert the user's input to an integer.
        guess_count += 1 # Increment the guess count for each attempt.

        # 4. Give hints to the player.
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        # If the guess is not lower and not higher, it must be correct, so the loop will end.

    except ValueError: # If 'int(player_guess)' fails (e.g., user types "hello"), this block runs.
        print("Oops! That's not a valid number. Please enter a whole number.")

# 5. Congratulate the player when they guess correctly.
print(f"\n🎉 Congratulations, {player_name}! You guessed the secret number!")
print(f"The number was indeed {secret_number}.")
print(f"It took you {guess_count} guesses to find it.")
print("Thanks for playing!")
```
