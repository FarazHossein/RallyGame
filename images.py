"""
This file has a bunch of image variables for the main program. It is mainly to reduce clutter on main.py.

Contributors:
Siddharth
"""

import pygame

pygame.init()

# getting information from user screen
dis_info = pygame.display.Info()
screen_width = dis_info.current_w
screen_height = dis_info.current_h

# create a loaded image for the loading screen
loading_image = pygame.image.load("graphics/loading.png")
loading_image = pygame.transform.scale(loading_image, (screen_width, screen_height))

# create a loaded image for the menu screen
menu_image = pygame.image.load("graphics/menu.png")
menu_image = pygame.transform.scale(menu_image, (screen_width, screen_height))

# create a loaded image for the game over screen
game_over_image = pygame.image.load("graphics/game_over.png")
game_over_image = pygame.transform.scale(game_over_image, (screen_width, screen_height))

# create a loaded image for the track
track_image = pygame.image.load("graphics/track.png")
track_image = pygame.transform.scale(track_image, (1000, 800))

# create a loaded image for the car
car_image = pygame.image.load("graphics/car.png")
car_image = pygame.transform.rotate(car_image,180)
car_image = pygame.transform.scale(car_image, (50, 25))

# create a loaded image for the instruction screen background
Instruction = pygame.image.load("graphics/Instruction.png")
Instruction = pygame.transform.scale(Instruction, (screen_width, screen_height))
