```python
# Welcome to the "Magic Number Guesser" game!

# This script tries to guess a number you think of, but with a twist.
# It uses simple arithmetic and observation.

# --- Step 1: User thinks of a secret number ---
print("Think of any whole number between 1 and 100. Don't tell me!")
print("Press Enter when you're ready to proceed...")
input() # Pauses the script until the user presses Enter

# --- Step 2: Perform some operations on the secret number ---
print("\nNow, follow these instructions carefully (do the math in your head or on paper):")

# Instruction 1: Multiply by 2
print("1. Multiply your secret number by 2.")
input("Press Enter after multiplying...")

# Instruction 2: Add 10
print("2. Add 10 to that new result.")
input("Press Enter after adding...")

# Instruction 3: Divide by 2
print("3. Divide that new result by 2.")
input("Press Enter after dividing...")

# Instruction 4: Subtract your original secret number
print("4. Now, subtract your *original secret number* from this result.")
input("Press Enter after subtracting...")

# --- Step 3: Reveal the "magic" result ---
print("\nAlright, I've used my psychic powers!")
print("Is your final number... 5?")

# You can uncomment the line below to show how the math works for any number 'n':
# ((n * 2) + 10) / 2 - n
# (2n + 10) / 2 - n
# n + 5 - n
# 5

# This simple trick always results in 5, no matter the starting number!

print("\nThank you for playing the Magic Number Guesser!")
```
