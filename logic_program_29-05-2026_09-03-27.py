```python
# Import the 'random' module to allow the script to make random choices
import random

# Greet the user and explain what the script does
print("Welcome to the Random Choice Selector!")
print("Enter items one by one, and I'll pick one for you.")
print("Type 'done' (without quotes) when you are finished adding items.")

# Create an empty list to store all the items the user will enter
items_to_choose_from = []

# Start a loop that will keep asking for items until the user types 'done'
while True:
    # Get input from the user for an item, and remove any extra spaces
    user_item = input("Enter an item: ").strip()

    # Check if the user has typed 'done' (case-insensitive)
    if user_item.lower() == 'done':
        break # Exit the loop if 'done' is entered

    # If the input is not empty, add it to our list of items
    if user_item:
        items_to_choose_from.append(user_item)
    else:
        # Inform the user if they entered an empty line
        print("Empty item not added. Please enter something or 'done'.")

# Check if there are any items in the list to choose from
if items_to_choose_from:
    # Use random.choice() to pick one item randomly from the list
    chosen_item = random.choice(items_to_choose_from)

    # Print the randomly selected item to the user
    print("\n--- Your Random Choice ---")
    print(f"The chosen item is: {chosen_item}") # Using an f-string for easy formatting
else:
    # If no items were entered, inform the user
    print("\nNo items were entered, so no choice could be made.")

print("\nThanks for using the Random Choice Selector!")
```
