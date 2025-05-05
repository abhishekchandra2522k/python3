import random

def play():
    user = input("What's your choice? \n 'r' for Rock, 'p' for Paper, 's' for Scissors : ").lower()
    computer = random.choice(['s', 'p', 'r'])

    if user == computer:
        return 'It\'s a tie'
    
    #r > s, s > p, p > r
    if is_win(user, computer):
        return "You WON!"

    return "You Lose!"


def is_win(player, opponent):
    # returns true if player returns
    if ((player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent =='r')):
        return True
    
print(play())