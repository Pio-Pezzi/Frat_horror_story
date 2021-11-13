import sys
import pygame as py
from vector import Vector
from gm import GameManager
from enemy import Fish
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

fish_position: list = [50, 200]

gloria: Fish = Fish(Vector(fish_position[0], fish_position[1]), fish_color, 8.0) 

fish_list: list[Fish] = []
# UI Elements for GUI
fish_total = pygame_gui.elements.UILabel(relative_rect=py.Rect((420, 40), (200, 50)), text='Fish: ' + str(len(fish_list)), manager=manager) 

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
            fish_list.append(Fish(Vector(pos[0], pos[1]), fish_color, 5.0))

    screen.fill(white)
    # for fish in fish_list: 
        # py.draw.circle(screen, fish_color, (fish.position.x, fish.position.y), 20)
        # fish.move_fish(Vector(pos[0] + 1, pos[1] + 2))

    # py.draw.rect(screen, blue, (200, 150, 100, 50))

    # py.draw.polygon(screen, fish_color, [(fish_position), (fish.position.x + 30, fish.position.y + 20), (fish.position.x + 30, fish.position.y - 20)])

    # GUI Updates
    fish_total.set_text("Social Points: " + str(len(fish_list)))
    manager.process_events(event)
    manager.update(20)
    manager.draw_ui(screen)

    # Flips all the updates from the loop onto screen
    py.display.update()