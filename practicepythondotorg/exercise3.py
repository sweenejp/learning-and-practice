source = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_input = int(input("Please enter a number: "))

list_b = []

for item in source:
    if item < user_input:
        list_b.append(item)

print(list_b)

# using filter and lambda (?)
print(list(filter(lambda x: (x < user_input), source)))

# list comprehensions (?)
list_c = []
[list_c.append(x) for x in source if x < user_input]
print(list_b)
