import pygame
import math
vec = pygame.math.Vector2

# -- Global Constants
GRAVITY = 8
JUMPSPEED = -20

Width = 1200
Height = 600

bg = pygame.image.load("Project/TreesBG.jpg").convert

# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)

# -- Classes
class player(pygame.sprite.Sprite):
    # --- Constructor Function ---
    def __init__(self):
        super().__init__()

        # --- Create Player ---
        self.image = pygame.Surface((30, 50))
        self.image.fill(WHITE)

        # --- Set Player Position ---
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 550

    # --- Functions ---

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y
    
    def getVertSpeed(self):
        return self.vel

    def playerSetSpeed(self, speed):
        self.rect.x = self.rect.x + speed

    def moveRight(self):
        player.playerSetSpeed(myplayer, 3)

    def moveLeft(self):
        player.playerSetSpeed(myplayer, -3)

    def stop(self):
        player.playerSetSpeed(myplayer, 0)

    def checkMoving(self):
        if player.getVertSpeed(self) == 0:
            return False
        else:
            return True
        
    def jumpinit(self,vertSpeed):
        if player.checkCollision(self) == True:
            self.jump(vertSpeed)

    def jump(self,vertSpeed):
            self.vel = vertSpeed
     #   while self.checkCollision == True:
            self.rect.y = self.rect.y + self.vel
            self.vel = self.vel - GRAVITY
            allspritegroup.draw

    def checkCollision(self):
        if self.rect.colliderect(myplayer.rect):
            return True
       


class platform(pygame.sprite.Sprite):
    # --- Constructor Function ---
    def __init__(self, width, height, color, posX, posY):
        super().__init__()

        # --- Create Platform ---
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # --- Set Platform Position ---
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY


# -- Initialise PyGame --
pygame.init()
# -- Blank Screen --
size = (Width, Height)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen --
pygame.display.set_caption("My Window")
# -- Exit game flag set to false --
done = False
# -- Manages how fast screen refreshes --
clock = pygame.time.Clock()

allspritegroup = pygame.sprite.Group()
platformgroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()


myplayer = player()
#platform1 = platform(200, 25, WHITE, 500, 500)
#platform2 = platform(100, 25, WHITE, 900, 300)

playergroup.add(myplayer)
allspritegroup.add(myplayer)
#platformgroup.add(platform1)
#platformgroup.add(platform2)
#allspritegroup.add(platformgroup)


# -- Load image for the background, and change size to screen size --
bg1 = pygame.image.load("Project/TreesBG.jpg").convert()
bg = pygame.transform.scale(bg1, (Width, Height))
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(Width / bg_width) + 1

# -- Game Loop --
while not done:


    # -- Scroll the background image --
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0



    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # End If
        # Next event
        # -- Game logic goes after this comment
        allspritegroup.update()
    
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT]:
        #if myplayer.rect.x < 0:
         #   myplayer.rect.x = 0
        #else:
         #   myplayer.rect.x = myplayer.rect.x - 15
    #if keys[pygame.K_RIGHT]:
        #if myplayer.rect.x >= 1440 - 50:
         #   myplayer.rect.x = 1440 - 50
        #else:
         #   myplayer.rect.x = myplayer.rect.x + 15
    if keys[pygame.K_UP]:
        myplayer.jumpinit(JUMPSPEED)

    # -- Prevent player from falling through the floor --
    if myplayer.rect.y < 550:
        myplayer.rect.y = myplayer.rect.y + GRAVITY

        

    # -- Screen background is BLACK
   # screen.fill(BLACK)
    pygame.display.update()
    # -- Draw here
    allspritegroup.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
