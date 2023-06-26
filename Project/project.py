import pygame

# -- Global Constants
GRAVITY = 9.8
VERTSPEED = 20

# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)

# -- Classes
class player(pygame.sprite.Sprite):
    # --- Constructor Function ---
    def __init__(self, width, height):
        super().__init__()

        # --- Create Player ---
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)

        # --- Set Player Position ---
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 835

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def playerSetSpeed(self, speed):
        self.rect.x = self.rect.x + speed

    def moveRight(self):
        player.playerSetSpeed(myplayer, 3)

    def moveLeft(self):
        player.playerSetSpeed(myplayer, -3)

    def stop(self):
        player.playerSetSpeed(myplayer, 0)

    def jump(self,jumpspeed):
        jumpstrength = jumpspeed
        while self.rect.x < 900:
            self.rect.x = self.rect.x + jumpstrength
            jumpstrength = jumpstrength - 1 



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


# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (1440, 900)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

allspritegroup = pygame.sprite.Group()
platformgroup = pygame.sprite.Group()


myplayer = player(50, 50)
platform1 = platform(200, 25, WHITE, 500, 500)
platform2 = platform(100, 25, WHITE, 900, 300)


allspritegroup.add(myplayer)
platformgroup.add(platform1)
platformgroup.add(platform2)
allspritegroup.add(platformgroup)

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # End If
        # Next event
        # -- Game logic goes after this comment
        allspritegroup.update()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if myplayer.rect.x < 0:
            myplayer.rect.x = 0
        else:
            myplayer.rect.x = myplayer.rect.x - 15
    if keys[pygame.K_RIGHT]:
        if myplayer.rect.x >= 1440 - 50:
            myplayer.rect.x = 1440 - 50
        else:
            myplayer.rect.x = myplayer.rect.x + 15
    if keys[pygame.K_UP]:
        while myplayer.rect.x < 900:
            myplayer.rect.x = myplayer.rect.x + VERTSPEED
            VERTSPEED = VERTSPEED - GRAVITY 
        

    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    allspritegroup.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
# End While - End of game loop
pygame.quit()
