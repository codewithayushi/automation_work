```python
# This script creates a simple "bouncing" animation in your console.
# It makes a character move back and forth across the screen.

import time # We need the 'time' module to pause the script.

# --- Configuration for our animation ---
character_to_animate = ">" # The character we want to move.
screen_width = 30           # How wide our "screen" is (number of spaces).
animation_speed = 0.05      # How fast it moves (smaller number means faster).

# --- Variables to control the animation ---
current_position = 0 # Where our character currently is, starting at the left.
direction = 1        # 1 means moving right, -1 means moving left.

# --- The main animation loop ---
# This loop will run forever, creating a continuous animation.
while True:
    # 1. Create the string to print.
    #    It's spaces before the character, then the character, then spaces after.
    leading_spaces = " " * current_position
    trailing_spaces = " " * (screen_width - 1 - current_position) # -1 for the character itself.

    # Combine them to form the line we will print.
    line_to_print = leading_spaces + character_to_animate + trailing_spaces

    # 2. Print the line.
    #    The 'end='\r' makes the cursor return to the beginning of the line,
    #    so the next print statement overwrites the current one, creating the animation effect.
    print(line_to_print, end='\r')

    # 3. Update the character's position for the next frame.
    current_position += direction

    # 4. Check if we hit the "edges" of our screen.
    if current_position >= screen_width - 1 or current_position <= 0:
        # If we hit an edge, reverse the direction.
        direction *= -1 # This multiplies direction by -1, so 1 becomes -1, and -1 becomes 1.

    # 5. Pause for a short moment to control the animation speed.
    time.sleep(animation_speed)
```
