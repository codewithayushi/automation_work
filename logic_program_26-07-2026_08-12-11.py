```python
import random # The 'random' module is used to pick a random item from a list.

# --- Define lists of words/phrases ---
# These lists will be used to construct unique sentences.
# You can add more options to each list!
subjects = ["The curious cat", "A wise old owl", "My best friend", "A tiny robot", "The bright sun"]
verbs = ["runs quickly", "sings softly", "explores bravely", "shines brightly", "dreams vividly"]
adjectives = ["magical", "sparkling", "mysterious", "joyful", "serene"]
nouns = ["forest", "mountain", "river", "castle", "garden"]
adverbs = ["gently", "happily", "silently", "forever", "surprisingly"]

# --- User Interaction ---
print("--- Your Unique Sentence Generator ---")
# Ask the user for a single word to personalize the sentence.
user_word = input("Enter a word you like (e.g., 'adventure', 'chocolate', 'star'): ").strip()

# --- Generate the sentence ---
# We'll pick one random item from each list.
# random.choice() picks a random element from a given list.
chosen_subject = random.choice(subjects)
chosen_verb = random.choice(verbs)
chosen_adjective = random.choice(adjectives)
chosen_noun = random.choice(nouns)
chosen_adverb = random.choice(adverbs)

# Combine all the chosen words, including the user's word, into a unique sentence.
# We use an f-string (formatted string literal) to easily insert variables into the string.
# The .capitalize() method makes sure the first letter of the sentence is uppercase.
generated_sentence = (
    f"{chosen_subject} {chosen_adverb} {chosen_verb} "
    f"in the {chosen_adjective} {chosen_noun}, thinking about {user_word}."
).capitalize()

# --- Display the result ---
print("\nHere's your unique sentence:")
print("✨ " + generated_sentence)
print("\n--- Enjoy your creativity! ---")
```
