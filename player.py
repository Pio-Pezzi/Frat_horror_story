class Player:
    from random import randint
   position: Vector
    size: float = 1.0
    toxicity: int = 0
    size: float: 1

    def __init__(self, position): 
        size = self.size
        


    

    def move_fish(self, new_position: Vector):
        vector: Vector = new_position - self.position 
        unit_vector: Vector = vector.normalize()
        speed_vector: Vector = unit_vector * self.speed
        self.position = self.position + speed_vector 

    def position_change(self) -> None:
        dx: int = 0
        dy: int = 0
        if K_UP:
            position.y += 1
        elif K_DOWN:
            position.y -= 1
        elif K_LEFT:
            position.x += 1
        elif K_RIGHT:
            position.x -= 1
        
        py.draw.circle(position, size)

        def collision

    def visual(self):
        py.draw.cicle(screen, fish_color, (fish.position.x, fish.position.y), 20)





