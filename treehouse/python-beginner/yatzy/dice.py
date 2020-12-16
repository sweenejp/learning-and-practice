import random


class Die:
    def __init__(self, sides=2, outcome=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        # this was super confusing to me at first...
        # the outcome argument is set to 0 as a default. If you pass in something other than 0,
        # then outcome will be "false" (because 0 gets false in a boolean expression). If it is
        # false, then self.butt gets random.randint(1, sides)
        self.outcome = outcome or random.randint(1, sides)

    def __int__(self):
        return self.outcome

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.outcome)


class D6(Die):
    def __init__(self, outcome=0):
        super().__init__(sides=6, outcome=outcome)


class D20(Die):
    def __init__(self, outcome=0):
        super().__init__(sides=20, outcome=outcome)


a = D20()

print(a.outcome)

