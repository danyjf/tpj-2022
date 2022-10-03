from player import Player

class Croupier(Player):
    def __init__(self, name):
        super().__init__(name)
        
    def flip_second_card(self):
        self.hand.flip_card(1)
        
    def is_hitting(self):
        return self.hand.get_points() < 17
