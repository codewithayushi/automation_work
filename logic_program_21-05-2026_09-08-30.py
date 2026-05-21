```python
# This script creates a simple "guess the number" game.
# The computer picks a secret number, and you try to guess it.

import random # We need this module to generate random numbers.

def play_guess_the_number():
    """
    Runs the 'guess the number' game.
    The computer chooses a random number within a set range.
    The user tries to guess it, receiving hints (too high/low).
    """
    
    # 1. Computer chooses a secret number
    # It will pick an integer between 1 and 10 (inclusive).
    secret_number = random.randint(1, 10) 
    
    # 2. Initialize variables to keep track of the game
    guess_count = 0     # How many guesses the user has made
    user_guess = None   # Stores the user's current guess, initialized to nothing

    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10.")
    print("Can you guess what it is?")

    # 3. Start a loop that continues until the user guesses correctly
    while user_guess != secret_number:
        guess_count += 1 # Increment the guess count for each attempt

        try:
            # Get input from the user and convert it to an integer
            guess_str = input(f"Guess #{guess_count}: Enter your guess: ")
            user_guess = int(guess_str) # Convert the text input to a whole number
        except ValueError:
            # Handle cases where the user enters something that isn't a number
            print("That's not a valid number. Please enter a whole number.")
            continue # Skip the rest of this loop iteration and ask for input again

        # Provide hints based on the user's guess
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        # If user_guess equals secret_number, the 'while' loop condition becomes false,
        # and the script will exit the loop.

    # 4. Congratulate the user once they guess correctly
    print(f"\nCongratulations! You guessed the number '{secret_number}' in {guess_count} guesses.")

# --- This is the main part of the script that runs the game ---
if __name__ == "__main__":
    play_guess_the_number() # Call the function to start the game
```
