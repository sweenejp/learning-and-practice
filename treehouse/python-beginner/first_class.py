class Student:
    name = ""
    
    def __init__(self, name):
        self.name = name
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()

new_student = Student("Jimmy")
print(new_student.name)