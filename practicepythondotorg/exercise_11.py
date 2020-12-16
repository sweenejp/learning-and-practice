# Ask the user for a number and determine whether the number is prime or not. (For those who have
# forgotten, a prime number is a number that has no divisors.). You can (and should!) use your
# answer to Exercise 4 to help you. Take this opportunity to practice using functions, described
# below.


def prime_checker():
    num = int(input("What number would you like to check? "))
    divisors = []
    for item in range(2, num):
        if num % item == 0:
            divisors.append(item)
    if divisors:
        print("{} is not a prime number.".format(num))
    else:
        print("{} is a prime number.".format(num))


prime_checker()