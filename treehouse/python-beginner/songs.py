class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __int__(self):
        return self.length

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


slimshady = Song("Eminem", "Real Slim Shady", 220)

print(slimshady.length + 14)
print(int(slimshady + 14))
