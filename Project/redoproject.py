import pygame
import random
import os
from typing import Any

FPS = 60
GRAVITY = 5
JUMPSPEED = -10
scroll = 0
BGSPEED = 1
FGSPEED = 2.5

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

class Background():

    # --- Constructor ---
    def __init__(self):

        # Load the image of the ground
        self.ground_image = pygame.image.load("Project/Images/ground.png").convert_alpha()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

        # Create a list to hold the 6 background images
        self.bg_images = []

        for i in range(1, 6):
            # Load each of the 6 background images
            self.bg_image = pygame.image.load(f"Project/Images/plx-{i}.png").convert_alpha()
            # Add them to the list
            self.bg_images.append(self.bg_image)
        # Next i

        # Find the width of one of the background images  
        self.bg_width = self.bg_images[0].get_width()

    # --- Functions ---

    # --- Draw the moving background --- 
    def draw_bg(self):

        # Draw the background so many times it will never reach the end
        for x in range(1000):

            # Set the speed of the background
            speed = BGSPEED

            # Iterate between the images in the list
            for i in self.bg_images:

                # Move the background images at different speeds
                screen.blit(i, ((x * self.bg_width) - scroll * speed, 0))
                speed += 0.2

            # Next i

    # --- Draw the ground ---
    def draw_ground(self):
        # Draw the ground so many times that it will never reach the end
        for x in range(1000):
            screen.blit(self.ground_image, ((x * self.ground_width) - scroll * FGSPEED, Height - self.ground_height))
        # Next x

    # --- Get the height of the ground image ---
    def get_ground_height(self):
        return self.ground_height



class Player(pygame.sprite.Sprite):

    # --- Constructor Function ---
    def __init__(self):

        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Set the player as a placholder rectangle
        self.image = pygame.Surface((10,20))
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

bg = Background()

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

    # Draw Background
    bg.draw_bg()

    # Draw the ground
    bg.draw_ground()

    # Set the necessary speeds of background and objects
    scroll += 2

    # Draw the objects on the screen
    allspritegroup.draw(screen)

    # Update all objects
    allspritegroup.update()

    # Flip display to reveal new position of objects
    pygame.display.flip()

    # Set the game speed
    clock.tick(FPS)

# End While - End of game loop
pygame.quit()