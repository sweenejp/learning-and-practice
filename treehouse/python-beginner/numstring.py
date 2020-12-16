class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

num = NumString("5")

print(isinstance(num.__int__, int))
print(num.__int__())