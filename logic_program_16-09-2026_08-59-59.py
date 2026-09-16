```python
import random

# This script generates a unique, imaginary animal name and its quirky habitat.

# A list of imaginative prefixes for animal names.
prefixes = ["Glimmer", "Sniffle", "Whisper", "Ponder", "Wobble", "Fizzle", "Quirk"]

# A list of fanciful suffixes for animal names.
suffixes = ["wing", "horn", "paws", "beak", "fin", "snout", "tail"]

# A list of odd habitats.
habitats = [
    "a cloud made of forgotten wishes",
    "the inside of a giant, sleeping teapot",
    "a forest where trees grow upside down",
    "the bottom of a rainbow's well",
    "a desert made entirely of sugar cubes",
    "the attic of a librarian's dream"
]

# Randomly select one prefix, one suffix, and one habitat.
chosen_prefix = random.choice(prefixes)
chosen_suffix = random.choice(suffixes)
chosen_habitat = random.choice(habitats)

# Combine them to create a unique animal name and description.
animal_name = f"{chosen_prefix}{chosen_suffix}"

# Print the generated imaginary creature and its home.
print("--- Discover Your Imaginary Creature! ---")
print(f"Behold! The magnificent {animal_name}!")
print(f"It makes its home in {chosen_habitat}.")
print("-----------------------------------------")
```
