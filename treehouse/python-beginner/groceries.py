groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food',]

index = 1
for item in groceries:
    print(f'{index}. {item}')
    index += 1

print("************************")
# enumerate does the above

for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')


print("************************")

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for index, color in enumerate(rainbow):
    print(index)
    print(color)

# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

# enumerate basically takes an iterable and creates a new variable for each object in the
# iterable. That new variable is assigned the index of the iterable. So basically it creates a
# list of tuples, each iterable in the tuple is the index followed by the original object.
for item in obj1:
    print(item)

for item in obj2:
    print(item)


# This is why you can pass in a tuple with two objects in a for loop with enumerate
new_list = ["butts", "chicken", "parrots"]
obj3 = enumerate(new_list)

for index, item in obj3:
    print(index, item)


# ranges
numbers = []
for number in range(10):
    numbers.append(number)


print(numbers)


numbers = []
for number in range(1, 100, 5):
    numbers.append(number)


print(numbers)


