# Liaison work ** wasn't commented by liaison

import pygame
import button

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



class Game_Over:
    def __init__(self):
        self.font_big = pygame.font.SysFont(None, 100)
        self.font_small = pygame.font.SysFont(None, 20)
        self.BACKGROUND = (0, 0, 0)
        self.BLACK = (0, 0, 0)
        self.TEXT_COLOUR = (255, 255, 255)
        self.BUTTON_COLOUR = (100, 0, 110)
        self.BUTTON_COLOUR_HIGHLIGHT = (120, 72, 124)
        self.screen_width = pygame.display.get_surface().get_size()[0]
        self.screen_height = pygame.display.get_surface().get_size()[1]

    def game_over(self):
        self.gameOver = self.font_big.render("Game Over!", True, self.TEXT_COLOUR, screen)
        self.gameOverRect = self.gameOver.get_rect()
        self.gameOverRect.centerx = screen.get_rect().centerx
        self.gameOverRect.centery = screen.get_rect().centery
        exit_button = button.Button(pygame.image.load("graphics/menu_button.png"), self.screen_width // 2,
                                    self.screen_height // 2 + 320, 400, 160)
        exit_button.draw(screen)


    def play_again(self):
        self.playAgain = self.font_small.render("PLAY AGAIN", True, self.TEXT_COLOUR, screen)
        self.playAgainRect = self.playAgain.get_rect()
        self.playAgainRect.centerx = screen.get_rect().centerx - 200
        self.playAgainRect.centery = screen.get_rect().centery + 200
        retry_button = button.Button(pygame.image.load("graphics/retry_button.png"), self.screen_width // 2, self.screen_height // 2 + 120, 400, 160)
        retry_button.draw(screen)

