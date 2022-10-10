from game import Game


g = Game()
g.status()
while True:
    r = g.play() 

    if r:
        g.status()
    else:
        print(f"Vencedor é o {g.winner}")
        break 
