import pygame
from define import *

class Player() :
    def __init__(self, color, x, y) -> None :
        self.x = x
        self.y = y
        self.color = color
    def show(self, surface) :
        pygame.draw.rect(surface, self.color, (self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT))
    def move_up(self) :
        self.y = self.y - PLAYER_VELOCITY 
        if self.y < 0 : 
            self.y = 0
    def move_down(self) :
        self.y += PLAYER_VELOCITY 
        if self.y > WINDOW_HEIGHT - PLAYER_HEIGHT :
            self.y = WINDOW_HEIGHT - PLAYER_HEIGHT