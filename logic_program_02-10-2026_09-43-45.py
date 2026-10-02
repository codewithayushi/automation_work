```python
# This script analyzes a sentence you type, focusing on words that start with vowels!

# First, we ask the user for a sentence.
# The input() function gets text from the user.
user_sentence = input("Please type a sentence: ")

# We want to count how many words start with a vowel.
vowel_starting_word_count = 0

# Define what a vowel is (case-insensitive).
vowels = "aeiou"

# Split the sentence into individual words.
# The split() method breaks a string by spaces by default.
words = user_sentence.split()

# Now, we'll go through each word one by one.
# This is called a 'for loop', which repeats actions for each item in a sequence.
for word in words:
    # Clean up the word a bit: remove punctuation like periods or commas.
    # We'll use a simple approach for common punctuation.
    cleaned_word = word.strip(".,!?;:").lower() # Convert to lowercase too for easy vowel check

    # Check if the cleaned word is not empty (e.g., if there were just punctuation marks).
    if cleaned_word:
        # Get the first letter of the word.
        first_letter = cleaned_word[0]

        # Check if the first letter is in our 'vowels' string.
        # The 'in' operator checks for membership.
        if first_letter in vowels:
            # If it is, increment our counter.
            vowel_starting_word_count += 1
            # You can also print the word if it starts with a vowel to see which ones:
            # print(f" - Found a vowel-starting word: '{cleaned_word}'")

# After checking all words, print the final count.
# An f-string (formatted string literal) allows embedding variables directly.
print(f"\nYour sentence has {len(words)} words in total.")
print(f"Out of these, {vowel_starting_word_count} words start with a vowel.")

print("\nThanks for using the Vowel Word Counter!")
```
