```python
# This script slowly reveals a "secret" word, letter by letter, with a dramatic pause.
# It's a great way to learn about variables, strings, loops, and time delays!

# --- Configuration Section ---
# 1. Set your secret word here.
#    Try changing "PYTHON" to your name, a favorite animal, or a short phrase!
secret_word = "BEGINNER"

# 2. Set the delay between revealing each letter (in seconds).
#    A value of 0.5 means half a second. Try changing it to 0.1 (faster) or 1.0 (slower)!
import time # This line imports the 'time' module, which lets us pause the script.
reveal_delay_seconds = 0.4

# --- Script Logic Starts Here ---
print("Get ready! A mysterious word is about to be revealed...\n")

# A separator line for visual effect.
print("------------------------------")

# Loop through each position in the 'secret_word'.
# 'index' will start at 0 (for the first letter), then 1, 2, and so on,
# up to the length of the word minus 1.
for index in range(len(secret_word)):
    # 'String slicing' allows us to take a part of a string.
    # secret_word[0 : index + 1] means:
    # - Start from the very beginning of the string (position 0).
    # - Go up to, but *not including*, the character at 'index + 1'.
    #   For example:
    #   - If index is 0, it takes secret_word[0:1], revealing just the first letter.
    #   - If index is 1, it takes secret_word[0:2], revealing the first two letters.
    #   ...and so on, gradually revealing more of the word.
    revealed_part = secret_word[0 : index + 1]

    # Print the part of the word that has been revealed so far.
    print(revealed_part)

    # Pause the script for the specified delay.
    time.sleep(reveal_delay_seconds)

# Another separator line.
print("------------------------------")

# After the loop finishes, the entire word has been revealed.
# An f-string (formatted string literal) is used here to easily embed the variable's value.
print(f"\nThe full secret word is: {secret_word}!")
print("Congratulations! You've revealed the mystery!")
```
