import socket

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
MULTICAST_TTL = 2

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
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        
        self.command = {
            'w': Up(),
            's': Down(),
            'a': Left(),
            'd': Right(),
        }
        
        self.send_msg = {
            'w': b'up',
            's': b'down',
            'a': b'left',
            'd': b'right',
        }
    
    def handle_input(self, key, actor):
        self.sock.sendto(self.send_msg[key], (MCAST_GRP, MCAST_PORT))
        self.command[key].execute(actor)
