from card import Card

class Hand:
    def __init__(self):
        self.cards = []
        
    def add(self, card):
        self.cards.append(card)
    
    def flip_card(self, i):
        self.cards[i].flip()
        
    def get_points(self):
        points = 0
        
        for card in self.cards:
            if str(card.value) in 'DJK':
                points += 10
            elif card.value == 'A':
                points += 1
            else:
                points += card.value
                
        contains_ace = False
        for card in self.cards:
            if card.value == 'A':
                contains_ace = True

        if contains_ace and points <= 11:
            points += 10
            
        return points

    def __str__(self):
        display = ''
        for card in self.cards:
            if card.is_facing_up:
                display += str(card.value) + ' '
        return display
        