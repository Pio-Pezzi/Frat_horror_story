import sys
import pygame as py
from vector import Vector
from gm import GameManager
from enemy import frat_bro
import pygame_gui
py.init()

# Window
size = width, height = 640, 480

# RGBA constants
green = 12, 152, 54, 0
blue = 12, 52, 154, 0
white = 255, 255, 255, 255
color = 100, 50, 20, 10
fish_color = 30, 40, 100

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

num_enemies: int = 4 

enemy_list: list[str] = []
enemy_total: int = len(enemy_list)
# UI Elements for GUI
time = pygame_gui.elements.UILabel(relative_rect=py.Rect((420, 40), (200, 50)), text='Time Remaining: ' + str(len(enemy_list)), manager=manager) 
social_points = pygame_gui.elements.UILabel(relative_rect=py.Rect((420, 50), (200, 60)), text='Social Points: ' + str(len(enemy_list)), manager=manager) 
toxicity = pygame_gui.elements.UILabel(relative_rect=py.Rect((420, 60), (200, 70)), text='Toxicity: ' + str(len(enemy_list)), manager=manager) 

i = 0 
# Game Loop
while playing:
    # Games internal clock, sets number of frames run per second
    clock.tick(FRAMES)

    # Tracks player interaction
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
        # Places fighter if game manager agrees
        if event.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()

    screen.fill(white)

    while i < num_enemies: 
        enemy_list.append(frat_bro(blue))
    for enemy in enemy_list: 
        py.draw.circle(screen, frat_bro.color, (frat_bro.position.x, frat_bro.position.y), 20)
        frat_bro.move(Vector(pos[0] + 1, pos[1] + 2))


    # GUI Updates
    enemy_total.set_text("Social Points: " + num_enemies)
    manager.process_events(event)
    manager.update(20)
    manager.draw_ui(screen)

    # Flips all the updates from the loop onto screen
    py.display.update()