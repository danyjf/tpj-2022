from cards import Card

class Baralho:
    def __init__(self, num_cards):
        self.cards = [Card() for _ in range(num_cards)]

    def adicionar(self, carta):
        self.cards.append(carta)
    
    def buscar(self):
        return self.cards.pop() 

    def valor(self):
        cards_temp = [card for card in self.cards if card.value!='A']

        total_temp = sum([c.valor() for c in cards_temp])    
        total_ases = 0
        if len(cards_temp) != len(self.cards):
            ases = [card for card in self.cards if card.value == 'A']
            total_ases = len(ases)
            if total_temp + total_ases+10 <= 21:
                total_ases+=10 # -1 + 11
        return total_temp + total_ases 
        
    def __str__(self):
        return str([str(c) for c in self.cards])

if __name__ == "__main__":
    b = Baralho(0)
    b.adicionar(Card('A'))
    b.adicionar(Card('A'))
    b.adicionar(Card('A'))
    
    print(b)
    print(b.valor())
