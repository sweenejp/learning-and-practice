# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use
# the user input lessons from the very first exercise)

import random

print("Type 'quit' to exit")

while True:
    secret_number = random.randint(1, 9)
    user_input = input("Guess a number! ")
    print("**{}**".format(secret_number))
    if user_input == "quit":
        break
    else:
        user_input = int(user_input)
        while user_input != secret_number:
            if user_input < secret_number:
                user_input = int(input("You guessed too low! Guess again! "))
            elif user_input > secret_number:
                user_input = int(input("You guessed too high! Guess again! "))
        print("Nailed it!")
        user_input = input("Play again? Y/N: ")
        if user_input.lower() == "n":
            break

