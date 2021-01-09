# Liaison

import pygame


class ScoreBoard:
    def __init__(self, file_path):
        self.file_path = file_path  # File path of scoreboard file
        self.scores = list()  # Creates list variable to store scores; stored as 2D list of [<Name>, <Score>]

        self.import_score_board()

    # Copies the external scoreboard file to the program scoreboard
    def import_score_board(self):
        f_in = open(self.file_path, 'r')
        self.scores = [entry.split() for entry in f_in.readlines()]
        f_in.close()

    # Overwrites the external scoreboard file with the program scoreboard
    def export_score_board(self):
        f_out = open(self.file_path, 'w')
        for entry in range(len(self.scores)):
            f_out.write(self.scores[entry][0] + ' ' + self.scores[entry][1])
            if entry < len(self.scores):  # Adds a newline except for after the last line
                f_out.write('\n')
        f_out.close()

    # Draws the scoreboard to a given screen at a given (x, y) with a given font path, size, and colour
    def draw(self, screen, x, y, font_path, font_size, font_colour):
        font = pygame.font.Font(font_path, font_size)

        # Draws each entry in scoreboard to screen
        for entry in range(len(self.scores)):
            text = font.render("{0:20}".format(self.scores[entry][0]), True, font_colour)
            pygame.Surface.blit(screen, text, (x - font_size * 10, y + entry * font_size * 1.5))
            text = font.render("{0:>20.2f}".format(float(self.scores[entry][1])), True, font_colour)
            pygame.Surface.blit(screen, text, (x + font_size * 10, y + entry * font_size * 1.5))

    # Overloaded draw function with optional "number of entries" (instead of drawing all the entries)
    def draw(self, screen, x, y, font_path, font_size, font_colour, entries):
        font = pygame.font.Font(font_path, font_size)

        # Makes sure the number of entries to draw doesn't exceed the total number of entries
        if entries > len(self.scores):
            entries = len(self.scores)

        # Draws each entry in scoreboard to screen
        for entry in range(entries):
            text = font.render("{0:20}".format(self.scores[entry][0]), True, font_colour)
            pygame.Surface.blit(screen, text, (x - font_size * 10, y + entry * font_size * 1.5))
            text = font.render("{0:>20.2f}".format(float(self.scores[entry][1])), True, font_colour)
            pygame.Surface.blit(screen, text, (x + font_size * 10, y + entry * font_size * 1.5))

    # Adds a new entry to the scoreboard
    def add_entry(self, new_name, new_score):
        self.scores.append([new_name.replace(' ', '_'), str(new_score)])

    # Sorts entries by score from smallest to largest
    def sort_ascending(self):
        self.scores.sort(key=lambda x: float(x[1]))

    # Sorts entries by score from largest to smallest
    def sort_descending(self):
        self.scores.sort(reverse=True, key=lambda x: float(x[1]))

    # Returns smallest entry (both name and score)
    def get_smallest(self):
        return sorted(self.scores, key=lambda x: float(x[1]))[0]

    # Returns largest entry (both name and score)
    def get_largest(self):
        return sorted(self.scores, reverse=True, key=lambda x: float(x[1]))[0]
