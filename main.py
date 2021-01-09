"""
This is the main program to be run to run the game.

Contributors:
Siddharth - car, checkpoints
Faraz - sounds, music, liaison classes implementation
Rick - different screens, scores, times
Shraddha - testing
"""

import pygame
from images import *
from carControl import Car
import button
import score_board
import key_input
import GameOver
from Instructions import instruction_screen, render_text

pygame.init()

# Sets up screen
fps_clock = pygame.time.Clock()  # Used to control fps of program
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Program variables
frame_rate = 60
screen_width = pygame.display.get_surface().get_size()[0]
screen_height = pygame.display.get_surface().get_size()[1]

width = screen_width // 2
height = screen_height // 2
pygame.display.set_caption("Mahmoud Rally 8 Supreme")  # Sets window caption

screen_control = 0
counter = 0  # Counter used for screen switches and countdowns; unrelated to player's lap time

x = 800
y = 800

# set the x,y coordinates for the checkpoints (separated by horizontal and vertical road checkpoints)
checks_hor = [[width - 50, height + 197], [width - 346, height - 72], [width - 100, height - 316], [width + 300, height - 120]]
checks_ver = [[width - 339, height + 100], [width - 441, height - 150], [width + 125, height - 170], [width + 373, height + 100]]

# create the player object
player = Car(width + 150, height + 230, 310, 0)

# Player info
name = ""
time = 0  # Time of round (divide by frame_rate to get time in seconds)
scores = score_board.ScoreBoard("score_board.txt")

# set the phase for checking the checkpoints
check_phase = 1

# create an instance for the game over function
gameover = GameOver.Game_Over()

# Buttons
play_button = button.Button(pygame.image.load("graphics/play_button.png"), screen_width // 2, screen_height // 2 + 120, 400, 160)
exit_button = button.Button(pygame.image.load("graphics/exit_button.png"), screen_width // 2, screen_height // 2 + 320, 400, 160)
okay_button = button.Button(pygame.image.load("graphics/okay_button.png"), screen_width // 2, screen_height // 2 + 320, 400, 160)
retry_button = button.Button(pygame.image.load("graphics/retry_button.png"), screen_width // 2, screen_height // 2 + 120, 400, 160)
menu_button = button.Button(pygame.image.load("graphics/menu_button.png"), screen_width // 2, screen_height // 2 + 320, 400, 160)

# Music
pygame.mixer.music.load('music/Music.mp3')
pygame.mixer.music.play()

# set the font for the on screen text
font = pygame.font.Font("arial.ttf", 48)
font_l = pygame.font.Font("arial.ttf", 144)
white = (255, 255, 255)
black = (0, 0, 0)

# Main program loop
running = True
while running:
    # Checks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks quit, stops the program loop
            running = False

    screen.fill(white)  # Sets background

    mouse_x, mouse_y = pygame.mouse.get_pos()  # Gets mouse coordinates and saves to shorter variable
    l_click = pygame.mouse.get_pressed()[0]  # Gets left click true/false and saves to shorter variable
    keys = pygame.key.get_pressed()  # Gets all keys being pressed

    # Loading screen
    if screen_control == 0:
        pygame.Surface.blit(screen, loading_image, (0, 0))  # Loading background

        # Switches to next screen after 1 second
        if counter >= 1 * frame_rate:
            screen_control = 1

    # Title screen
    elif screen_control == 1:
        pygame.Surface.blit(screen, menu_image, (0, 0))  # Menu background

        # Draws buttons
        play_button.draw(screen)
        exit_button.draw(screen)

        # Goes to next screen when play button is clicked
        if play_button.detect_click(mouse_x, mouse_y, l_click):
            screen_control = 1.5

        # Closes when exit button is clicked
        if exit_button.detect_click(mouse_x, mouse_y, l_click):
            running = False

    # Enter name screen
    elif screen_control == 1.5:
        pygame.Surface.blit(screen, menu_image, (0, 0))  # deisplay Menu background

        name = key_input.key_input(name, keys)  # Gets all keyboard and uses it to update name

        text = font.render("Enter Name: " + name, True, white)
        pygame.Surface.blit(screen, text, (screen_width // 5, screen_height // 2))

        # Draws buttons
        okay_button.draw(screen)

        # Goes to instructions screen when okay button is clicked
        if okay_button.detect_click(mouse_x, mouse_y, l_click):
            # If the player did not enter a name, set it to Player
            if len(name) == 0:
                name = "Player"
            screen_control = 2

    # Instructions screen
    elif screen_control == 2:
        pygame.Surface.blit(screen, Instruction, (0, 0))  # Loading background

        # Draws buttons
        okay_button.draw(screen)

        # call the instruction_screen function fro Instructions.py
        instruction_screen('instructions.txt')  # Calling function

        # Goes to game screen when okay button is clicked
        if okay_button.detect_click(mouse_x, mouse_y, l_click):
            screen_control = 3
            player.reset()
            time = 0
            counter = 0

    # Game screen
    elif screen_control == 3:

        # this draws the background image
        pygame.draw.rect(screen, (255, 207, 158), [0, 0, screen_width, screen_height])  # Track background
        pygame.Surface.blit(screen, track_image, (screen_width // 2 - 500, screen_height // 2 - 400))  # Track

        # this establishes the count down before the game commences
        if 0 <= counter // frame_rate < 1:
            text = font_l.render("3", True, black)
            pygame.Surface.blit(screen, text, (screen_width // 2 - 30, screen_height // 2 - 30))
        elif 1 <= counter // frame_rate < 2:
            text = font_l.render("2", True, black)
            pygame.Surface.blit(screen, text, (screen_width // 2 - 30, screen_height // 2 - 30))
        elif 2 <= counter // frame_rate < 3:
            text = font_l.render("1", True, black)
            pygame.Surface.blit(screen, text, (screen_width // 2 - 30, screen_height // 2 - 30))
        else:

            # Increases and displays time
            time += 1
            text = font.render(str(int(100 * time / frame_rate) / 100), True, (0, 0, 0))

            # draw the first 2 checkpoints
            pygame.draw.rect(screen,(255,0,0),[checks_hor[0][0],checks_hor[0][1],20,93])
            pygame.draw.rect(screen,(255,0,0),[checks_ver[0][0],checks_ver[0][1],102,20])

            # draw the remaining horizontal checkpoints
            for i in range(3):
                pygame.draw.rect(screen,(255,0,0),[checks_hor[i+1][0],checks_hor[i+1][1],20,90])

            # draw the remaining vertical checkpoints
            for p in range(3):
                pygame.draw.rect(screen,(255,0,0),[checks_ver[p+1][0],checks_ver[p+1][1],96,20])

            # if the check_phase is 1:
            if check_phase == 1:

                # call the checkpoint detection function
                player.detect()

                # call the function that checks if all the checkpoints have been crossed
                player.checker()

                # if the return value of checker is True...
                if player.checker() is True:  # If the player finishes
                    scores.add_entry(name, time / frame_rate)  # Adds player's score to scoreboard
                    scores.sort_ascending()  # Sorts by ascending, since the players with the lowest times are better
                    scores.export_score_board()  # Saves new scores to file
                    screen_control = 4

            # call the move function from player
            player.move()

            pygame.Surface.blit(screen, text, (25, 25))

    # End screen
    elif screen_control == 4:
        pygame.Surface.blit(screen, game_over_image, (0, 0))  # Game over background
        pygame.mixer.pause()

        TEXT_COLOUR = (255, 255, 255)
        BUTTON_COLOUR = (100, 0, 110)
        BUTTON_COLOUR_HIGHLIGHT = (120, 72, 124)

        # Draws time
        text = font.render("Final Time: " + str(int(100 * time / frame_rate) / 100), True, white)
        pygame.Surface.blit(screen, text, (20, 20))

        # Draws scoreboards of time (top 10)
        scores.draw(screen, screen_width // 2 - 80, screen_height // 2 - 300, "arial.ttf", 24, white, 10)

        # Calling GameOver class functions (Button and mouse detection for retry and menu button)
        gameover.game_over()
        gameover.play_again()

        # Mouse detection for menu button and resetting variables
        if menu_button.detect_click(mouse_x, mouse_y, l_click):
            # If the player did not enter a name, set it to Player
            screen_control = 1
            player.reset()
            time = 0
            counter = 0
            name = ""
        elif retry_button.detect_click(mouse_x, mouse_y, l_click):
            # If the player did not enter a name, set it to Player
            screen_control = 3
            player.reset()
            time = 0
            counter = 0

    pygame.display.flip()  # Updates screen
    fps_clock.tick(frame_rate)  # Sets program to 60fps
    counter += 1


pygame.quit()  # Quits at the end
