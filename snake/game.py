import pygame

from environment import Environment
from snake import Snake
from apple import Apple
from input_handler import InputHandler
from spawner import Spawner
from score_board import ScoreBoard

import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

class Game:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sock.bind(('', MCAST_PORT))
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        
        self.display = pygame.display.set_mode((Environment.SCALE * Environment.WIDTH, Environment.SCALE * Environment.HEIGHT))
        self.clock = pygame.time.Clock()
        self.input_handler = InputHandler()
        
        self.snakes = [Snake('Player1', 40, 20), Snake('Player2', 40, 20)]
        # self.snakes = [Snake('Player1', 40, 10)]

        self.score_board = ScoreBoard(self.snakes)
        
        self.spawner = Spawner()
        apple = Apple()
        self.food = [
            self.spawner.spawn_food(apple), 
            self.spawner.spawn_food(apple)
        ]
    
    def get_input(self, event):
        if event.key == pygame.K_w:
            self.input_handler.handle_input('w', self.snakes[0])
        elif event.key == pygame.K_s:
            self.input_handler.handle_input('s', self.snakes[0])
        elif event.key == pygame.K_a:
            self.input_handler.handle_input('a', self.snakes[0])
        elif event.key == pygame.K_d:
            self.input_handler.handle_input('d', self.snakes[0])
    
    def render(self):
        self.display.fill("white")
            
        for item in self.food:
            item.draw(self.display)
        for snake in self.snakes:
            snake.draw(self.display)
        self.score_board.draw(self.display)
            
        pygame.display.flip()

    def update(self):
        for snake in self.snakes:
            snake.update(self.food)
    
    def loop(self):
        while not any(snake.dead for snake in self.snakes):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    [snake.kill() for snake in self.snakes]
                elif event.type == pygame.KEYDOWN:
                    self.get_input(event)
            
            try:
                data = self.sock.recv(10240)
                
                if data == b'up':
                    self.snakes[-1].up()
                elif data == b'down':
                    self.snakes[-1].down()
                elif data == b'left':
                    self.snakes[-1].left()
                elif data == b'right':
                    self.snakes[-1].right()
            except:
                pass

            self.update()

            self.render()
            
            self.clock.tick(15)
