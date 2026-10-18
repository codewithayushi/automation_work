```python
# This script creates a simple, repeating pattern using a word you provide.

# 1. Ask the user for a single word.
#    The input() function gets text from the user.
user_word = input("Enter a short word: ")

# 2. Print a decorative header line.
#    Multiplying a string repeats it.
print("=" * 30)

# 3. Use a loop to print the word in a pattern.
#    The 'range(5)' means the loop will run 5 times (for i=0, 1, 2, 3, 4).
for i in range(5):
    # 4. Use an 'if-else' statement to change the pattern based on the loop count.
    #    The modulo operator (%) gives the remainder of a division.
    #    If 'i % 2 == 0', it means 'i' is an even number (0, 2, 4).
    if i % 2 == 0:
        # F-strings (formatted string literals) are a modern way to embed variables.
        print(f"|-- {user_word.upper()} --|") # Print in uppercase with extra decoration
    else:
        # If 'i' is an odd number (1, 3).
        print(f"|   {user_word.lower()}   |") # Print in lowercase with different spacing

# 5. Print a decorative footer line.
print("=" * 30)

# 6. Offer a friendly message.
print("Hope you enjoyed your pattern!")
```
