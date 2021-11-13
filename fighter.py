from enemy import frat_bro
from projectile import Projectile
import pygame as py
import math
from vector import Vector
from random import randint

class Player:
    position: Vector
    size: float = 1.0
    social_points: int
    toxicity: int = 0

    def __init__(self, position): 
        size = self.size
        
    def position_change(self) -> None:
        dx: int = 0
        dy: int = 0
        if py.K_UP:
            self.position.y += 1
        elif py.K_DOWN:
            self.position.y -= 1
        elif py.K_LEFT:
            self.position.x += 1
        elif py.K_RIGHT:
            self.position.x -= 1
        
        py.draw.circle(self.position, self.size)

        # def collision

    def visual(self):
        py.draw.cicle(screen, fish_color, (fish.position.x, fish.position.y), 20)