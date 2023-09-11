import pygame
import math
import random
vec = pygame.math.Vector2
pygame.font.init()

# -- Global Constants --

GRAVITY = 4
JUMPSPEED = -10

BGSPEED = 1
FGSPEED = 2.5
COINSPEED = -5.5

SPEEDMOD = 1

Width = 768
Height = 432

FPS = 60

scroll = 0

MaxCoins = 25

font1 = pygame.font.Font('Project/Fonts/04B_30__.TTF', 30)

# -- Sprite Groups --

allspritegroup = pygame.sprite.Group()
barriergroup = pygame.sprite.Group()
coingroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()

# -- Colours --
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
            speed = BGSPEED
            for i in self.bg_images:
                screen.blit(i, ((x * self.bg_width) - scroll * speed, 0))
                speed += 0.2

    def draw_ground(self):
        for x in range(1000):
            screen.blit(self.ground_image, ((x * self.ground_width) - scroll * FGSPEED, Height - self.ground_height))

    def get_ground_height(self):
        return self.ground_height
    

class Menu():

    def __init__(self):
        count = 1
    
    def openmenu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Pause")
    


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
#        self.image.height = self.image.get_height()
 #       self.image.width = self.image.get_width()

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print("oaengowjro")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action



class Scoreboard():

    def __init__(self):
        self.score = 0

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def pickupcoins(self):
        if pygame.sprite.spritecollide(myplayer, coingroup, True):
            self.score += 1
        score = str(self.score)
        if self.score > 99:
            self.draw_text(score, font1, WHITE, Width - 85, 20)
        elif self.score > 9:
            self.draw_text(score, font1, WHITE, Width - 65, 20)
        else:
            self.draw_text(score, font1, WHITE, Width - 45, 20)

    def checkplayercollision(self):
        if pygame.sprite.groupcollide(playergroup, barriergroup, True, False):
            pygame.quit()
            print("oof")

    def checkcoincollision(self):
        if pygame.sprite.groupcollide(barriergroup, coingroup, False, True):
            coingroup.empty()



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
            self.rect.y += vertSpeed

    def checkCollision(self):
        if self.rect.colliderect(myplayer.rect):
            return True
        
    def jumpinit(self,vertSpeed):
        if self.checkCollision() == True:
            self.jump(vertSpeed)
       


class Barrier(pygame.sprite.Sprite):
    # --- Constructor Function ---
    def __init__(self, width, height, posX, posY):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Project/Images/SpikyStick.png")
        self.image = pygame.transform.scale(img, (width, height))
    #    self.image = pygame.Surface((width, height))
    #    self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    def spawn():
        if len(barriergroup) < 2:
            barrierx = random.randint(800,1700)
            nbarriers = random.randint(3,7)
            barriergap = random.randint(170, 230)
            for i in range(1, nbarriers):
                if i % 2 == 0:
                    newbarrier = Barrier(75, 200, barrierx + (i * barriergap), -5)
                    barriergroup.add(newbarrier)
                else:
                    newbarrier = Barrier(75, 200, barrierx + (i * barriergap), Height - 195)
                    barriergroup.add(newbarrier)

    def update(self):
        self.rect.move_ip(COINSPEED * SPEEDMOD, 0)
        if self.rect.x < -75:
            self.kill()



class Coins(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Project/Images/coin.png")
        self.image = pygame.transform.scale(img, (15,15))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.rect.x = x
        self.rect.y = y

    def spawn():
        while len(coingroup) == 0:
            coinx = random.randint(1000, 2500)
            coiny = random.randint(40, Height - 100)
            coing = random.randint(5, 17)
            stepback = random.randint(1,8) * 10
            for i in range(0, coing):
                newcoin = Coins(coinx + i * 20, coiny)
                coingroup.add(newcoin)
            for j in range(0, 25 - coing):
                newcoin = Coins(coinx + (j * 20) - 60, coiny + 20)
                coingroup.add(newcoin)

    def movecoins(self):
        self.rect.x -= 1

    def update(self):
        self.rect.move_ip(COINSPEED * SPEEDMOD, 0)
        if self.rect.x < -50:
            self.kill()

# -- Initialise PyGame --
pygame.init()
# -- Blank Screen --
size = (Width, Height)
screen = pygame.display.set_mode(size)
# -- Variables --
game_paused = False
# -- Title of new window/screen --
pygame.display.set_caption("My Window")
# -- Exit game flag set to false --
done = False
# -- Manages how fast screen refreshes --
clock = pygame.time.Clock()


myplayer = player()

scoreboard = Scoreboard()

bg = Background()

startbutton = Button(53, 153, pygame.image.load('Project/Images/start_btn.png').convert_alpha())
endbutton = Button(456, 153, pygame.image.load('Project/Images/exit_btn.png').convert_alpha())

playergroup.add(myplayer)
allspritegroup.add(playergroup)
allspritegroup.add(barriergroup)
allspritegroup.add(coingroup)

# -- Game Loop --
while not done:

    if game_paused == True:

        if startbutton.draw() == True:
            game_paused = False
        
        if endbutton.draw() == True:
            pygame.quit()


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Pause")
                    game_paused = False
    else:
        clock.tick(FPS)

        bg.draw_bg()
        bg.draw_ground()

        scroll += 2
        SPEEDMOD = SPEEDMOD * scoreboard.score / 200 + 1

        Coins.spawn()
        Barrier.spawn()

        # -- Fly --
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            myplayer.jumpinit(JUMPSPEED)

        # -- Prevent player from falling through the floor --
        if myplayer.rect.y <= Height - 62 - 20:
            myplayer.rect.y = myplayer.rect.y + GRAVITY

        # -- User input and controls
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Pause")
                    game_paused = True
            # End If

        # Next Event

        #pygame.display.update()

        # -- Draw here
        playergroup.draw(screen)
        coingroup.draw(screen)
        barriergroup.draw(screen)

        allspritegroup.update()
        coingroup.update()
        barriergroup.update()

        scoreboard.pickupcoins()
        scoreboard.checkcoincollision()
        scoreboard.checkplayercollision()

    # -- flip display to reveal new position of objects
    pygame.display.flip()

# End While - End of game loop
pygame.quit()