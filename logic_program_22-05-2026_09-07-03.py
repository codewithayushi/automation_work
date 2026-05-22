```python
# This script simulates a very basic "Mood Tracker".
# It asks how you feel and then gives a simple, encouraging message.

# We will use the 'input()' function to get text from the user.
# And the 'print()' function to display messages.

# First, let's greet the user and ask how they are feeling.
print("Hello! Let's check in on your mood today.")

# Store the user's input in a variable called 'feeling'.
# We convert the input to lowercase using '.lower()' for easier comparison later.
feeling = input("How are you feeling right now (e.g., happy, sad, tired, great)? ").lower()

# Now, we use 'if/elif/else' statements to respond based on their feeling.
# This introduces conditional logic: doing different things based on different conditions.

if "happy" in feeling or "great" in feeling or "good" in feeling:
    print("That's wonderful to hear! Keep that positive energy going!")
elif "sad" in feeling or "down" in feeling:
    print("I'm sorry to hear that. Remember, it's okay to feel sad, and things can get better.")
elif "tired" in feeling or "sleepy" in feeling:
    print("Sounds like you might need some rest. Take care of yourself!")
elif "okay" in feeling or "alright" in feeling or "fine" in feeling:
    print("Okay, sometimes 'okay' is just right. Hope your day improves!")
else:
    # If the feeling doesn't match any of our specific conditions.
    print("Thanks for sharing! Whatever you're feeling, acknowledge it and be kind to yourself.")

# A final message to end the script.
print("Have a great rest of your day!")

# This script demonstrates:
# - Printing text to the console.
# - Taking user input.
# - Storing data in variables.
# - Using basic conditional logic (if/elif/else).
# - String methods (like .lower() and 'in' for checking substrings).
```
