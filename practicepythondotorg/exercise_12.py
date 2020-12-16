# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a
# new list of only the first and last elements of the given list. For practice, write this code
# inside a function.

a = [5, 10, 15, 20, 25]


def first_and_last(x):
    new_list = [x[0], x[-1]]
    return new_list


print(first_and_last(a))

