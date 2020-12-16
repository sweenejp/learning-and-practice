# Create a program that asks the user for a number and then prints out a list of all the divisors
# of that number. (If you don’t know what a divisor is, it is a number that divides evenly into
# another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

user_input = int(input("Please give me a number: "))
user_range = range(1, (user_input + 1))
divisors = []
for item in user_range:
    if user_input % item == 0:
        divisors.append(item)

print("The divisors of {} are: ".format(user_input))
print(divisors)


# interesting solution for from the comments on this page. However it doesn't actually work with
# small numbers
def divisify(x):
    divs =[]
    for i in range(1, int(x**.5)):
        if x % i == 0:
            divs.append(i)
            divs.append(x//i)
    divs.sort()
    print(divs)


divisify(user_input)

