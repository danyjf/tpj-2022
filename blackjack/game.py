from croupier import Croupier
from player import Player
from deck import Deck
from croupier import Croupier

class Game:
    def __init__(self):
        self.player = Player('Jogador1')
        self.croupier = Croupier('Croupier')
        self.turn = 0
        self.deck = Deck(40)

    def play(self):
        self.deal_starting_cards()
        self.croupier.flip_second_card()
        self.display_players_hands()
        self.display_croupier_hand()
        
        self.deck.deal_additional(self.player)
        
        self.croupier.flip_second_card()
        self.display_croupier_hand()
        
        self.deck.deal_additional(self.croupier)
        
        if self.croupier.is_busted():
            if not self.player.is_busted():
                self.player.win()
        else:
            if not self.player.is_busted():
                if self.player.hand.get_points() > self.croupier.hand.get_points():
                    self.player.win()
                elif self.player.hand.get_points() < self.croupier.hand.get_points():
                    self.player.lose()
                else:
                    self.player.push()

    def deal_starting_cards(self):
        for i in range(2):
            self.deck.deal(self.player.hand)
            self.deck.deal(self.croupier.hand)
        
    def display_players_hands(self):
        print(self.player)
        
    def display_croupier_hand(self):
        print(self.croupier)
