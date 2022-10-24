from food import Food

class Spawner:
    def spawn_food(self, prototype) -> Food:
        return prototype.clone()
