import sys
import pygame as py
from vector import Vector
from gm import GameManager
from enemy import frat_bro
import pygame_gui
from random import randint
from fighter import Player

py.init()

# Window
size = width, height = 840, 480

# RGBA constants
green = 12, 152, 54, 0
blue = 12, 52, 154, 0
white = 255, 255, 255, 255
color = 100, 50, 20, 10
fish_color = 30, 40, 100
points: int = 4

FRAMES = 60

# Makes Screen
screen = py.display.set_mode(size)

# Game clock
clock = py.time.Clock()

# Keeps game loop running
playing = True

# Handles GUI
py.display.set_caption('Frat Horror Story')

    # font = py.font.SysFont("", 32)
    # text = font.render('Welcome to the game!', True, green, blue)
    # textRect = text.get_rect()
    # textRect.center = (640 // 2, 480 // 2)

manager = pygame_gui.UIManager((width, height))
gm: GameManager = GameManager()

num_enemies: int = 4 

enemy_list: list[frat_bro] = []
enemy_total: int = len(enemy_list)

# Clock integer 
c: int = 0 
# UI Elements for GUI
time = pygame_gui.elements.UILabel(relative_rect=py.Rect((640, 0), (200, 50)), text='Time Remaining: ' + str(1800 - c), manager=manager) 
social_points = pygame_gui.elements.UILabel(relative_rect=py.Rect((640, 100), (200, 50)), text='Social Points: ' + str(len(enemy_list)), manager=manager) 
toxicity = pygame_gui.elements.UILabel(relative_rect=py.Rect((640, 200), (200, 50)), text='Toxicity: ' + str(len(enemy_list)), manager=manager) 
person: Player = Player()

i = 0 
# Game Loop
while playing:
    # Games internal clock, sets number of frames run per second
    if c > 800: 
        sys.exit()
    else: 
        c += 1 
    clock.tick(FRAMES)
    pos = py.mouse.get_pos()


    # Tracks player interaction
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                print("prha")
                person.position.y -= 10
            if event.key == py.K_s:
                person.position.y += 10
            if event.key ==  py.K_a:
                person.position.x -= 10
            if event.key ==  py.K_d:
                person.position.x += 10
        # Places fighter if game manager agrees
        #if event.type == py.MOUSEBUTTONUP:
            # pos = py.mouse.get_pos()

    screen.fill(white)

    # Adding Frat Bros and making them move
    while i < num_enemies: 
        enemy_list.append(frat_bro(blue))
        i += 1 
    for enemy in enemy_list: 
        py.draw.circle(screen, enemy.color, (enemy.position.x, enemy.position.y), 20)
        enemy.move(Vector(enemy.position.x + randint(1, 5), enemy.position.y + randint(-5, -1)))
        enemy.move(Vector(enemy.position.x + randint(-5, -1), enemy.position.y + randint(1, 5)))

    for key in enemy_list:
        if gm.collision(Vector(person.position.x, person.position.y), Vector(key.position.x, key.position.y)):
            points -= 1

    py.draw.circle(screen, green, (person.position.x, person.position.y), 20)


    # GUI Updates
    social_points.set_text("Social Points: " + str(points))
    time.set_text('Time Remaining: ' + str(800 - c))
    toxicity.set_text("Social Points: " + str(num_enemies))
    manager.process_events(event)
    manager.update(20)
    manager.draw_ui(screen)

    # Flips all the updates from the loop onto screen
    py.display.update()