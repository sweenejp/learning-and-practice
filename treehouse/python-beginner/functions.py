def add_two_nums(num1, num2):
    #print(num1, "+", num2, "=")
    val = num1 + num2
    print(val)
    return val


add_two_nums(1, 1)

for butts in range(10):
    print(butts)


# def hello_student(name):
#     return "Hello {}".format(name)

# ^same result as above
def hello_student(name):
    return "Hello " + name


print(hello_student("Ashley"))
