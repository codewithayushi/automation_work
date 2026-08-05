```python
import random # The 'random' module is used here to shuffle items in a list.

def scramble_word(word):
    """
    Scrambles the letters within a single word, keeping the first and last
    letters in their original positions. Short words (2 letters or less)
    are returned unchanged to avoid issues and maintain readability.
    """
    if len(word) <= 2:
        return word # No scrambling needed for very short words

    first_letter = word[0]       # Get the very first letter of the word.
    last_letter = word[-1]       # Get the very last letter of the word.
    
    # Extract the letters that are in between the first and last.
    # We convert them to a list because string characters cannot be shuffled directly.
    middle_letters = list(word[1:-1]) 
    
    random.shuffle(middle_letters) # Randomly reorder the letters in the 'middle_letters' list.
    
    # Join the shuffled middle letters back into a single string.
    scrambled_middle = "".join(middle_letters)
    
    # Combine the first letter, the scrambled middle, and the last letter
    # to form the newly scrambled word.
    return first_letter + scrambled_middle + last_letter

# --- Main part of the script starts here ---

# Prompt the user to enter a sentence.
original_sentence = input("Enter a sentence you'd like to see scrambled: ")

# Split the input sentence into individual words.
# The .split() method by default splits at any whitespace and handles multiple spaces.
words = original_sentence.split()

# Create an empty list to store the words after they have been scrambled.
scrambled_words = []

# Loop through each word in the list of original words.
for word in words:
    # Call our 'scramble_word' function for the current word.
    # Then, add the resulting scrambled word to our 'scrambled_words' list.
    scrambled_words.append(scramble_word(word))

# Join all the scrambled words back together to form a complete sentence.
# We use a single space " " as the separator between each word.
final_scrambled_sentence = " ".join(scrambled_words)

# Print the original sentence for comparison (optional, but nice for beginners).
print(f"\nOriginal sentence: '{original_sentence}'")

# Display the final scrambled sentence to the user.
print(f"Scrambled sentence: '{final_scrambled_sentence}'")
```
