class Liar(list):

    def __len__(self):
        return super().__len__() + 5


new_list = Liar([1, 2])


wrong_length = len(new_list)
print(wrong_length)

