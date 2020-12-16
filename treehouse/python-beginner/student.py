class Student:
    name = "Jimmy"

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def praise(self):
        return "You're doing a great job, {}!".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.reassurance()


james = Student("Jimbo")

print(james.name)

print(james.praise())
print(james.feedback(50))