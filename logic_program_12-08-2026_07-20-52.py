```python
import time # Import the time module to pause execution

# Ask the user to enter a short word
user_word = input("Enter a short word: ")

# Define the maximum length for our "stretch" effect
max_stretch = 15

print("\n--- Stretching ---")
# Loop from 1 up to max_stretch to make the word appear to "grow"
for i in range(1, max_stretch + 1):
    # Create a string by repeating a hyphen 'i' times
    # Then add the user's word, and repeat the hyphen again
    stretched_line = "-" * i + user_word + "-" * i
    
    # Print the stretched line
    print(stretched_line)
    
    # Pause for a brief moment to create an animation effect
    time.sleep(0.08) # 0.08 seconds

print("\n--- Shrinking ---")
# Loop from max_stretch down to 1 to make the word appear to "shrink"
# The range function goes from max_stretch, down to 1 (exclusive), with a step of -1
for i in range(max_stretch, 0, -1):
    # Create the stretched line similar to the growing phase
    stretched_line = "-" * i + user_word + "-" * i
    
    # Print the shrinking line
    print(stretched_line)
    
    # Pause for a brief moment
    time.sleep(0.08)

print("\nAnimation complete!") # Inform the user the script has finished
```
