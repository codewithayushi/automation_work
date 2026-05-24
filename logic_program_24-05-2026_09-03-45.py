```python
# A simple "Mood Tracker" using emojis!

# Get a number from the user representing their mood (1-5)
# input() reads text, int() converts it to a whole number for calculations
user_mood_rating_str = input("How are you feeling today on a scale of 1 to 5? (1=Bad, 5=Great): ")
user_mood_rating = int(user_mood_rating_str)

# A list of emojis, where the position (index) corresponds to the mood rating (minus 1)
# Index 0 for mood 1, Index 1 for mood 2, etc.
emoji_moods = ["😔", "😕", "😐", "🙂", "😄"]

# Check if the entered rating is within our valid range
if 1 <= user_mood_rating <= 5:
    # Calculate the correct index: lists start at 0, so a mood of 1 is at index 0
    selected_emoji = emoji_moods[user_mood_rating - 1]

    # Print the result using an f-string (formatted string literal)
    print(f"\nYour mood today: {selected_emoji}")
    print("Thanks for checking in!")
else:
    # Handle cases where the user input is outside the 1-5 range
    print("\nOops! Please enter a number between 1 and 5.")
    print("Let's try again next time!")
```
