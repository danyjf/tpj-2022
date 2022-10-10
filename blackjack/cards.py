import random

VALUES = ['A','2','3','4','5','6','7','8','9','10','D','J','K']

class Card:
    def __init__(self, value=None):
        if value:
            assert value in VALUES
            self.value = value
        else:
            self.value = random.choice(VALUES)

    def valor(self):
        if self.value.isnumeric():
            return int(self.value)
        if self.value in "DJK":
            return 10
        return 1 

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.valor() 
