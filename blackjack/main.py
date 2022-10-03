# How blackjack is played:
# 1. Every player gets 2 cards facing up
# 2. Dealer gets first card facing up and second facing down
# 3. First player chooses to either stand or hit
# 4. If the player stands then ask the next player
# 5. If the player hits then deal a card and ask again until the player stands or busts
# 6. Repeat this for each player
# 7. Dealer flips his card to face up
# 8. If dealer has 17 or more then stand
# 9. If dealer has less than 17 then hit
# 10. Dealer keeps hitting until he has 17 or more or until he busts

from game import Game

g = Game()

while True:
    g.play()
    break
