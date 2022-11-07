from observer import Observer
from environment import Environment
from score_board_text import ScoreBoardText

class ScoreBoard(Observer):
    def __init__(self, players):
        self.scores = {}
        
        for player in players:
            player.add_observer(self)
            self.scores[player.name] = 0
            
        self.score_board_text = ScoreBoardText(self.scores)

    def on_notify(self, entity, event):
        if event == Environment.EAT:
            self.scores[entity.name] += 1
            self.score_board_text.update_scores(self.scores)

    def draw(self, display):
        for player_name in self.score_board_text.text:
            display.blit(self.score_board_text.text[player_name], self.score_board_text.text_rect[player_name])
