```python
# Import the 'random' module to use its functions, like picking a random item.
import random

# Define a list of possible "fun facts" about Python.
# Lists are ordered collections of items, perfect for storing multiple options.
python_facts = [
    "Python was named after the British comedy group Monty Python, not the snake!",
    "Python's creator, Guido van Rossum, is known as the 'Benevolent Dictator For Life' (BDFL).",
    "Python uses indentation (whitespace) to define code blocks, unlike many languages that use curly braces.",
    "The Zen of Python is a set of guiding principles for Python's design, accessible via 'import this'.",
    "Python supports multiple programming paradigms, including object-oriented, imperative, and functional.",
    "The first version of Python was released in 1991.",
    "Python is often used for web development (Django, Flask), data science, AI, and automation.",
    "Python's package installer is called 'pip', which stands for 'Pip Installs Packages'.",
    "Python is an interpreted language, meaning code is executed line by line rather than fully compiled.",
    "Python's official mascot is two L-shaped blocks representing the indentation."
]

# Greet the user and ask them to press Enter.
# The input() function waits for user input.
print("Hello! Let's learn a fun Python fact.")
input("Press Enter to reveal a random Python fact: ")

# Use random.choice() to pick one fact randomly from our list.
# This function is great for selecting a single item from a sequence.
random_fact = random.choice(python_facts)

# Print the chosen fact to the console.
print("\n--- Your Python Fact ---") # The '\n' adds a blank line for better readability.
print(random_fact)
print("------------------------")

# End the script with a friendly message.
print("\nHope you learned something new!")
```
