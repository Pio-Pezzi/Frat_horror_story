from enemy import Fish
from projectile import Projectile
import pygame as py
import math
from vector import Vector

class Player:
    """Main player of the game."""
    position: Vector
    speed: float = 5.0
    size: int = 1
    social_points: int
    time: int
    toxicity: int

    def move(self, new_position: Vector) -> None: 
        vector: Vector = new_position - self.position 
        unit_vector: Vector = vector.normalize()
        speed_vector: Vector = unit_vector * self.speed
        self.position = self.position + speed_vector 