"""
This is a class that creates a button with coordinates, text, and etc. It was used before some of the liaison code
was adapted in and is largely unused now.

Contributors:
Rick
"""

import pygame
import time


class Button:
    def __init__(self, image, x, y, w, h):
        self.image = image
        self.image = pygame.transform.scale(self.image, (w, h))  # Scales image to designated dimensions
        self.x = x - w // 2
        self.y = y - h // 2
        self.w = w
        self.h = h

    # Draws button to screen
    def draw(self, screen):
        pygame.Surface.blit(screen, self.image, (self.x, self.y))

    # Detects if button is clicked
    def detect_click(self, mouse_x, mouse_y, l_click):
        if self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h and l_click:
            time.sleep(0.1)  # Pauses to make sure user doesn't accidentally click another button on the next screen
            return True
        else:
            return False
