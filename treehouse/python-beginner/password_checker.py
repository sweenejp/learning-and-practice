#while loops. Good for looping when you aren't sure how many iterations the loop will last.

import sys

#style note - all caps indicates that this variable will remain constant while the program is running
MASTER_PASSWORD = 'opensesame'

password = input("Please enter the password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        # sys.exit stops a program from running
        sys.exit("Too many invalid password attempts")
    password = input('Invalid password, try again: ')
    attempt_count += 1
print("Welcome to secret town")