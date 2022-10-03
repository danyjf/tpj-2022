from hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        
    def is_busted(self):
        if self.hand.get_points() > 21:
            self.bust()
            return True
        return False
    
    def is_hitting(self):
        print('1 - Hit')
        print('2 - Stand')
        opt = input('Choose an option: ')
        
        if opt == '1':
            return True
        elif opt == '2':
            return False
        else:
            print(f'{opt} is not an option')
            
    def win(self):
        print(f'{self.name} wins.')
    
    def bust(self):
        print(f'{self.name} busts.')
        
    def lose(self):
        print(f'{self.name} loses.')
        
    def push(self):
        print(f'{self.name} pushes.')
        
    def __str__(self):
        return f'{self.name}: {str(self.hand)}'
