```python
# This script creates a simple "digital pet" that you can feed.
# It demonstrates variables, input, loops, and conditional statements.

# Start with a happy pet and some food.
pet_mood = "happy"
food_in_bowl = 3 # Represents how many "servings" of food are left.

# Greet the user and show the initial status.
print("Hello! Your digital pet is here.")
print(f"Current mood: {pet_mood}")
print(f"Food left: {food_in_bowl} servings")
print("-" * 20) # Prints a line for separation.

# Start a loop so you can interact multiple times.
# The loop continues as long as there is food available.
while food_in_bowl > 0:
    # Ask the user for input.
    user_action = input("Type 'feed' to feed your pet (or 'quit' to exit): ").lower()

    # Check the user's input using an 'if-elif-else' structure.
    if user_action == "feed":
        # If the user chose to feed, decrease the food count.
        food_in_bowl -= 1 # This is shorthand for food_in_bowl = food_in_bowl - 1
        pet_mood = "very happy!" # Pet's mood improves!

        # Print the updated status.
        print(f"You fed your pet! Pet is now {pet_mood}")
        print(f"Food left: {food_in_bowl} servings")
        print("-" * 20)

    elif user_action == "quit":
        # If the user wants to quit, break out of the loop.
        print("Goodbye! Thanks for playing with your pet.")
        break # This command exits the 'while' loop immediately.

    else:
        # Handle unrecognized commands.
        print("Sorry, I don't understand that command. Please try 'feed' or 'quit'.")
        print("-" * 20)

# This code runs after the loop finishes (either by running out of food or quitting).
if food_in_bowl == 0:
    print("Oh no! You've run out of food.")
    print("Your pet looks a bit hungry now. Time to get more food!")
    pet_mood = "hungry"
    print(f"Current mood: {pet_mood}")

print("Script finished. Have a great day!")
```
