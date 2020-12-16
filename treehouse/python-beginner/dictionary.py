course = {'teacher': 'Jimmy', 'title': 'Introducing Dictionaries', 'level': 'Beginner'}

print(course['teacher'])

print(course.keys())

print(course.values())

print(sorted(course.values()))

student = {'name': '', 'topic': 'python'}

course['teacher'] = 'Treasure'

print(course['teacher'])

course['stages'] = 2

course['butt_amount'] = 0

print(course)

del(course['butt_amount'])

print(course)

# iteration, packing, and unpacking

# print out all of the keys
for item in course:
    print(item)

# print out all of the values
for item in course:
    print(course[item])

# print out a list (?) of tuples where each element in the list is a tuple with two objects - first
# the key, then the value
print(course.items())

for key, value in course.items():
    print(f'{key}: {value}')


def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_teacher(name='Ashley', job='instructor', topic='Python', second_topic='butts')


teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}


def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)


print_teacher(**teacher)


teacher.v
