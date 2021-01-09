# Liaison ** wasn't commented by liaison

import pygame
p = pygame
p.init()

screen_width = pygame.display.get_surface().get_size()[0]
screen_height = pygame.display.get_surface().get_size()[1]

run = True

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def render_text(text, size, position, colour):  # bliting function
    font = pygame.font.SysFont("Times New Roman", size)  # makes font
    text = font.render(text, True, colour)  # renders text
    screen.blit(text, position)  # displays text


def instruction_screen(path):
    with open(path) as instructions:
        Instruction = open(path, 'r')  # opening the file
        line_num = 0 # set line number
        for line in Instruction.readlines():
            if line_num == 0: # if first line
                render_text(line.strip(), int(screen_width * 0.0425), (screen_width * 0.02, screen_height * 0.01), (255, 255, 255)) # draws title (use own function here but keep line.strip())
            else: # if any other line
                render_text(line.strip(),int(screen_width * 0.025), (screen_width * 0.02, line_num * screen_height * 0.05 + screen_height * 0.05), (255, 255, 255)) # draws main text (use own function here but keep line.strip())
            line_num += 1 # changes line


instruction_screen('instructions.txt')  # calling file (change to be path to your file)
p.display.flip()  # update screen

for event in pygame.event.get():
    if event.type == pygame.QUIT:  # so as not to error out
        run = False

#pygame.quit()  # closing the screen