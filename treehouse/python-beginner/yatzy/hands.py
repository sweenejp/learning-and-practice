import yatzy.dice


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        # create instances of the die_class
        for _ in range(size):
            self.append(die_class())
        self.sort()
        self.total = sum(self)

    def _by_outcome(self, outcome):
        dice = []
        for die in self:
            if die == outcome:
                dice.append(die)
        return dice


class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=yatzy.dice.D6, *args, **kwargs)

    @property
    def ones(self):
        return self._by_outcome(1)

    @property
    def twos(self):
        return self._by_outcome(2)

    @property
    def threes(self):
        return self._by_outcome(3)

    @property
    def fours(self):
        return self._by_outcome(4)

    @property
    def fives(self):
        return self._by_outcome(5)

    @property
    def sixes(self):
        return self._by_outcome(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }


yh = YatzyHand()
i = 0
for value in yh:
    print(yh[i].outcome)
    i += 1

print("The Yatzy Hand total is {}".format(yh.total))
print(yh._sets)

