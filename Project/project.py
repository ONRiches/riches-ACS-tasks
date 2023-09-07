import pygame
import math
vec = pygame.math.Vector2

# -- Global Constants
GRAVITY = 8
JUMPSPEED = -20

Width = 768
Height = 432

FPS = 60

scroll = 0

# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)

# -- Classes

class Background():

    def __init__(self):
        self.ground_image = pygame.image.load("Project/Images/ground.png").convert_alpha()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

        self.bg_images = []
        for i in range(1, 6):
            self.bg_image = pygame.image.load(f"Project/Images/plx-{i}.png").convert_alpha()
            self.bg_images.append(self.bg_image)
        self.bg_width = self.bg_images[0].get_width()


    def draw_bg(self):
        for x in range(1000):
            speed = 1
            for i in self.bg_images:
                screen.blit(i, ((x * self.bg_width) - scroll * speed, 0))
                speed += 0.2

    def draw_ground(self):
        for x in range(1000):
            screen.blit(self.ground_image, ((x * self.ground_width) - scroll * 2.5, Height - self.ground_height))

    def get_ground_height(self):
        return self.ground_height


class player(pygame.sprite.Sprite):
    # --- Constructor Function ---
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # --- Create Player ---
        self.image = pygame.Surface((10, 20))
        self.image.fill(WHITE)

        # --- Set Player Position ---
        self.rect = self.image.get_rect()
        self.rect.x = Width / 3
        self.rect.y = Height - 60 - 20

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
        self.playerSetSpeed(myplayer, 3)

    def moveLeft(self):
        self.playerSetSpeed(myplayer, -3)

    def stop(self):
        self.playerSetSpeed(myplayer, 0)

    def checkMoving(self):
        if self.getVertSpeed(self) == 0:
            return False
        else:
            return True

    def jump(self,vertSpeed):
            self.vel = vertSpeed
     #   while self.checkCollision == True:
            self.rect.y = self.rect.y + self.vel
            self.vel = self.vel - GRAVITY
            allspritegroup.draw

    def checkCollision(self):
        if self.rect.colliderect(myplayer.rect):
            return True
        
    def jumpinit(self,vertSpeed):
        if self.checkCollision() == True:
            self.jump(vertSpeed)
       


class platform(pygame.sprite.Sprite):
    # --- Constructor Function ---
    def __init__(self, width, height, color, posX, posY):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # --- Create Platform ---
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # --- Set Platform Position ---
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

class coins(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)



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

bg = Background()

playergroup.add(myplayer)
allspritegroup.add(myplayer)
allspritegroup.add(platformgroup)

# -- Game Loop --
while not done:

    clock.tick(FPS)

    bg.draw_bg()
    bg.draw_ground()

    scroll += 2

    # -- User input and controls
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        # End If

    # Next Event


        # -- Game logic goes after this comment
        allspritegroup.update()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        myplayer.jumpinit(JUMPSPEED)

    # -- Prevent player from falling through the floor --
    if myplayer.rect.y <= Height - 62 - 20:
        myplayer.rect.y = myplayer.rect.y + GRAVITY


   # screen.fill(BLACK)
    pygame.display.update()
    # -- Draw here
    allspritegroup.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
# End While - End of game loop
pygame.quit()