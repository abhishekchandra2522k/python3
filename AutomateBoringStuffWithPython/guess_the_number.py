import random

print("Welcome to the Guess the number game:")

name = input("Enter your name: ")

secret_number = random.randint(1, 20)

print("You will have seven chances to guess the number")

for i in range(1, 8):
    print("Enter a number")

    try:
        num = int(input())
        if num == secret_number:
            print("Yay " + name + "! you have guessed the number in", i, "chances")
            break
        elif num > secret_number:
            print("Duhh! your number is a bit on higher side, guess a lower number.")
            print("Now you have " + str(7 - i) + " chances left")
        elif num < secret_number:
            print("Duhh! your number is a bit on the lower side, guess a higher number")
            print("Now you have " + str(7 - i) + " chances left")
    except ValueError:
        print("You did not enter a number")
        print("One chance wasted!!!!")

print("Congratulations!!!")
