import pygame

class ScoreBoardText:
    def __init__(self, scores):
        self.font = pygame.font.Font('Figerona-VF.ttf', 20)
        self.display_text = {}
        self.text = {}
        self.text_rect = {}
        self.x = 50
        self.y = 20
        for player_name in scores:
            self.display_text[player_name] = f'{player_name}: {scores[player_name]}'
            self.text[player_name] = self.font.render(self.display_text[player_name], True, (0, 0, 0))
            self.text_rect[player_name] = self.text[player_name].get_rect()
            self.text_rect[player_name].center = (self.x, self.y)
            self.y += 30
    
    def update_scores(self, scores):
        self.display_text = {}
        for player_name in scores:
            self.display_text[player_name] = f'{player_name}: {scores[player_name]}'
            self.text[player_name] = self.font.render(self.display_text[player_name], True, (0, 0, 0))
