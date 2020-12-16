rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'bluybluy']

print(rainbow[1:4])

print(rainbow[3:])

print(rainbow[::2])

print(rainbow[::-1])

print(rainbow[0:8:2])

print(min(rainbow))

print(max(rainbow))

print(len(rainbow))

docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

# in operator
if 'tuple' in docs:
    print('yes')

# not in operator

if 'tuple' not in docs:
    print('no')

print(docs.count("tuple"))
print(docs.index("tuple"))

nums = range(1, 10, 2)
for item in nums:
    print(item)

print(nums.index(5))

object1 = [1, 2, 3, 4, 5]
object2 = [6, 7, 8, 9, 10]

object1 = object1 + object2
print(object1)

object1 = (1, 2, 3, 4, 5)
object2 = (6, 7, 8, 9, 10)

object1 = object1 + object2
print(object1)

print(object1 * 5)