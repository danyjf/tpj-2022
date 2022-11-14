class Entity:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def update(self):
        return NotImplemented
    
    def render(self, display):
        return NotImplemented
