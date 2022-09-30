from card import Card

class Deck:
    def __init__(self, num_cards):
        self.cards = [Card() for _ in range(num_cards)]

    def draw(self):
        return self.cards.pop()
    
    def add(self, card):
        self.cards.append(card)
        
    def __str__(self):
        return str(self.cards)
