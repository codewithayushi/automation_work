```python
# Import the 'random' module to use its functions for picking random items
import random

# Create a list of different animal names
animals = [
    "Lion",
    "Elephant",
    "Giraffe",
    "Penguin",
    "Dolphin",
    "Kangaroo",
    "Octopus"
]

# Pick one random animal name from the 'animals' list
chosen_animal = random.choice(animals)

# Display a fun message and the randomly chosen animal
print("Welcome to the Animal Picker 3000!")
print(f"Your random animal of the day is: {chosen_animal}!")

# You can also see the entire list of animals, sorted alphabetically
# The '.sort()' method changes the list directly (in-place)
animals.sort()
print("\n---") # Just a separator line for better readability
print("Here's the full list of animals, now sorted alphabetically:")
print(animals) # Print the entire sorted list
```
