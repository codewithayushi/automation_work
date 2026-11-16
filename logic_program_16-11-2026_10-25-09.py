```python
# This script generates a random inspiring quote from a predefined list.
# It introduces lists, importing modules, and using functions from those modules.

import random # The 'random' module helps us pick a random item.

# This is a 'list' of strings (text). Each string is an inspiring quote.
# Lists are useful for storing multiple related pieces of data.
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The best way to predict the future is to create it. - Peter Drucker",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar"
]

# Use the 'random.choice()' function to select one random quote from our 'quotes' list.
# This function takes a list as input and returns one item from it.
chosen_quote = random.choice(quotes)

# Print a friendly message, then display the randomly chosen quote.
# The 'print()' function is used to show output to the user.
print("✨ Here's some inspiration for you: ✨")
print(chosen_quote)

# Try running this script multiple times to see different quotes!
```
