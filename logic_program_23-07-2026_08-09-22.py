# A simple script to create a customizable ASCII face!

print("Let's build a little ASCII face!")

# Get user input for eyes
# The user will choose a number corresponding to an eye style.
eye_choice = input("Choose eyes (1 for 'o o', 2 for '- -', 3 for 'x x'): ")

# Get user input for mouth
# The user will choose a number corresponding to a mouth style.
mouth_choice = input("Choose mouth (1 for 'u', 2 for 'o', 3 for '_'): ")

# Determine the eyes based on the user's choice.
# We use an 'if/elif/else' structure to handle different options.
eyes = "o o" # Default eyes if no valid choice is made
if eye_choice == '1':
    eyes = "o o"
elif eye_choice == '2':
    eyes = "- -"
elif eye_choice == '3':
    eyes = "x x"
else:
    print("Invalid eye choice, using default 'o o'.")

# Determine the mouth based on the user's choice.
mouth = "u" # Default mouth if no valid choice is made
if mouth_choice == '1':
    mouth = "u"
elif mouth_choice == '2':
    mouth = "o"
elif mouth_choice == '3':
    mouth = "_"
else:
    print("Invalid mouth choice, using default 'u'.")

# Print the final ASCII face using f-strings for easy formatting.
# F-strings allow us to embed variables directly into strings.
print("\nHere's your unique face:")
print("  -----  ") # Top of the face/head
print(f" | {eyes} | ") # Eyes line, with chosen eyes
print(f" |  {mouth}  | ") # Mouth line, with chosen mouth
print("  -----  ") # Bottom of the face/head
print("\nEnjoy your creation!")
