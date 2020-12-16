import random


class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):
        return self.sneaky and (random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10


new_character = Thief(input("What is the name of your champion?: "), butts=0)

print(f"Your champion's name is {new_character.name}")
print(f"{new_character.name} has {new_character.butts} butts")