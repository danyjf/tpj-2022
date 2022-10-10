from baralhos import Baralho

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = Baralho(2)

    def adicionar(self, carta):
        self.hand.adicionar(carta)

    def valor(self):
        return self.hand.valor()

    def __str__(self):
        return f"{self.name}: {self.hand}"
