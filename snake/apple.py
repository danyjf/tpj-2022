from food import Food
from apple_sprite import AppleSprite
from environment import Environment

class Apple(Food):
    def __init__(self):
        super().__init__()
        self.apple_sprite = AppleSprite()
    
    def draw(self, display):
        display.blit(self.apple_sprite.image, (Environment.SCALE * self.pos[0], Environment.SCALE * self.pos[1]))
    
    def clone(self):
        return Apple()
