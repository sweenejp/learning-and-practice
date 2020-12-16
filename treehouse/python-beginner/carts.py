def calculate_total(*args):
    total = sum(args)
    print(total)


calculate_total(24, 70, 80, 90, 10, 10)


def packer(*args):
    lis = []
    for arg in args:
        lis.append(arg)
    print(lis)


packer("buttons", "chickens", 1.6)


def packer2(*items):
    for arg in items:
        print(arg)


packer2(1, 15.7, -11, "butts")

print("*******************************")


def unpacker():
    return 1, 3, "hey you butt head"


var1, var2, var3 = unpacker()

print(var1)
print(var2)
print(var3)


first, last = input('Enter your full name: \n').split(" ")

print(first)
print(last)
