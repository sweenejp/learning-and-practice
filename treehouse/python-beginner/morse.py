class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse = []
        for item in self.pattern:
            if item == ".":
                morse.append("dot")
            elif item == "_":
                morse.append("dash")
        return "-".join(morse)

    def __iter__(self):
        yield from self.pattern

    @classmethod
    def from_string(cls, a_string):
        a_list = a_string.split("-")
        dif_list = []
        for item in a_list:
            if item == "dot":
                dif_list.append(".")
            elif item == "dash":
                dif_list.append("_")
        return cls(dif_list)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


morse_of_S = S().__str__()
print(morse_of_S)

new_list = Letter.from_string("dot-dot-dot")
print(new_list)
