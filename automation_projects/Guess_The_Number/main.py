import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while guess != random_number:
        count += 1
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess > random_number:
            print("Sorry, Number is too high")
        elif guess < random_number:
            print("Sorry, Number is too low")
    print(f"Congratulations! You guessed it correct in {count} attempts.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 0
    while feedback != 'c':
        count += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess =  low
        feedback = input(f"is {guess} too high(h), to low(l), or correct(c)? : ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congratulations! computer guessed it correct in {count} attempts.")

guess(10) 
computer_guess(10000) # guessing ethereum price $3059 on 20th sept, 2021