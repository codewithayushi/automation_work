```python
# This script helps you decide what to watch from a list of options!
import random # We need the 'random' module to pick a movie/show randomly.

print("Let's list some movies or shows you could watch. Type 'done' when finished.")

watchlist = [] # This is an empty list where we'll store your viewing ideas.

# This 'while True' loop will keep asking for input until you type 'done'.
while True:
    # The 'input()' function waits for you to type something and press Enter.
    item = input("Add a movie/show to your watchlist (or type 'done'): ")

    # '.lower()' converts the input to lowercase, so 'Done', 'DONE', and 'done' all work.
    if item.lower() == 'done':
        break # This 'break' statement stops the 'while True' loop.
    elif item.strip(): # '.strip()' removes leading/trailing spaces; ensures input isn't just spaces.
        watchlist.append(item.strip()) # '.append()' adds the new item to our list.

print("\n--- Time to Pick! ---") # A separator for better readability.

# Now, let's check if the 'watchlist' actually has any items.
if not watchlist: # 'not watchlist' is True if the list is empty.
    print("Your watchlist is empty! Time to find some new content.")
else:
    # 'random.choice()' picks one item randomly from our 'watchlist' list.
    chosen_item = random.choice(watchlist)

    # An f-string (formatted string literal) lets us easily put variables into text.
    print(f"You should watch: {chosen_item}!")
    print("Enjoy your viewing!")

# End of script!
```
