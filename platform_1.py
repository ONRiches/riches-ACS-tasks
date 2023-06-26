import pygame
# -- Global Constants
gravity = -0.5
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


class player(pygame.sprite.Sprite):
   def __init__(self, color, width, height):
      super().__init__()

      self.image = pygame.Surface([width,height])
      self.image.fill(color)

      self.rect = self.image.get_rect()
      self.rect.x = 5
      self.rect.y = 380
      self.b = self.rect.y - height

      self.jumpSpeed = 5
      self.moveSpeed = 3

   def jump(self):
      if self.b <= 400:
         self.rect.y = self.rect.y - self.jumpSpeed
         self.jumpSpeed = self.jumpSpeed + gravity

   def moveright(self):
      self.rect.x = self.rect.x + self.moveSpeed

   def moveleft(self):
      self.rect.x =self.rect.x - self.moveSpeed

   def ismoving(self):
      if self.b < 400:
         return True


  # def update():
      
   
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (600,400)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock() 

all_sprites_group = pygame.sprite.Group()

player1 = player(BLUE,20,20)
all_sprites_group.add(player1)

### -- Game Loop
while not done:
 # -- User input and controls
 for event in pygame.event.get():
    if (event.type == pygame.QUIT):
     done = True 
    elif event.type == pygame.KEYDOWN: # - a key is down
        if event.key == pygame.K_SPACE:
         while player1.ismoving() == True:
            player1.jump()

#End If
 #Next event
 # -- Game logic goes after this comment
 # -- Screen background is BLACK
 screen.fill (BLACK)
 # -- Draw here
 pygame.draw.rect(screen, WHITE, (350,125,125,25))
 pygame.draw.rect(screen, WHITE, (200,250,125,25))
 all_sprites_group.draw(screen)
 # -- flip display to reveal new position of objects
 pygame.display.flip()
 # - The clock ticks over
 clock.tick(60)
#End While - End of game loop
pygame.quit()