```python
# This script is a fun "Mood Ring" that gives you a color and a short message
# based on a number you choose, from 1 to 5.
# It's a great way to learn about input, conditions (if/elif/else), and basic output!

# First, we greet the user and explain what the script does.
print("Welcome to the Python Mood Ring!")
print("Enter a number between 1 and 5, and I'll tell you your mood color and a message.")
print("Let's see what today holds for you!\n")

# We use a loop to make sure the user enters a valid number.
# 'while True' means this loop will run forever until we explicitly 'break' out of it.
while True:
    # Get input from the user. input() always returns a string.
    user_input = input("Enter your magic number (1-5): ")

    # We use a 'try-except' block to handle potential errors.
    # What if the user types text instead of a number?
    try:
        # Convert the user's input string into an integer (a whole number).
        mood_number = int(user_input)

        # Now, we check if the number is within our desired range (1 to 5).
        if 1 <= mood_number <= 5:
            # If the number is valid, we can exit the loop.
            break
        else:
            # If the number is not between 1 and 5, we tell the user.
            print("That number is out of range! Please choose between 1 and 5.")
    except ValueError:
        # If int(user_input) fails (e.g., user typed "hello"), a ValueError occurs.
        print("That's not a valid number! Please enter a whole number.")

# Once a valid number is received, we determine the "mood."
print(f"\nYour magic number is: {mood_number}")

# Now, we use 'if', 'elif' (else if), and 'else' statements
# to assign a color and a message based on the 'mood_number'.

if mood_number == 1:
    mood_color = "Red"
    message = "You are passionate and energetic! Tackle today with zeal."
elif mood_number == 2:
    mood_color = "Blue"
    message = "You are calm and peaceful. Find serenity in your tasks."
elif mood_number == 3:
    mood_color = "Green"
    message = "You are balanced and growing. Nurture your ideas."
elif mood_number == 4:
    mood_color = "Yellow"
    message = "You are joyful and optimistic! Share your light with others."
else:  # This will catch mood_number == 5
    mood_color = "Purple"
    message = "You are wise and imaginative. Let your creativity flow!"

# Finally, we print out the results using an f-string for easy formatting.
print(f"Your mood color is: {mood_color}")
print(f"Your message for today: {message}")

print("\nThanks for trying the Python Mood Ring!")
# The script ends here.
```
