```python
# Import the 'random' module to make choices randomly
import random

# Define a list of possible "sparkle words"
sparkle_words = [
    "Dazzle",
    "Glimmer",
    "Shine",
    "Radiate",
    "Twinkle",
    "Glow",
    "Illuminate"
]

# Define a list of simple "sparkle patterns" using characters
sparkle_patterns = [
    "  *  ",
    " * * ",
    "* * *",
    " * * ",
    "  *  "
], [
    " \\ | / ",
    "  - -  ",
    " / | \\ "
], [
    " ^ ^ ",
    "  v  ",
    " ^ ^ "
], [
    " /-\\ ",
    "<*-*>",
    " \\-/ "
]

# Randomly choose one sparkle word from the list
chosen_word = random.choice(sparkle_words)

# Randomly choose one sparkle pattern (which is a list of strings itself)
chosen_pattern = random.choice(sparkle_patterns)

# Print a header for our sparkle message
print("--- Your Moment of Sparkle! ---")

# Print each line of the chosen sparkle pattern
for line in chosen_pattern:
    print(line)

# Print the chosen sparkle word, centered below the pattern
# The len() of the longest line helps determine how much to indent
longest_line_len = max(len(line) for line in chosen_pattern)
print(f"{chosen_word:^{longest_line_len}}") # f-string for formatted output

# Print a footer
print("-----------------------------")
```
