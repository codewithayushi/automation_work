```python
# A unique, short Python script for beginners!

# Part 1: Define a list of initial "magic words"
magic_words = ["abracadabra", "hocus pocus", "sim sala bim", "alakazam"]

# Part 2: Print the current list of magic words
print("My current collection of magic words:")
for word in magic_words:
    print(f"- {word.capitalize()}") # .capitalize() makes each word start with a capital letter

# Part 3: Ask the user to contribute a new "magic word"
new_word = input("\nWhat's a new magic word you know? ")

# Part 4: Add the user's word to our list, converting it to lowercase for consistency
magic_words.append(new_word.lower())

# Part 5: Import the 'random' module to pick a word at random
import random

# Part 6: Randomly select one "super special" magic word from our updated list
super_special_word = random.choice(magic_words)

# Part 7: Print a fun message using our super special word!
print(f"\nBehold! The ancient texts reveal the 'Super Special Magic Word' is...")
print(f"✨ {super_special_word.upper()}! ✨") # .upper() makes it all capital letters

# Part 8: Briefly show the final, updated list of magic words
print("\nMy complete enchanted lexicon now includes:")
print(magic_words)
```
