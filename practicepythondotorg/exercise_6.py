# Ask the user for a string and print out whether this string is a palindrome or not. (A
# palindrome is a string that reads the same forwards and backwards.)

user_input = input("Type a word! ")

if user_input[::-1].lower() == user_input.lower():
    print("{} is a palindrome!".format(user_input))
else:
    print("{} is not a palindrome :(".format(user_input))
