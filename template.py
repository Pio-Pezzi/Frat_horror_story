import sys
import pygame as py
from vector import Vector
from gm import GameManager
from enemy import frat_bro, poi
import pygame_gui
from random import randint, choice 
from fighter import Player

py.init()

# Window
size = width, height = 840, 480

# Constants
green = 12, 152, 54, 0
blue = 12, 52, 154, 0
white = 255, 255, 255, 255
color = 100, 50, 20, 10
tan = 210, 180, 140
brown = 139, 69, 19, 0
fish_color = 30, 40, 100
i = 0 
d = 0 
points: int = 4
level: int = 0

# Clock information 
c: int = 0 
FRAMES = int(input("How fast are the frat bros? Range of 1-120. "))

# Enemy Information 
num_enemies: int = int(input("How many frat bros are there? "))
enemy_list: list[str] = []
enemy_total: int = len(enemy_list)

# Alcohol Information 
num_drinks: int = 5 
drink_list: list[str] = []

# Makes Screen
screen = py.display.set_mode(size)

# Game clock
clock = py.time.Clock()

# Keeps game loop running
playing = True

# Handles GUI
py.display.set_caption('Frat Horror Story')

manager = pygame_gui.UIManager((width, height))
gm: GameManager = GameManager()


# UI Elements for GUI
time = pygame_gui.elements.UILabel(relative_rect=py.Rect((640, 0), (200, 50)), text='Time Remaining: ' + str(750 - c), manager=manager) 
social_points = pygame_gui.elements.UILabel(relative_rect=py.Rect((640, 100), (200, 50)), text='Social Points: ' + str(len(enemy_list)), manager=manager) 
toxicity = pygame_gui.elements.UILabel(relative_rect=py.Rect((640, 200), (200, 50)), text='Toxicity: ', manager=manager) 
person: Player = Player()

# Game Loop
while playing:
    # Games internal clock, sets number of frames run per second
    if c > 750: 
        sys.exit()
    else: 
        c += 1 
    clock.tick(FRAMES)
    pos = py.mouse.get_pos()

    # AI Movement - Frat Bros 
    y: int 
    x: int 
    move_set: list[int] = [-8, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 8]
    r: int = randint(1, 3)
    if r == 1:
        x = choice(move_set)
        y = 0 
    elif r == 2: 
        y = choice(move_set)
        x = 0 
    elif r == 3: 
        x = choice(move_set)
        y = choice(move_set)
        
    # Tracks player interaction
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                print("prha")
                person.position.y -= 30
            if event.key == py.K_s:
                person.position.y += 30
            if event.key ==  py.K_a:
                person.position.x -= 30
            if event.key ==  py.K_d:
                person.position.x += 30
        # Places fighter if game manager agrees
        #if event.type == py.MOUSEBUTTONUP:
            # pos = py.mouse.get_pos()

    screen.fill(tan)

    # Adding Frat Bros and making them move
    while i < num_enemies: 
        enemy_list.append(frat_bro(blue))
        i += 1 
    for enemy in enemy_list: 
        r: int = randint(1, 3)
        if r == 1:
            x = choice(move_set)
            y = 0 
        elif r == 2: 
            y = choice(move_set)
            x = 0 
        elif r == 3: 
            x = choice(move_set)
            y = choice(move_set)
             
        py.draw.circle(screen, enemy.color, (enemy.position.x, enemy.position.y), 20)
        enemy.move(Vector(enemy.position.x + x, enemy.position.y + y))
        enemy.move(Vector(enemy.position.x + x, enemy.position.y + y))

       

    
    # Adding Drinks 
    while d < num_drinks: 
        drink_list.append(poi(brown))
        d += 1 
    for drink in drink_list: 
        if drink.show:
            py.draw.circle(screen, drink.color, (drink.position.x, drink.position.y), 10)

    # Collision (Enemies)
    for key in enemy_list:
        if gm.collision(Vector(person.position.x, person.position.y), Vector(key.position.x, key.position.y)):
            points -= 1

    py.draw.circle(screen, green, (person.position.x, person.position.y), 20)

    for key in drink_list:
        if gm.collision(Vector(person.position.x, person.position.y), Vector(key.position.x, key.position.y)) and key.show:
            points += 10
            level += 3
            key.show = False

    if level > 10: 
        points -= 100 


    # GUI Updates
    social_points.set_text("Social Points: " + str(points))
    time.set_text('Time Remaining: ' + str(750 - c))
    toxicity.set_text("Toxicity: " + str(level))
    manager.process_events(event)
    manager.update(20)
    manager.draw_ui(screen)

    # Flips all the updates from the loop onto screen
    py.display.update()