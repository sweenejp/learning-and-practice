class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        self = self * 2
        return self


print(Double(5))

