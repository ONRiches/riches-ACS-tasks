import pygame
import random
import math
import winsound

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
  self.rect.y = random.randrange(-150,0)
  # Set speed of the sprite
  self.speed = random.randrange(1,2)
 #End Procedure

  # Class update function - runs for each pass through the game loop
 def update(self):
  self.rect.y = self.rect.y + self.speed
  self.rect.x = self.rect.x + random.randint(1,3)
  self.rect.x = self.rect.x - random.randint(1,3)

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
  self.lives = 3

 def get_x(self):
  return self.rect.x

 def get_y(self):
  return self.rect.y

 def player_set_speed(self,speed):
  self.rect.x = self.rect.x + speed

 # Class update function - runs for each pass through the game loop
 def update(self):
  print("")
  msg = "Lives: " + str(self.lives)
  self.font1 = pygame.font.SysFont('freesanbold.ttf', 24)
  self.text1 = self.font1.render(msg , True, WHITE)
  self.textRect1 = self.text1.get_rect()
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
    self.rect.x = my_player.get_x() + 5
    self.rect.y = 400

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
number_of_invaders = 20 # we are creating 10 invaders
for x in range (number_of_invaders):
 # draw the snow and make them fall at different speeds.
 my_invader = Invader(BLUE, 15, 5) # snowflakes are white with size 10 by 10 px
 invader_group.add (my_invader) # adds the new snowflake to the group of snowflakes
 all_sprites_group.add (my_invader) # adds it to the group of all Sprites
#Next x

my_player = player(YELLOW, 15, 15)
all_sprites_group.add(my_player)

def fire():
  my_bullet = Bullet(WHITE, 5, 10)
  all_sprites_group.add(my_bullet)
  bullet_group.add(my_bullet)

#Game Loop
while not done:
  # User input and controls
 for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (my_player.lives == 0):
     done = True 
    elif event.type == pygame.KEYDOWN: # - a key is down 
        if event.key == pygame.K_LEFT: # - if the left key pressed
            my_player.player_set_speed(-3) # speed set to 3
        elif event.key == pygame.K_RIGHT: # - if the right key pressed
            my_player.player_set_speed(3) # speed set to -3
        elif event.key == pygame.K_UP:
            player.get_x(my_player)
            fire()

    elif event.type == pygame.KEYUP: # - a key released 
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
            my_player.player_set_speed(0) # speed set to 0

 #Next event
 # -- Game logic goes after this comment
 player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True)
 all_sprites_group.update()
 for z in player_hit_group: 
  my_player.lives = my_player.lives - 1
  winsound.Beep(1000,1000)
 # -- Screen background is BLACK
 screen.fill (BLACK)
 # -- Draw here
 all_sprites_group.draw (screen)
 screen.blit(my_player.text1, my_player.textRect1)
 # -- flip display to reveal new position of objects
 pygame.display.flip()
 # - The clock ticks over
 clock.tick(60)
#End While - End of game loop
pygame.quit()