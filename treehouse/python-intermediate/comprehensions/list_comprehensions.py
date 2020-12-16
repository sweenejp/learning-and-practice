nums = range(5, 101)

halves = [num/2 for num in nums]


# conditionals
fizzes = [num for num in range(1, 101) if num % 3 == 0]
buzzes = [num for num in range(1, 101) if num % 7 == 0]

# multiple for loops
rows = range(4)
columns = range(10)
table = [(x, y) for y in rows for x in columns]
print(table)

# loops the same way it would with a for loop inside a for loop
example = [(letter, number) for number in range(5) for letter in "abc"]
print(example)

# dictionaries
students = {student: points for student, points in zip(["Jimmy", "Noah", "Grayson", "Marc"],
                                                       [12, 0, 5, 10])}
print(students)

total_nums = range(1, 101)
fizzbuzzes = {
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz': [n for n in total_nums if n % 7 == 0]
}

fizzbuzzes = {key: set(value) for key, value in fizzbuzzes.items()}
fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz'])}

print(fizzbuzzes)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print([n for n in fizzbuzzes])
