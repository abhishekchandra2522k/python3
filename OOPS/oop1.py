# position, name, age, level, salary
se1 = ["Software Engineer", "Abhishek", 21, "Junior", 600000]
se2 = ["Software Engineer", "Siddharth", 24, "Senior", 1000000]

# class is only a blueprint of data structure
class SoftwareEngineer():

    #class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


se1 = SoftwareEngineer("Abhishek", 21, "Junior", 600000)

print(se1.name, se1.age)
print(SoftwareEngineer.alias)