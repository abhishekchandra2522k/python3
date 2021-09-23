import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    # we all want players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
        # return super().get_move(game)

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
        # return super().get_move(game)