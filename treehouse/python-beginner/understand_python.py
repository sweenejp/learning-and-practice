name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
response = input("Hello, {}! Do you understand while loops in Python? \nEnter yes/no ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
while response.lower() != "yes":
    # TODO: Since the user doesn't understand while loops, let's explain them.
    print("While loops are blah blah blah blah blah")
    # TODO: Ask the user again, by name, if they understand while loops.
    response = input("{}, now do you understand? ".format(name))

# TODO: Outside the while loop, congratulate the user for understanding while loops
print("That's great! I'm glad you understand!")