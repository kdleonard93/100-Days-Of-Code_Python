class Parent:
    def __init__(self, parent_attribute):
        self.parent_attribute = parent_attribute

class Child(Parent):
    def __init__(self, parent_attribute, child_attribute):
        super().__init__(parent_attribute)
        self.child_attribute = child_attribute

confession = Child("I'm the Pappy!", "That's the truth!")


print(confession.parent_attribute)
print(confession.child_attribute)