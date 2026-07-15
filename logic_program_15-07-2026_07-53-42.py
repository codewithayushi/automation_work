```python
# This script creates a simple "Personalized Greeter" that remembers your name!
# It's a fun way to see how you can store and use information in Python.

def personalized_greeter():
    """
    Greets the user, asks for their name, and then offers a personalized message.
    It "remembers" the name for subsequent greetings within the same run.
    """

    # We use a variable to store the user's name.
    # Initialize it to None, meaning we don't have a name yet.
    user_name = None

    # This loop will keep the greeter running until the user decides to exit.
    # A 'while True' loop runs indefinitely until a 'break' statement is hit.
    while True:
        # Check if we already know the user's name.
        if user_name is None:
            # If not, ask for their name using the input() function.
            # input() gets text from the user and stores it in 'user_name'.
            user_name = input("Hello there! What's your name? ")
            print(f"Nice to meet you, {user_name}!") # f-strings are a neat way to embed variables in strings.
        else:
            # If we already have a name, offer a personalized greeting.
            print(f"Welcome back, {user_name}! It's great to see you again.")

        # Ask the user what they want to do next.
        # We convert the input to lowercase to make checking easier.
        action = input("Type 'greet' to say hello again, or 'exit' to quit: ").lower()

        # Check the user's input to decide the next action.
        if action == "greet":
            # If they want to greet again, the loop will simply repeat.
            # The 'user_name' is still stored, so it will use the personalized message.
            continue # 'continue' skips the rest of the current loop iteration and goes to the next.
        elif action == "exit":
            # If they want to exit, print a goodbye message and break the loop.
            print(f"Goodbye for now, {user_name}! Have a great day!")
            break # 'break' exits the loop immediately.
        else:
            # Handle invalid input gracefully.
            print("Sorry, I didn't understand that. Please type 'greet' or 'exit'.")

# This is a common Python construct. It ensures that 'personalized_greeter()'
# is called only when the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    personalized_greeter()
```
