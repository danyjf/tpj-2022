from observer import Observer
from environment import Environment

class ScoreBoard(Observer):
    def __init__(self, players):
        self.scores = {}
        
        for player in players:
            player.add_observer(self)
            self.scores[player.name] = 0

    def on_notify(self, entity, event):
        if event == Environment.EAT:
            self.scores[entity.name] += 1
            print(self.scores)
