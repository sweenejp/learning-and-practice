import random


class Thief:
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickpocket(self):
        return self.sneaky and (random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10


kenneth = Thief("Sir Kenneth", False)

print(kenneth.sneaky)

kenneth.sneaky = False

print(kenneth.sneaky)

print(Thief.sneaky)

print(kenneth)

# a method needs an instance...
print(Thief.pickpocket(kenneth))

# does the same as...
print(kenneth.pickpocket())

print("**************************")
# because 'self' means that method is using the instance as it's parameter (?)

kenneth.sneaky = True
print(kenneth.hide(9))

jim = Thief("Sir Jamie", scars=15, favorite_weapon="Blunt Ax")

print(jim.favorite_weapon)
print(jim.name)
print(jim.scars)
print(jim.sneaky)

