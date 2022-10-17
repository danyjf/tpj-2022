class Command:
    def execute():
        raise NotImplemented

class Up(Command):
    def execute(self, actor):
        actor.up()

class Down(Command):
    def execute(self, actor):
        actor.down()

class Left(Command):
    def execute(self, actor):
        actor.left()

class Right(Command):
    def execute(self, actor):
        actor.right()

class InputHandler:
    command = {
        'w': Up(),
        's': Down(),
        'a': Left(),
        'd': Right(),
        'up': Up(),
        'down': Down(),
        'left': Left(),
        'right': Right()
    }
    
    def handle_input(self, key, actor):
        self.command[key].execute(actor)
