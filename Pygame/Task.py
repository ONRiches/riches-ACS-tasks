import pygame
import math

# -- Global Constants
done = False
sun_x = 40
sun_y = 100

center_x = 320 # x pos in relation to screen width
center_y = 480 # y pos in relation to screen height
radius = 300
angle = -90 #pi / 4 # starting angle 45 degrees
omega = .001 #Angular velocity

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop

while not done:
 # -- User input and controls
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
    #End If
 #Next event
 # -- Game logic goes after this comment

 #   sun_x = center_x + (math.cos(angle) * radius)
 #   sun_y = center_y + (math.sin(angle) * radius)

 sun_x = sun_x + 2

 if sun_x < 320:
    sun_y = sun_y - 0.5
 #End if

 if sun_x > 320:
    sun_y = sun_y + 0.5
 #End if

 # -- Screen background is BLACK
 screen.fill (BLACK)
 # -- Draw here
 pygame.draw.rect(screen, BLUE, (220,165,200,150))
 pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)

 # -- flip display to reveal new position of objects
 pygame.display.flip()
 # - The clock ticks over
 clock.tick(60)
#End While - End of game loop
pygame.quit()