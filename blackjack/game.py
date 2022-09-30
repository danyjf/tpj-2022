from player import Player
from deck import Deck

class Game():
    def __init__(self):
        self.croupier = Player('Croupier')
        self.player = Player('Jogador1')

        self.table = Deck(40)

        self._current_player = self.player
        
    def status(self):
        print(self.croupier)
        print(self.player)

    def play(self):
        self._current_player.add(self.table.draw())
