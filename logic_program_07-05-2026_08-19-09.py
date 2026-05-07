```python
# This script creates a simple "Word Stretcher" that repeats each letter
# of a word based on its position in the word.

# 1. Ask the user to input a word.
# The input() function displays a message and waits for the user to type something.
# Whatever the user types is stored in the 'user_word' variable as a string.
user_word = input("Enter a word: ")

# 2. Initialize an empty string to store our stretched word.
# We'll build up this string character by character.
stretched_word = ""

# 3. Loop through each character in the 'user_word'.
# The 'enumerate()' function gives us both the index (position) and the character itself.
# The index 'i' will start from 0 for the first letter, 1 for the second, and so on.
for i, char in enumerate(user_word):
    # 4. Determine how many times to repeat the current character.
    # We want to repeat it 'index + 1' times.
    # For the first character (index 0), it repeats 1 time.
    # For the second character (index 1), it repeats 2 times.
    # And so on.
    repeat_count = i + 1

    # 5. Repeat the character and append it to our 'stretched_word'.
    # The string multiplication operator (*) repeats a string.
    # Example: 'a' * 3 results in 'aaa'.
    stretched_word += char * repeat_count

# 6. Print the final stretched word.
print(f"Your stretched word: {stretched_word}")

# Example if you enter "Hello":
# H (index 0) -> H * (0+1) = H
# e (index 1) -> e * (1+1) = ee
# l (index 2) -> l * (2+1) = lll
# l (index 3) -> l * (3+1) = llll
# o (index 4) -> o * (4+1) = ooooo
# Output will be: Heeellllllooooo
```
