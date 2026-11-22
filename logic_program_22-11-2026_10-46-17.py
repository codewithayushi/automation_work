```python
import time
import sys
import random

# A list of fun, short messages to animate
messages = [
    "Hello, Pythonista!",
    "Coding is fun!",
    "Keep learning!",
    "You got this!",
    "Python rocks!",
    "Happy scripting!"
]

# Define how many times the animation loop should run
animation_cycles = 3

# Loop through the animation sequence a few times
for _ in range(animation_cycles):
    # Select a random message from our list for the current cycle
    current_message = random.choice(messages)

    # --- Type out the message character by character ---
    for char in current_message:
        sys.stdout.write(char) # Write a single character to the console
        sys.stdout.flush()     # Force the character to appear immediately
        time.sleep(0.1)        # Pause for a short duration (0.1 seconds)

    time.sleep(0.8)            # Pause a bit longer after the full message is typed

    # --- Erase the message by overwriting it with spaces ---
    # '\r' (carriage return) moves the cursor to the beginning of the current line
    # ' ' * len(current_message) creates a string of spaces equal to message length
    # Another '\r' moves the cursor back to the start, ready for the next message
    sys.stdout.write('\r' + ' ' * len(current_message) + '\r')
    sys.stdout.flush()
    time.sleep(0.2)            # Short pause before the next message or cycle

# After all animation cycles, display a final message slowly
final_greeting = "Animation complete! Have a great day!"
for char in final_greeting:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
sys.stdout.write('\n') # Move to a new line after the final message
sys.stdout.flush()
```
