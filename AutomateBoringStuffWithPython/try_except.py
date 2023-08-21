print("Enter the number of cats you have: ")
cats = input()

try:
    if int(cats) >= 4:
        print("You have a lot of cats")
    elif int(cats) == 0:
        print("You should get some cats. They are fun")
    elif int(cats) < 0:
        print("Invalid entry")
    else:
        print("That is not that many cats")
except ValueError:
    print("You did not enter a number")