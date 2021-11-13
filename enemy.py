import pygame as py
import math
from vector import Vector
from random import randint

class frat_bro:
    """Non-Playable Characters."""
    position: Vector
    color: tuple 
    speed: float = 5.0 
    size: float = 3.0 

    # Giving all NPC's Position, color, and speed. 
    def __init__(self, color: tuple):
        self.position = self.randpos()
        self.color = color 

    # Moving characters 
    def move(self, new_position: Vector) -> None: 
        vector: Vector = new_position - self.position 
        unit_vector: Vector = vector.normalize()
        speed_vector: Vector = unit_vector * self.speed
        self.position = self.position + speed_vector 

    def randpos(self) -> Vector: 
        x: float = randint(20, 620) 
        y: float = randint(20, 460)
        result: Vector = Vector(x, y) 
        return result 

class poi: 
    position: Vector 
    color: tuple 
    """Person of Interest."""
    def __init__(self, color: tuple):
        self.position = self.randpos()
        self.color = color 

    # Moving characters 
    def move(self, new_position: Vector) -> None: 
        vector: Vector = new_position - self.position 
        unit_vector: Vector = vector.normalize()
        speed_vector: Vector = unit_vector * self.speed
        self.position = self.position + speed_vector 
