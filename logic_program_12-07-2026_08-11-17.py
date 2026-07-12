```python
# This script tells a very short, personalized story!
# It will ask you for a few words and then combine them.

# First, we'll ask the user for their name using the input() function.
# The text inside input() is a prompt shown to the user.
# The value they type is stored in the 'name' variable.
name = input("What is your name? ")

# Next, we ask for an adjective (a describing word).
adjective = input("Give me an adjective (e.g., 'sleepy', 'shiny'): ")

# Then, we ask for a noun (a person, place, or thing).
noun = input("Now, give me a noun (e.g., 'cat', 'cloud', 'hat'): ")

# And finally, a verb (an action word).
verb = input("And a verb (e.g., 'jump', 'sing', 'fly'): ")

# Now, let's create our story!
# We use an f-string (formatted string literal) which starts with 'f'
# and allows us to embed variables directly inside curly braces {}.
story = f"\nOnce upon a time, a {adjective} {noun} saw {name} and decided to {verb} all the way to the moon!"

# Finally, we print the finished story to the console.
# The '\n' at the start of the story string creates a new line before the story.
print(story)

# You can run this script multiple times to create different stories!
```
