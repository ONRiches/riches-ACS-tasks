import pygame
import random
import os
from typing import Any

FPS = 60
GRAVITY = 5
JUMPSPEED = -10

# --- Screen Dimensions ---

Width = 768
Height = 432

# --- Colours ---

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (225, 0, 0)

# --- Sprite Groups ---

allspritegroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()

# --- Classes ---

class Player(pygame.sprite.Sprite):

    # --- Constructor Function ---
    def __init__(self):

        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Set the player as a placholder rectangle
        self.image = pygame.Surface((20, 50))
        self.image.fill(WHITE)

        # Set Player Position
        self.rect = self.image.get_rect()
        self.rect.x = Width / 3
        self.rect.y = Height - 60 - 20

    # --- Functions ---

    # --- x value getter ---
    def get_x(self):
        return self.rect.x

    # --- y value getter ---
    def get_y(self):
        return self.rect.y

    # --- Fly ---
    def fly(self,vertSpeed):

        # If the player is below the top of the screen move the player up
        if self.rect.y > 0:
            self.rect.y += vertSpeed
        # End if


# --- Initialise Pygame ---

pygame.init()

# --- Blank Screen ---

size = (Width, Height)
screen = pygame.display.set_mode(size)

# --- Title of window ---

pygame.display.set_caption("My Window")

# --- Exit game flag set to false ---

done = False

# --- Manage how fast screen refreshes ---

clock = pygame.time.Clock()

# --- Instantiate Objects ---

myplayer = Player()

# --- Add new objects to sprite groups ---

playergroup.add(myplayer)

# --- Add all the sprite groups to one common group ---

allspritegroup.add(playergroup)


# --- Game Loop ---
while not done:

    # User input and controls
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        # End if
    # Next

    # If the up key is pressed then fly
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        myplayer.fly(JUMPSPEED)
    # End if

    # Prevent player from falling through the floor
    if myplayer.rect.y <= Height - 62 - 20:
        myplayer.rect.y = myplayer.rect.y + GRAVITY
    # End if

    # Draw the objects on the screen
    allspritegroup.draw(screen)

    # Update all objects
    allspritegroup.update()

    # Draw Background
    screen.fill(BLACK)

    # Flip display to reveal new position of objects
    pygame.display.flip()

    # Set the game speed
    clock.tick(FPS)

# End While - End of game loop
pygame.quit()