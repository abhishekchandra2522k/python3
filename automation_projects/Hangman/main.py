import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    words_letter = set(word)  # set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(words_letter) > 0 and lives > 0:
        #letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd' (converted iterable to string)
        print(f"You have {lives} lives left and You have used these letters :", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letter:
                words_letter.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word.')
        
        elif user_letter in used_letters:
            print('You have already guessed! Guess again with different letter...')
        else:
            print('Invalid character. Please try again')

    if lives == 0:
        print(f'Lives over! The word was {word}')
    else:
        print(f"Yay! you guesses the word {word}!!")


hangman()