# Write a program (function!) that takes a list and returns a new list that contains all the
# elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list,
# and another using sets. Go back and do Exercise 5 using sets, and write the solution for that
# in a different function.


def remove_duplicates(x):
    return list(set(x))


def other_remove_duplicates(x):
    a_list = []
    for item in x:
        if item not in a_list:
            a_list.append(item)
    return a_list


print(remove_duplicates([1, 1, 3, 5, 6, 7, 7, 7, 10]))
print(other_remove_duplicates([1, 1, 3, 5, 6, 7, 7, 7, 10]))
