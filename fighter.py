from enemy import frat_bro
from projectile import Projectile
import pygame as py
import math
from vector import Vector
from random import randint
import sys

class Player:
    position: Vector = Vector(200,200)
    size: float = 3.0
    social_points: int
    toxicity: int = 0

    def __init__(self): 
        size = self.size
        
    def position_change(self) -> None:
        dx: int = 0
        dy: int = 0
        for event in py.event.get():
            if event.type == py.K_UP:
                self.position.y += 1
            elif event.type == py.K_DOWN:
                self.position.y -= 1
            elif event.type ==  py.K_LEFT:
                self.position.x += 1
            elif event.type ==  py.K_RIGHT:
                self.position.x -= 1


    def collision(self, vector) -> None:
        for key in enemy_list:
            if (self.position.x + 2 * self.size < enemy_list[key].position.x < self.position.x - 2 * self.size) and (self.position.y + 2 * self.size < enemy_list[key].position.y < self.position.y - 2 * self.size):
                social_points -= 5

        for key in poi_list:
            if (self.position.x + 2 * self.size < poi_list[key].position.x < self.position.x - 2 * self.size) and (self.position.y + 2 * self.size < poi_list[key].position.y < self.position.y - 2 * self.size):
                social_points += 5


# F


