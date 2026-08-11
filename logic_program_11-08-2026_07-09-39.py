```python
import time
import random

# A list of fun emojis to "spin" through
spinning_emojis = ["😊", "😂", "👍", "🤔", "🥳", "✨", "🚀", "💡"]

# A list of positive "result" emojis to land on
lucky_emojis = ["🍀", "⭐", "🌈", "🎉", "💯", "✅", "🙌"]

print("--- Welcome to the Lucky Emoji Spinner! ---")
time.sleep(1)

print("\nSpinning the wheel...")
time.sleep(1)

# Simulate spinning by displaying emojis quickly on the same line
# The `end='\r'` makes the print overwrite the current line instead of moving to the next
for _ in range(15): # Spin 15 times quickly
    chosen_emoji = random.choice(spinning_emojis)
    print(f"  {chosen_emoji}  ", end='\r') # Print the emoji, then return cursor to start
    time.sleep(0.18) # Short pause

# Clear the spinning line by printing spaces, then reveal the final emoji
print("            ", end='\r') # Overwrite the last spinning emoji with spaces
final_emoji = random.choice(lucky_emojis)
print(f"Your lucky emoji is: {final_emoji}!")
print("Have a fantastic day!")
```
