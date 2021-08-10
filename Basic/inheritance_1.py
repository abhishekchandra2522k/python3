class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof!..")

d1 = Dog("Marcs", "Grey")
d1.bark()