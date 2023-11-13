from typing import Any
import pygame
import math
import random
import os
vec = pygame.math.Vector2
pygame.font.init()
pygame.display.init()

# -- Global Constants --

GRAVITY = 4
JUMPSPEED = -10

# --- Speed Modifiers ---
BGSPEED = 1
FGSPEED = 2.5
COINSPEED = -5.5
SPEEDMOD = 1
scroll = 0

# --- Screen dimensions ---
Width = 768
Height = 432

# --- Misc Constants ---
FPS = 60
MaxCoins = 25

# --- Fonts ---
font1 = pygame.font.Font('Project/Fonts/04B_30__.TTF', 30)
font2 = pygame.font.Font('Project/Fonts/04B_30__.TTF', 15)
font3 = pygame.font.Font('Project/Fonts/04B_30__.TTF', 40)
font4 = pygame.font.Font('Project/Fonts/04B_30__.TTF', 22)

#sprite_sheet_image = pygame.image.load('Project/Images/BarryFullSpriteSheet.png').convert_alpha()
#sprite_sheet = spritesheet.Spritesheet(sprite_sheet_image)

# --- Load the highscore ---
if os.path.exists('Project/highscore.txt'):
    with open('Project/highscore.txt', 'r') as file:
        high_score = file.read()
else:
    high_score = 0

# --- Set a new highscore variable that can be changed whilst keeping the original score ---
original_high_score = high_score

# -- Sprite Groups --

allspritegroup = pygame.sprite.Group()
lasergroup = pygame.sprite.Group()
barriergroup = pygame.sprite.Group()
coingroup = pygame.sprite.Group()
warninggroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()
firegroup = pygame.sprite.Group()

# -- Colours --
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (225, 0, 0)

# -- Classes ---

class Background():

    # --- Constructor ---
    def __init__(self):
        self.ground_image = pygame.image.load("Project/Images/ground.png").convert_alpha()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

        self.bg_images = []
        for i in range(1, 6):
            # --- Load each of the 6 background images ---
            self.bg_image = pygame.image.load(f"Project/Images/plx-{i}.png").convert_alpha()
            self.bg_images.append(self.bg_image)
        self.bg_width = self.bg_images[0].get_width()

    # --- Draw the moving background --- 
    def draw_bg(self):
        for x in range(1000):
            # --- Set the speed of the background ---
            speed = BGSPEED
            for i in self.bg_images:
                # --- Move the background images at different speeds ---
                screen.blit(i, ((x * self.bg_width) - scroll * speed, 0))
                speed += 0.2

    # --- Draw the ground ---
    def draw_ground(self):
        for x in range(1000):
            screen.blit(self.ground_image, ((x * self.ground_width) - scroll * FGSPEED, Height - self.ground_height))

    def get_ground_height(self):
        return self.ground_height
    

class Menu():

    def __init__(self):
        count = 1
    
    # --- Pause function ---
    def openmenu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Pause")

    # --- Cover the background if dead ---
    def deathscreen(self):
        screen.fill(BLACK)

    # --- Quit from death screen ---
    def checkplay(self):
        self.deathscreen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('hahaha')
                    pygame.QUIT()

    # --- Start function ---
    def start(self):
        myplayer = player()
        playergroup.add(myplayer)
        allspritegroup.add(playergroup)
        
    


class Button():

    # --- Constructor ---
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # --- Draw the buttons for menus ---
    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        # --- Check for button clicks ---
        if self.rect.collidepoint(pos):
            # --- Make sure the button can only be pressed once ---
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # --- Reset the button ---
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # --- Draw the button ---
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action



class Scoreboard():

    def __init__(self):
        self.score = 0

    # --- Function for drawing necessary text ---
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def pickupcoins(self, option):
        if option == 1:
            self.draw_text("score:", font2, WHITE, Width - 65, 5)
            if pygame.sprite.spritecollide(myplayer, coingroup, True):
                self.score += 1
            score = str(self.score)
            if self.score > 99:
                self.draw_text(score, font1, WHITE, Width - 85, 20)
            elif self.score > 9:
                self.draw_text(score, font1, WHITE, Width - 65, 20)
            else:
                self.draw_text(score, font1, WHITE, Width - 45, 20)
        else:
            self.draw_text("score:", font1, WHITE, 285, 90)
            score = str(self.score)
            self.draw_text(score, font3, WHITE, 435, 85)      

    def getscore(self):
        return self.score

    def checkplayercollision(self):
        if pygame.sprite.groupcollide(playergroup, barriergroup, False, True, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(playergroup, lasergroup, False, True, pygame.sprite.collide_rect):
            return True
    
    def checkcoincollision(self):
        if pygame.sprite.groupcollide(barriergroup, coingroup, False, True):
            coingroup.empty()

    def draw_high_score(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def checkscore(self, score, highscore):
        if int(score) > int(original_high_score):
            highscore = score
            with open('Project/highscore.txt', 'w') as file:
                file.write(str(highscore))

    def drawhighscoretxt(self, option):
        if option == 1:
            self.draw_text("highscore:", font2, WHITE, 0, 2)
        else:
            self.draw_text("highscore:", font1, WHITE, 240, 305)

    def checknewscore(self, score, option):
        if option == 1:
            if int(score) > int(original_high_score):
                self.draw_text("new highscore!", font3, WHITE, 180, 20)
        else:
            if int(score) > int(original_high_score):
                self.draw_text("new highscore!", font3, WHITE, 180, 350)

    def setscore(self, score):
        self.score = score



class player(pygame.sprite.Sprite):

    # --- Constructor Function ---
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # --- Create Player ---
      #  self.image = pygame.Surface((10, 20))
       # self.image.fill(WHITE)


        self.image1 = pygame.image.load("Project/Images/BarryRunning.png").convert_alpha()
        self.image = self.get_image(self.image1, 280, 288, 0)
        #self.animation_list = []
        #animation_count = 4
        #self.animation_cooldown = 300
        #self.frame = 0
        #for x in range(animation_count):
        #    self.animation_list.append(self.get_image(self.image1, 280, 288, x))
        #self.current_time = pygame.time.get_ticks()



        # --- Set Player Position ---
        self.rect = self.image.get_rect()
        self.rect.x = Width / 3
        self.rect.y = Height - 60 - 20

    # --- Functions ---

    def get_image(self, sheet, width, height, frame):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0,0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (50,50))
        image.set_colorkey(BLACK)
        return image
    
    #def draw(self):
        #if self.current_time % self.animation_cooldown == 0:
        #    self.frame += 1

       # self.image = self.animation_list[self.frame]

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

    def jump(self,vertSpeed):
        if self.rect.y > 0:
            self.rect.y += vertSpeed
        


class Fire(pygame.sprite.Sprite):

    def __init__(self, x, y):
            super().__init__()
            pygame.sprite.Sprite.__init__(self)
            image = pygame.image.load("Project/Images/Pixel Flame Spritesheet.png")
            self.image = pygame.transform.scale(image, (35, 35))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def fly(self, x, y):
            myfire = Fire(x, y)
            firegroup.add(myfire)



class Barrier(pygame.sprite.Sprite):
    # --- Constructor Function ---
    def __init__(self, width, height, posX, posY):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Project/Images/SpikyStick.png")
        self.image = pygame.transform.scale(img, (width, height))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()
        self.rect.x = posX
        self.rect.y = posY

    def spawn():
        if len(barriergroup) < 2:
            barrierx = random.randint(800,1700)
            nbarriers = random.randint(3,7)
            barriergap = random.randint(200,250)
            for i in range(1, nbarriers):
                barrierheight = random.randint(120,250)
                if i % 2 == 0:
                    newbarrier = Barrier(75, barrierheight, barrierx + (i * barriergap), -5)
                    barriergroup.add(newbarrier)
                else:
                    newbarrier = Barrier(75, barrierheight, barrierx + (i * barriergap), Height - 195 + (216 - barrierheight))
                    barriergroup.add(newbarrier)

    def update(self):
        self.rect.move_ip(COINSPEED * SPEEDMOD, 0)
        if self.rect.x < -75:
            self.kill()



class Laser(pygame.sprite.Sprite):
    def __init__(self, length, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.laserlength = length
        self.image = pygame.Surface((self.laserlength, 3))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spawn():
        if len(lasergroup) == 0:
            laserlength = random.randint(150, 450)
            laserx = random.randint(800, 1700)
            lasery = random.randint(30, Height - 30)
            newlaser = Laser(laserlength, laserx, lasery)
            lasergroup.add(newlaser)
            Warning.spawn(lasery)

    def update(self):
        self.rect.move_ip(COINSPEED * SPEEDMOD - 10, 0)
        if self.rect.x + self.laserlength < -50:
            self.kill()
    
    def gety(self):
        return self.rect.y



class Warning(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.img = font4.render("!", True, BLACK)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spawn(temp):
        Warning1 = Warning(1, temp - 11)
        warninggroup.add(Warning1)
        Warning2 = Warning(Width - 26, temp - 11)
        warninggroup.add(Warning2)

    def update(self):
        screen.blit(self.img, (self.rect.x + 8, self.rect.y + 1))
        if len(lasergroup) == 0:
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
game_paused = True
death = False
died = False
# -- Title of new window/screen --
pygame.display.set_caption("My Window")
# -- Exit game flag set to false --
done = False
# -- Manages how fast screen refreshes --
clock = pygame.time.Clock()

menu = Menu()

myplayer = player()

scoreboard = Scoreboard()

bg = Background()

startbutton = Button(53, 153, pygame.image.load('Project/Images/start_btn.png').convert_alpha())
endbutton = Button(456, 153, pygame.image.load('Project/Images/exit_btn.png').convert_alpha())

playergroup.add(myplayer)
allspritegroup.add(playergroup)
allspritegroup.add(barriergroup)
allspritegroup.add(coingroup)
allspritegroup.add(lasergroup)
allspritegroup.add(firegroup)

# -- Game Loop --
while not done:

    if death == True:
        menu.checkplay()
        scoreboard.draw_high_score(high_score, font3, WHITE, 485, 300)
        scoreboard.drawhighscoretxt(2)
        scoreboard.checknewscore(scoreboard.getscore(), 2)
        scoreboard.pickupcoins(2)

        if startbutton.draw() == True:
            scoreboard.setscore(0)
            scoreboard.pickupcoins(2)
            death = False
            barriergroup.empty()
            coingroup.empty()
            lasergroup.empty()
            warninggroup.empty()
            firegroup.empty()

        if endbutton.draw() == True:
            pygame.QUIT()

        allspritegroup.update
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True


    elif game_paused == True:

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
        Laser.spawn()

        # -- Fly --
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            myplayer.jump(JUMPSPEED)
            Fire.fly(0,myplayer.get_x(),myplayer.get_y() + 50)
        else:
            firegroup.empty()

        if len(firegroup) > 1:
            firegroup.empty()

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
        lasergroup.draw(screen)
        warninggroup.draw(screen)
        firegroup.draw(screen)

        allspritegroup.update()
        coingroup.update()
        barriergroup.update()
        lasergroup.update()
        warninggroup.update()
        firegroup.update()

        scoreboard.pickupcoins(1)
        scoreboard.checkcoincollision()
        scoreboard.drawhighscoretxt(1)
        scoreboard.checknewscore(scoreboard.getscore(), 1)

        if scoreboard.checkplayercollision() == True:
            death = True


        scoreboard.draw_high_score(high_score, font1, WHITE, 45, 20)
        scoreboard.checkscore(scoreboard.getscore(), high_score)
        
        if int(scoreboard.getscore()) > int(high_score):
            high_score = scoreboard.getscore()
            high_score = str(high_score)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

# End While - End of game loop
pygame.quit()