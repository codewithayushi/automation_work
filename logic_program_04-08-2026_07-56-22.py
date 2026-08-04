```python
import random # We need the 'random' module to pick a random item from a list.

# --- Tiny Decision Helper ---
# This script helps you make a small decision by picking one option from a list you provide.

print("--- Tiny Decision Helper ---")
print("Enter options one by one. Type 'done' when you have no more options.")

choices = [] # This is an empty list where we will store all your options.

# This loop will keep asking for options until you type 'done'.
while True:
    # Ask the user for an option, showing them which number option they are entering.
    user_input = input(f"Option #{len(choices) + 1} (or 'done'): ") 
    
    # Check if the user wants to stop. We convert to lowercase to accept 'Done', 'DONE', etc.
    if user_input.lower() == 'done':
        break # Exit the loop if 'done' is entered.
    elif user_input.strip(): # Check if the input is not just empty spaces.
        choices.append(user_input.strip()) # Add the cleaned-up option to our list.

# After collecting options, let's make a decision.
if choices: # Check if the 'choices' list actually has options in it.
    final_choice = random.choice(choices) # Pick one random item from the list.
    print("\n------------------------------")
    print("Here is your chosen option:")
    print(f"👉 {final_choice} 👈") # Display the randomly picked option using an f-string.
    print("------------------------------")
else:
    print("\nYou didn't provide any options for me to choose from!")

print("\n--- End of Tiny Decision Helper ---")
```
