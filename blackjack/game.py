from baralhos import Baralho
from players import Player

class Game():
    def __init__(self):

        self.croupier = Player("Croupier")
        self.humano = Player("Jogador1")

        self.mesa = Baralho(40)

        self.winner = None
        self.running = True
        self.last_option = "" 
        self._current_player = None 

    def status(self):
        print(self.croupier)
        print(self.humano)

    def input(self):
        while True:
             o = input("(H)it, (S)tand, (F)old")
             if o in "HhSsFf":
                return o

    def play(self):
        if self._current_player == self.humano:
            self._current_player = self.croupier
        else:
            self._current_player = self.humano


        if self._current_player == self.humano:
            option = self.input()
        else:
            if self.croupier.valor() >= 17:
                option = "s"
            else:
                option = "h"


        if option in "Hh":
            self._current_player.adicionar(self.mesa.buscar())

        if option in "Ff":
            #Desiste e perde
            self.running = False           
            self.winner = self.croupier 

        if option in "Ss" and self.last_option in "Ss":
            self.running = False
            self.winner = self.humano if self.humano.valor() > self.croupier.valor() else self.croupier
 
        if self._current_player.valor() == 21:
            self.winner = self._current_player 
            self.running = False       

        if self._current_player.valor() > 21:
            self.winner = self.croupier if self._current_player == self.humano else self.humano
            self.running = False       

        self.last_option = option

        if self.running == False:
            return False

        return True
