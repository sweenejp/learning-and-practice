import random


class Die:

    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other


class D20(Die):
    def __init__(self):
        super().__init__(sides=20)


class Hand(list):
    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, size):
        new_hand = Hand()
        for _ in range(size):
            new_hand.append(D20())
        return new_hand


# ...This does not work:
new_butt = Hand()
new_butt.roll(2)
print(new_butt)
# ...because the list "new_butt" can't be acted on by the class method. The class method acts on
# the class

# Class Methods act on the class
butt = Hand.roll(2)

for item in butt:
    print(int(item))

# properties can act on the object (in this case, the list "butt"). So I can run the total method
# on the "butt" object since it is an object of the class "Hand"
print("The total is: ", butt.total)


# I can update the butt object by again calling Hand.roll(2)
butt = Hand.roll(2)
for item in butt:
    print(int(item))
print("The total is: ", butt.total)

final_butt = Hand()
final_butt.roll(2)
print(final_butt)
