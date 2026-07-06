```python
# Import the 'random' module to enable random selections
import random

# Greet the user and explain the script's purpose
print("Welcome to the 'Decision Dice'!")
print("I'll help you pick one thing from a list you give me.")

# Create an empty list to store all the options the user enters
options_list = []

# Start a loop to collect options from the user
# This loop will continue indefinitely until the user types 'done'
while True:
    # Ask the user for an option
    user_input = input("Enter an option (or type 'done' to finish): ")

    # Check if the user wants to stop adding options
    if user_input.lower() == 'done':
        break  # Exit the loop if 'done' is entered

    # If the input is not empty, add it to our list of options
    if user_input: # This checks if the string is not empty
        options_list.append(user_input)

# Check if the user actually entered any options
if not options_list:
    # If no options were entered, let the user know and end the script
    print("\nNo options were provided. I can't help you decide!")
else:
    # If there are options, randomly select one from the list
    chosen_one = random.choice(options_list)

    # Print the randomly chosen option to the user
    print("\nBased on your input, the 'Decision Dice' chooses:")
    print(f"🎲 {chosen_one} 🎲") # Using an f-string for clear output
    print("Good luck with your choice!")

```
