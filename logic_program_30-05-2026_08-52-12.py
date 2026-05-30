```python
# A magical "emoji name generator" script!

import random # This line lets us use random choices

# Get the user's name
user_name = input("Enter your name: ")

# A list of fun emojis to choose from
emojis = ["✨", "🌈", "🚀", "💡", "💖", "🌟", "🎉", "🦋"]

# Choose a random emoji for the beginning and end
start_emoji = random.choice(emojis)
end_emoji = random.choice(emojis)

# Make sure the start and end emojis are different for extra uniqueness
while start_emoji == end_emoji:
    end_emoji = random.choice(emojis)

# Combine them into a new "magical" name
magical_name = f"{start_emoji} {user_name.upper()} {end_emoji}"

# Print the newly generated name!
print("\nYour magical new name is:")
print(magical_name)

# This script demonstrates:
# - Importing a module (random)
# - Taking user input (input())
# - Storing data in a list []
# - Choosing random items from a list (random.choice())
# - Using a loop for a specific condition (while)
# - String manipulation (.upper(), f-strings)
# - Printing formatted output (print())
```
