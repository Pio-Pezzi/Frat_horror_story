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

    def collision(self, vector) -> None:
        for key in enemy_list:
            if (self.position.x + 2 * self.size < enemy_list[key].position.x < self.position.x - 2 * self.size) and (self.position.y + 2 * self.size < enemy_list[key].position.y < self.position.y - 2 * self.size):
                Social_score -= 5

        for key in poi_list:
            if (self.position.x + 2 * self.size < poi_list[key].position.x < self.position.x - 2 * self.size) and (self.position.y + 2 * self.size < poi_list[key].position.y < self.position.y - 2 * self.size):
                Social_score += 5


