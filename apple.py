import pygame
from pygame.locals import *
import random

class Apple:

    def __init__(self):
        self.apple = pygame.Surface((10, 10))
        self.apple.fill((255, 0,0 ))
        self.position = (0, 0)

    def set_random_position(self, screen_size):
        self.position = (random.randrange(0, screen_size-10, 10), random.randrange(0, screen_size-10,10))
