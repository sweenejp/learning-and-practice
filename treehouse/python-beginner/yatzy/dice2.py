import random


class Die:
    def __init__(self, sides=2):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.outcome = random.randint(1, sides)


d = Die(10)
print(d.outcome)