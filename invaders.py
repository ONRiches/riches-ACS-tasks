import pygame
import random
import math

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

## -- Define the class Invaders which is a sprite
class Invader(pygame.sprite.Sprite):
 # Define the constructor for snow
 def __init__(self, color, width, height):
  # Call the sprite constructor
  super().__init__()
  # Create a sprite and fill it with colour
  self.image = pygame.Surface([width,height])
  self.image.fill(color)
  # Set the position of the sprite
  self.rect = self.image.get_rect()
  self.rect.x = random.randrange(0, 640)
  self.rect.y = random.randrange(-50,0)
  # Set speed of the sprite
  self.speed = random.randrange(1,2)
 #End Procedure

  # Class update function - runs for each pass through the game loop
 def update(self):
  self.rect.y = self.rect.y + self.speed

#End class

## -- Define the class player which is a sprite
class player(pygame.sprite.Sprite):
 # Define the constructor for snow
 def __init__(self, color, width, height):
  # Call the sprite constructor
  super().__init__()
  # Create a sprite and fill it with colour
  self.image = pygame.Surface([width,height])
  self.image.fill(color)
  # Set the position of the sprite
  self.rect = self.image.get_rect()
  self.rect.x = 320
  self.rect.y = 400
  # Set speed
  self.speed = 0

 def get_x(self):
  return self.rect.x

 def get_y(self):
  return self.rect.y

 def player_set_speed(self,speed):
  self.rect.x = self.rect.x + speed

 # Class update function - runs for each pass through the game loop
 def update(self):
  #self.rect.x = self.rect.x + self.speed
  print("")
#End class

# Define the class Bullet
class Bullet(pygame.sprite.Sprite):
  # Define the constructor for Invader
  def __init__(self, color, width, height):
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = player.get_x(self)
    self.rect.y = player.get_y(self)

  def update(self):
    # Shoot Bullet 
    self.rect.y = self.rect.y - 4
    pygame.sprite.groupcollide(bullet_group, invader_group, True, True)

# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")
# -- Exit game flag set to false
done = False
# Create a list of the snow blocks
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
# -- Manages how fast screen refreshes
clock = pygame.time.Clock() 
# Create the snowflakes
number_of_invaders = 10 # we are creating 10 invaders
for x in range (number_of_invaders):
 # draw the snow and make them fall at different speeds.
 my_invader = Invader(BLUE, 10, 10) # snowflakes are white with size 10 by 10 px
 invader_group.add (my_invader) # adds the new snowflake to the group of snowflakes
 all_sprites_group.add (my_invader) # adds it to the group of all Sprites
#Next x

my_player = player(YELLOW, 10, 10)
all_sprites_group.add(my_player)

def fire():
  my_bullet = Bullet(WHITE, 5, 5)
  all_sprites_group.add(my_bullet)
  bullet_group.add(my_bullet)

#Game Loop
while not done:
  # User input and controls
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        print()
      elif event.key == pygame.K_RIGHT:
        print()
      elif event.key == pygame.K_SPACE:
        print("shoot")
        fire()
    # Code that somehow makes moving smooth
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if my_player.rect.x <= 0:
            my_player.rect.x = 0
        else:
            my_player.rect.x = my_player.rect.x - 15
    if keys[pygame.K_RIGHT]:
        if my_player.rect.x >= 640:
            my_player.rect.x = 640
        else:
            my_player.rect.x = my_player.rect.x + 15

 #Next event
 # -- Game logic goes after this comment
  player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True)
  all_sprites_group.update()
 # -- Screen background is BLACK
  screen.fill (BLACK)
 # -- Draw here
  all_sprites_group.draw (screen)
 # -- flip display to reveal new position of objects
  pygame.display.flip()
 # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()