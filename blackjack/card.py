import random

VALUES = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'D', 'J', 'K']

class Card:
    def __init__(self):
        self.value = random.choice(VALUES)

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()
