import pygame as py
import math
from vector import Vector


class Fish:
    """Objects player is defending against."""
    position: Vector
    color: tuple 
    speed: float = 5.0 

    def __init__(self, position: Vector, color: tuple, speed: float):
        self.position = position
        self.color = color 
        self.speed = speed 

    def move_fish(self, new_position: Vector) -> None: 
        vector: Vector = new_position - self.position 
        unit_vector: Vector = vector.normalize()
        speed_vector: Vector = unit_vector * self.speed
        self.position = self.position + speed_vector 