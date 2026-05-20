```python
# Import the time module to add pauses to our script
import time
# Import the sys module to force output to appear immediately
import sys

# Define a list of characters that will form our simple animation frames
animation_frames = ["-", "\\", "|", "/"]

# Set how many times the entire animation sequence should repeat
total_animation_cycles = 5

print("Starting a tiny loading animation...")

# Loop for the specified number of animation cycles
for cycle in range(total_animation_cycles):
    # Loop through each frame in our animation_frames list
    for frame in animation_frames:
        # Print the current frame
        # '\r' (carriage return) moves the cursor to the beginning of the current line
        # 'end=""' prevents print from adding a new line, so subsequent prints overwrite the same line
        print(f"\rLoading {frame}", end="")
        # Force the output buffer to display immediately, important for '\r' to work well
        sys.stdout.flush()
        # Pause the script for a short duration (0.1 seconds)
        time.sleep(0.1)

# After the animation finishes, print a final message on a new line
print("\nAnimation complete! Have a great day.")
```
