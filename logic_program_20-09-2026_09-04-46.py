```python
# A simple script to create an expanding and contracting text pattern.

# Ask the user to enter a short word or phrase.
# The input() function gets text from the user.
user_text = input("Enter a short word (e.g., PYTHON): ")

# Print a header for the first part of the pattern.
print("\n--- Expanding Pattern ---")

# Loop through the length of the user's text.
# The 'range(len(user_text))' generates numbers from 0 up to (length - 1).
for i in range(len(user_text)):
    # Use string slicing to get a portion of the text.
    # user_text[0:i+1] means: start from index 0, go up to (but not including) index i+1.
    # This effectively prints one more character each time the loop runs.
    print(user_text[0:i+1])

# Print a header for the second part of the pattern.
print("\n--- Contracting Pattern ---")

# Loop again, this time to contract the pattern.
# 'range(len(user_text) - 1, 0, -1)' generates numbers:
# from (length - 1) down to 1 (the '0' is exclusive, so it stops before 0).
# The '-1' is the step, meaning it counts downwards.
for i in range(len(user_text) - 1, 0, -1):
    # Slice the string again.
    # user_text[0:i] means: start from index 0, go up to (but not including) index i.
    # This effectively prints one fewer character each time, until only the first char remains.
    print(user_text[0:i])

# Print a final message to the user.
print("\nPattern complete! Thanks for trying.")
```
