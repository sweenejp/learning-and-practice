# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require
# the solution in a different way. Take two lists and write a program that returns a list that
# contains only the elements that are common between the lists (without duplicates). Make sure
# your program works on two lists of different sizes. Write this using at
# least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

import random


def random_list(list_length, value_range):
    a = []
    for _ in range(list_length):
        a.append(random.randint(0, value_range))
    a.sort()
    return a


first = random_list(10, 10)
second = random_list(10, 10)
print(first)
print(second)
# remove duplicates from the lists
first = list(dict.fromkeys(first))
second = list(dict.fromkeys(second))
print("**********")
print(first)
print(second)

third = [item for item in first if item in second]

print("**********")
print(third)
