"""
Function that accepts a string and the pygame.key.get_pressed() list and returns a string with added/removed letters.
In other words, a function that gets keyboard input using pygame for typing.

I know it's really inefficient but I don't think pygame natively has an easy way to turn key input into typing.
input() does not work because it uses the console and it also pauses the program.

Contributors:
Rick
"""

import pygame
import time
delay = 0.1


def key_input(string, keys):
    output = string

    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        if keys[pygame.K_a]:
            output = output + 'A'
            time.sleep(delay)
        elif keys[pygame.K_b]:
            output = output + 'B'
            time.sleep(delay)
        elif keys[pygame.K_c]:
            output = output + 'C'
            time.sleep(delay)
        elif keys[pygame.K_d]:
            output = output + 'D'
            time.sleep(delay)
        elif keys[pygame.K_e]:
            output = output + 'E'
            time.sleep(delay)
        elif keys[pygame.K_f]:
            output = output + 'F'
            time.sleep(delay)
        elif keys[pygame.K_g]:
            output = output + 'G'
            time.sleep(delay)
        elif keys[pygame.K_h]:
            output = output + 'H'
            time.sleep(delay)
        elif keys[pygame.K_i]:
            output = output + 'I'
            time.sleep(delay)
        elif keys[pygame.K_j]:
            output = output + 'J'
            time.sleep(delay)
        elif keys[pygame.K_k]:
            output = output + 'K'
            time.sleep(delay)
        elif keys[pygame.K_l]:
            output = output + 'L'
            time.sleep(delay)
        elif keys[pygame.K_m]:
            output = output + 'M'
            time.sleep(delay)
        elif keys[pygame.K_n]:
            output = output + 'N'
            time.sleep(delay)
        elif keys[pygame.K_o]:
            output = output + 'O'
            time.sleep(delay)
        elif keys[pygame.K_p]:
            output = output + 'P'
            time.sleep(delay)
        elif keys[pygame.K_q]:
            output = output + 'Q'
            time.sleep(delay)
        elif keys[pygame.K_r]:
            output = output + 'R'
            time.sleep(delay)
        elif keys[pygame.K_s]:
            output = output + 'S'
            time.sleep(delay)
        elif keys[pygame.K_t]:
            output = output + 'T'
            time.sleep(delay)
        elif keys[pygame.K_u]:
            output = output + 'U'
            time.sleep(delay)
        elif keys[pygame.K_v]:
            output = output + 'V'
            time.sleep(delay)
        elif keys[pygame.K_w]:
            output = output + 'W'
            time.sleep(delay)
        elif keys[pygame.K_x]:
            output = output + 'X'
            time.sleep(delay)
        elif keys[pygame.K_y]:
            output = output + 'Y'
            time.sleep(delay)
        elif keys[pygame.K_z]:
            output = output + 'Z'
            time.sleep(delay)
    else:
        if keys[pygame.K_a]:
            output = output + 'a'
            time.sleep(delay)
        elif keys[pygame.K_b]:
            output = output + 'b'
            time.sleep(delay)
        elif keys[pygame.K_c]:
            output = output + 'c'
            time.sleep(delay)
        elif keys[pygame.K_d]:
            output = output + 'd'
            time.sleep(delay)
        elif keys[pygame.K_e]:
            output = output + 'e'
            time.sleep(delay)
        elif keys[pygame.K_f]:
            output = output + 'f'
            time.sleep(delay)
        elif keys[pygame.K_g]:
            output = output + 'g'
            time.sleep(delay)
        elif keys[pygame.K_h]:
            output = output + 'h'
            time.sleep(delay)
        elif keys[pygame.K_i]:
            output = output + 'i'
            time.sleep(delay)
        elif keys[pygame.K_j]:
            output = output + 'j'
            time.sleep(delay)
        elif keys[pygame.K_k]:
            output = output + 'k'
            time.sleep(delay)
        elif keys[pygame.K_l]:
            output = output + 'l'
            time.sleep(delay)
        elif keys[pygame.K_m]:
            output = output + 'm'
            time.sleep(delay)
        elif keys[pygame.K_n]:
            output = output + 'n'
            time.sleep(delay)
        elif keys[pygame.K_o]:
            output = output + 'o'
            time.sleep(delay)
        elif keys[pygame.K_p]:
            output = output + 'p'
            time.sleep(delay)
        elif keys[pygame.K_q]:
            output = output + 'q'
            time.sleep(delay)
        elif keys[pygame.K_r]:
            output = output + 'r'
            time.sleep(delay)
        elif keys[pygame.K_s]:
            output = output + 's'
            time.sleep(delay)
        elif keys[pygame.K_t]:
            output = output + 't'
            time.sleep(delay)
        elif keys[pygame.K_u]:
            output = output + 'u'
            time.sleep(delay)
        elif keys[pygame.K_v]:
            output = output + 'v'
            time.sleep(delay)
        elif keys[pygame.K_w]:
            output = output + 'w'
            time.sleep(delay)
        elif keys[pygame.K_x]:
            output = output + 'x'
            time.sleep(delay)
        elif keys[pygame.K_y]:
            output = output + 'y'
            time.sleep(delay)
        elif keys[pygame.K_z]:
            output = output + 'z'
            time.sleep(delay)

    if keys[pygame.K_SPACE]:
        output = output + ' '
        time.sleep(delay)
    elif keys[pygame.K_1]:
        output = output + '1'
        time.sleep(delay)
    elif keys[pygame.K_2]:
        output = output + '2'
        time.sleep(delay)
    elif keys[pygame.K_3]:
        output = output + '3'
        time.sleep(delay)
    elif keys[pygame.K_4]:
        output = output + '4'
        time.sleep(delay)
    elif keys[pygame.K_5]:
        output = output + '5'
        time.sleep(delay)
    elif keys[pygame.K_6]:
        output = output + '6'
        time.sleep(delay)
    elif keys[pygame.K_7]:
        output = output + '7'
        time.sleep(delay)
    elif keys[pygame.K_8]:
        output = output + '8'
        time.sleep(delay)
    elif keys[pygame.K_9]:
        output = output + '9'
        time.sleep(delay)
    elif keys[pygame.K_0]:
        output = output + '0'
        time.sleep(delay)

    if keys[pygame.K_BACKSPACE] and len(output) > 0:
        output = output[:-1]
        time.sleep(delay)

    return output
