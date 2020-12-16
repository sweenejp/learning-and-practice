class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length
