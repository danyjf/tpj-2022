from card import Card

class Deck:
    def __init__(self, num_cards):
        self.cards = [Card() for _ in range(num_cards)]

    def deal(self, hand):
        hand.add(self.cards.pop())

    def deal_additional(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deal(player.hand)
            print(player)
            
            if player.is_busted():
                player.bust()
