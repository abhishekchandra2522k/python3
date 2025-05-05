#string concatenation (how to put strings together)
# name = "Abhishek"

# print("Hi " + name)
# print(f"Hi {name}") # fstring
# print("Hi {}".format(name)) #formatting

adj = input("Adjective : ")
verb1 = input("Verb : ")
verb2 = input("Verb : ")
famous_person = input("Famous Person : ")

madlib = f"Computer programming is {adj}! It makes me so excited all the because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}."

print(madlib)