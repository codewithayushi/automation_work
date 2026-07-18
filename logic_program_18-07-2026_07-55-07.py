```python
# This script generates a simple, personalized "fortune" message.
# It's a fun way to see how Python can combine user input into text!

# First, we ask the user for a few pieces of information.
# The 'input()' function waits for the user to type something and press Enter.
# Whatever they type is stored in the variable on the left (e.g., 'name').
name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
lucky_number = input("What is your lucky number? ")

# Now, we'll combine these inputs into a single message.
# We use an f-string (formatted string literal) for easy text formatting.
# Just put 'f' before the opening quote, and place variables inside curly braces {}.
fortune_message = f"Hello, {name}! Your future shines as bright as your favorite color, {favorite_color}. " \
                  f"Remember, a stroke of luck awaits you, especially around the number {lucky_number}!"

# Finally, we display the generated message to the user using the 'print()' function.
print("\n--- Your Personalized Fortune ---") # A small header for readability
print(fortune_message)
print("---------------------------------")

# You can run this script, enter your details, and see your unique fortune!
```
