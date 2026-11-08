```python
# This script creates a unique "Word Magic Spell" based on any word you type!

# Step 1: Get a word or name from the user.
# The 'input()' function displays a message and waits for the user to type something,
# then stores that text in the 'user_word' variable.
user_word = input("Enter a word or name for your magical spell: ")

# Step 2: Calculate the magical "length" of the word.
# The 'len()' function tells us how many characters are in the word.
word_length_magic = len(user_word)

# Step 3: Perform a secret magical calculation.
# We're multiplying the word's length by a "secret number" (3.14)
# and then adding a "lucky charm" (7).
# This creates a unique "magical energy" score.
magical_energy = (word_length_magic * 3.14) + 7

# Step 4: Add a special bonus if the word is particularly long.
# An 'if' statement checks a condition. If it's true, the code inside runs.
if word_length_magic > 8:
    # If the word is long, we'll give it an extra boost!
    magical_energy = magical_energy * 1.5 # Increase energy by 50%
    bonus_message = "Wow! Your word radiates extra strong magic!"
else:
    # If the word is not long, a different message is shown.
    bonus_message = "A perfectly balanced magical word!"

# Step 5: Display the results of our spell.
# 'f-strings' (formatted string literals) allow us to easily embed variables inside strings.
print("\n--- Your Word Magic Spell Results ---")
print(f"The word you chose: '{user_word}'")
print(f"Its mystical length: {word_length_magic} characters")
print(f"{bonus_message}")
print(f"Your word's total magical energy is: {magical_energy:.2f} units!") # '.2f' formats to 2 decimal places
print("May your spell bring wonder!")
```
