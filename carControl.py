"""
This class handles the car itself as well as the checkpoints and collision detection.

Contributors:
Rick - Car Velocity/Acceleration, reset function
Siddharth - Everything else (off screen detection, off road detection, checkpoint detection, center of car detection,
etc)
"""

# import the necessary modules (images, python, math)
import pygame
from images import *
import math
from images import car_image

# set the screen size to a set of variables
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = pygame.display.get_surface().get_size()[0]
screen_height = pygame.display.get_surface().get_size()[1]
width = screen_width // 2
height = screen_height //2

# create a class for the player's car
class Car:
    def __init__(self,x_pos,y_pos,x_change, y_change):
        # these variables store the initial coordinates of the car
        self.initial_x = x_pos
        self.initial_y = y_pos

        # these variables set the x and y coordinate of the car
        self.x_pos = x_pos
        self.y_pos = y_pos

        #self.x_cen = self.x_pos + 25
        #self.y_cen = self.y_pos + 12
        self.x_cen = self.x_pos
        self.y_cen = self.y_pos

        # these variables change the x and y position of the car
        self.x_change = x_change
        self.y_change = y_change

        # this is the initial angle of the car (flat to the horizon)
        self.angle = 180

        # this variable is a flag to signal when the car passes through a checkpoint (1=not passes, 2 = passed)
        self.flag = [1,1,1,1,1,1,1,1]

        # this variable is used to check whether the user passes all the checkpoints
        self.final_check = True

        # this is the initial velocity of the car
        self.velocity = 0

    def move(self):

        """this function is used to move the plyaer car, and establishes the boundaries in which the car will
        slow down if the car passes the borders"""

        # these lines save the conditions in which the car is out of bounds
        # the conditions see if the car's x,y coordinate in the given square
        out_one = self.x_cen >= 0 and self.x_cen <= width-455 and self.y_cen >= 0 and self.y_cen <= height*2
        out_two = self.x_cen >= width-455 and self.x_cen <= width*2 and self.y_cen >= 0 and self.y_cen <= height - 326
        out_three = self.x_cen >= width+235 and self.x_cen <= width*2 and self.y_cen >= 0 and self.y_cen <= height - 135
        out_four = self.x_cen >= width + 483 and self.x_cen <= width*2 and self.y_cen >= 0 and self.y_cen <= height*2
        out_five = self.x_cen >= 0 and self.x_cen <= width*2 and self.y_cen >= height + 307 and self.y_cen <= height*2
        out_six = self.x_cen >= 0 and self.x_cen <= width-350 and self.y_cen >= height + 28 and self.y_cen <= height*2
        out_seven = self.x_cen >= width-332 and self.x_cen <= width+115 and self.y_cen >= height-217 and self.y_cen <= height-79
        out_eight = self.x_cen >= width-227 and self.x_cen <= width+115 and self.y_cen >= height - 79 and self.y_cen <= height+185
        out_nine = self.x_cen >= width+115 and self.x_cen <= width+360 and self.y_cen >= height - 20 and self.y_cen <= height+185

        # if the car's x,y position meets any of the conditions above, make the velocity 0.5 (slow)
        if out_one or out_two or out_three or out_four or out_five or out_six or out_seven or out_eight or out_nine:
            self.velocity = self.velocity * 0.9

        # set variables that are used for the key commands to control the car
        keys = pygame.key.get_pressed()
        LEFT = keys[pygame.K_a]
        RIGHT = keys[pygame.K_d]
        FORWARD = keys[pygame.K_w]
        STOP = keys[pygame.K_s]

        # if the velocity is less than 10 and the user presses the forward key, increase the velocity
        if FORWARD:
            self.velocity += 0.1

        # if the user presses the S key, increase the angle by 5
        if LEFT:
            self.angle += 4

        # if the user presses the D key, decrease the angle by 5
        if RIGHT:
            self.angle -= 4

        # if the user presses the S button, and the velocity is greater than 0, decrease the velocity
        if STOP:
            self.velocity -= 0.1

        # if the velocity of the car is greater than 0, then multiply it by 0.99
        if self.velocity > 0:
            self.velocity = self.velocity * 0.99

        # if the velocity is less than 0, multiply it by 0.95
        elif self.velocity < 0:
            self.velocity = self.velocity * 0.95

        # rotate the image for the given angle
        pygame.transform.rotate(car_image, self.angle)

        # set the change in the x,y position of the car (components of the trig. circle, multiplied by velocity)
        self.x_change = math.cos(math.radians(self.angle)) * self.velocity
        self.y_change = math.sin(math.radians(self.angle)) * self.velocity

        # if the magnitude of the y_change is greater than the magnitude of the x_change then...
        if abs(self.y_change) > abs(self.x_change):
            # ... set the x-center of the car to the x position + 12
            self.x_cen = self.x_pos + 12
            # ... set the y-center of the car to the y position + 25
            self.y_cen = self.y_pos + 25

        # if the magnitude of the y_change is less than the magnitude of the x_change then...
        if abs(self.y_change) < abs(self.x_change):
            # make the x-center of the car the x position + 25
            self.x_cen = self.x_pos + 25

            # make the y-center of the car the y position + 12
            self.y_cen = self.y_pos + 12

        # if the two magnitudes of the x and y change are the same...
        if abs(self.y_change) == abs(self.x_change):
            # set the x and y centers to the x and y position, + 17
            self.x_cen = self.x_pos + 17
            self.y_cen = self.y_pos + 17

        # off screen detection

        # if the car is beyond or at the left border, and it's direction is towards the left, pass the body of code
        if self.x_pos <= 0 and self.x_change < 0:
            pass
        # if the car is beyond or at the right border, and its direction si towards the right, pass the bod of code
        elif self.x_pos+50 >= width*2 and self.x_change > 0:
            pass

        # if the above conditions are false, change the x_position of the car
        else:
            self.x_pos += self.x_change
            self.x_cen += self.x_change

        # if the car is at the top border of the screen and it's direction is up, then pass the body of code
        if self.y_pos <= 0 and self.y_change > 0:
            pass

        # if the car is at the bottom of the screen and it's direction is down, then pass the body of code
        elif self.y_pos + 50 >= height*2 and self.y_change < 0 :
            pass

        # if the above conditions are false, then change the y position
        else:
            self.y_pos -= self.y_change
            self.y_cen -= self.y_change

        # set the rotation of the car to driver, and blit driver to the screen
        drive = pygame.transform.rotate(car_image, self.angle)
        screen.blit(drive, (self.x_pos, self.y_pos))

    def detect(self):
        """This function is used to detect whether the car passes over a checkpoint"""

        # this checks if the car passes over the first checkpoint, and sets the first element of flag to 2
        if self.x_cen >= width - 50 and self.x_cen <= width - 30 and self.y_cen >= height + 197 and self.y_cen <= height + 290:
            self.flag[0] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[0] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width - 50, height + 197, 20, 93))

        # this checks if the car passes over the third checkpoint, and sets the second element of flag to 2
        if self.x_cen >= width-346 and self.x_cen <= width - 326 and self.y_cen >= height - 72 and self.y_cen <= height + 18:
            self.flag[1] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[1] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width - 346, height - 72, 20, 90))

        # this checks if the car passes over the fifth checkpoint, and sets the third element of flag to 2
        if self.x_cen >= width-100 and self.x_cen <= width-80 and self.y_cen >= height-316 and self.y_cen <= height-226:
            self.flag[2] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[2] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width - 100, height - 316, 20, 90))

        # this checks if the car passes over the seventh checkpoint, and sets the fourth element of flag to 2
        if self.x_cen >= width+300 and self.x_cen <= width +320 and self.y_cen >= height-120 and self.y_cen <= height - 30:
            self.flag[3] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[3] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width + 300, height - 120, 20, 90))

        # this checks if the car passes over the second checkpoint, and sets the fifth element of flag to 2
        if self.x_cen >= width-339 and self.x_cen <= width -237 and self.y_cen >= height +100 and self.y_cen <= height + 120:
            self.flag[4] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[4] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width - 339, height + 100, 102, 20))

        # this checks if the car passes over the fourth checkpoint, and sets the sixth element of flag to 2
        if self.x_cen >= width-441 and self.x_cen <= width -345 and self.y_cen >= height-150 and self.y_cen <= height - 130:
            self.flag[5] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[5] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width -441, height -150, 96, 20))

        # this checks if the car passes over the sixth checkpoint, and sets the seventh element of flag to 2
        if self.x_cen >= width+125 and self.x_cen <= width +221 and self.y_cen >= height-170 and self.y_cen <= height - 150:
            self.flag[6] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[6] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width + 125, height -170, 96, 20))

        # this checks if the car passes over the last checkpoint, and sets the eighth element of flag to 2
        if self.x_cen >= width+373 and self.x_cen <= width + 469 and self.y_cen >= height+100 and self.y_cen <= height + 120:
            self.flag[7] = 2

        # if the flag is 2, then draw a green rectangle over the checkpoint
        if self.flag[7] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (width + 373, height + 100, 96, 20))

    def checker(self):
        """this function checks if the car passes through all the checkpoints"""

        # if the car is at the finish line, run the following code
        if self.x_cen >= width + 205 and self.x_cen <= width + 225 and self.y_cen >= height+197 and self.y_cen <= height + 297:

            # this sets finished to True
            finished = True

            # make a for loop checking all 8 checkpoints
            for i in range(8):

                # if the given flag element is not 2, then make finished be False
                if self.flag[i] != 2:
                    finished = False
                    break

            # if finished is True, then return the value
            if finished == True:
                return finished

    # resets all of the car's variables
    def reset(self):
        self.x_pos = self.initial_x
        self.y_pos = self.initial_y
        self.x_change = 0
        self.y_change = 0
        self.x_cen = self.x_pos+25
        self.y_cen = self.y_pos + 12
        self.angle = 180
        self.flag = [1,1,1,1,1,1,1,1]
        self.final_check = True
        self.velocity = 0