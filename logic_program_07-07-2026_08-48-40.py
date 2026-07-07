```python
# This simple script draws a dynamic, repeating pattern based on user input!

# First, we ask the user for a single character to use in their pattern.
# The 'input()' function waits for the user to type something and press Enter.
pattern_character = input("Enter a single character for your pattern (e.g., * or #): ")

# Next, we ask how many times that character should repeat in a single line.
# We convert the user's text input to a whole number using 'int()'.
line_length_str = input("How many times should the character repeat in a line? (e.g., 5): ")
line_length = int(line_length_str)

# Then, we ask how many lines of this pattern the user wants to see.
num_lines_str = input("How many lines of this pattern should we draw? (e.g., 3): ")
num_lines = int(num_lines_str)

# Now, let's create and print the pattern!
print("\nHere's your custom pattern:")

# We use a 'for' loop to repeat the pattern drawing 'num_lines' times.
# The '_' is a common convention when we don't need to use the loop counter itself.
for _ in range(num_lines):
    # Inside the loop, we create one line of the pattern.
    # Multiplying a string by an integer repeats the string.
    single_pattern_line = pattern_character * line_length
    # Then we print that completed line.
    print(single_pattern_line)

# A final message to the user!
print("\nPattern drawing complete! Hope you liked it!")
```
