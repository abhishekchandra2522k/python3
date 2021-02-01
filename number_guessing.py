import random

guesses = []

myComp = random.randint(1,50)

player = int(input("Enter a number between 1-50: "))
guesses.append(player)

while player != myComp:
    if myComp > player:
        print("Number guessed is lower than computer's number.")
    else:
        print("Number guessed is higher than computer's number.")
    
    player = int(input("Enter a number between 1-50: "))
    guesses.append(player)

if player == myComp:
    print("You have guessed the number right!")
    print("It took you %i guesses" %len(guesses))
    print("These were your guesses :")
    print(guesses)