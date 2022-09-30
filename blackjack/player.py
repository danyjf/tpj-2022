from unicodedata import name
from deck import Deck

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = Deck(3)
        
    def add(self, card):
        self.hand.add(card)
        
    def __str__(self):
        return f'{self.name}: {str(self.hand)}'
