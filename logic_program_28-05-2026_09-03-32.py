```python
# This script takes your name, makes it "shouty", and then reverses it!

# 1. Ask the user for their name.
user_name = input("Hello! What's your name? ")

# 2. Make the name "shouty" (convert to uppercase).
shouty_name = user_name.upper()

# 3. Reverse the name.
# Python allows slicing a string with [start:end:step].
# A step of -1 reverses the string.
reversed_name = user_name[::-1]

# 4. Print out the results.
print(f"\nNice to meet you, {user_name}!")
print(f"In a very loud voice, your name is: {shouty_name}!!!")
print(f"And backwards, your name is: {reversed_name}")

# This is the end of our small script.
print("\nKeep learning Python!")
```
