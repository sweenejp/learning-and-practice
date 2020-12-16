import random

from rpg.attributes import Agile, Sneaky
from rpg.characters3 import Character


class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))