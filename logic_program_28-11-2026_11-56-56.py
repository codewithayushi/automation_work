```python
# Import the 'random' module to allow choosing random items from a list
import random

# Define a list of possible magical ingredients
ingredients = ["dragon's scale", "unicorn tear", "phoenix feather", "griffin claw", "elf dust", "goblin snot"]

# Define a list of possible effects for a potion
effects = ["invisibility", "super strength", "flight", "luck", "mind-reading", "glowing skin"]

# Define a list of possible container types
containers = ["a chipped cauldron", "a sparkling vial", "an ancient goblet", "a humble flask", "a crystal phial"]

# Randomly pick one ingredient from the 'ingredients' list
chosen_ingredient = random.choice(ingredients)

# Randomly pick one effect from the 'effects' list
chosen_effect = random.choice(effects)

# Randomly pick one container from the 'containers' list
chosen_container = random.choice(containers)

# Print the recipe for a unique potion using an f-string (formatted string literal)
# f-strings make it easy to embed variables directly into strings
print(f"To brew a potion of {chosen_effect}:")
print(f"Combine one {chosen_ingredient} in {chosen_container}.")
print("Stir clockwise three times under a full moon!")

# Every time you run this script, you'll get a different, unique potion recipe!
```
