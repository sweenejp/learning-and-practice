class NewClass:
    name_attribute = "Jimmy"

    def name_method(self):
        return self.name_method


new_instance = NewClass()
new_instance.name_method()

print(new_instance.name_method())
