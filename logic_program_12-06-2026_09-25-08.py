```python
# This script asks for your favorite animal and creates a unique "fun-factor" score!

# 1. We start by asking the user to type their favorite animal.
#    The input() function pauses the program and waits for the user's text.
favorite_animal = input("What is your favorite animal? ")

# 2. Next, we count how many letters are in the animal's name.
#    The len() function tells us the length of a string (text).
animal_name_length = len(favorite_animal)

# 3. Now, let's calculate a "fun-factor" score.
#    We'll multiply the name's length by a "magic number" (3) and add 5.
fun_factor_score = (animal_name_length * 3) + 5

# 4. We print out the calculated score for the user to see.
#    f-strings (formatted string literals) are a nice way to include variables in text.
print(f"\nYour animal's 'fun-factor' score is: {fun_factor_score}")

# 5. Finally, we give a little encouraging message based on the score.
#    This uses an 'if/else' statement, which lets our code make decisions.
if fun_factor_score > 20:
    print("Wow, that's a super fun animal! You must have great energy!")
else:
    print("A solid fun animal! A little quiet, but full of charm!")

# And that's it! A simple script combining text input, number calculations, and decisions.
```
