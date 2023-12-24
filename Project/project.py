from typing import Any
import pygame
import random
import os
vec = pygame.math.Vector2
pygame.font.init()
pygame.display.init()

# -- Global Constants --

GRAVITY = 5
JUMPSPEED = -10

# --- Speed Modifiers ---

BGSPEED = 1
FGSPEED = 2.5
COINSPEED = -5.5
SPEEDMOD = 1
scroll = 0

# --- Screen Dimensions ---

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

# Set a new highscore variable that can be changed whilst keeping the original score
original_high_score = high_score

# --- Sprite Groups ---

allspritegroup = pygame.sprite.Group()
lasergroup = pygame.sprite.Group()
barriergroup = pygame.sprite.Group()
coingroup = pygame.sprite.Group()
warninggroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()
firegroup = pygame.sprite.Group()

# --- Colours ---

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (225, 0, 0)

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
    


class Menu():

    # --- Constructor ---
    def __init__(self):

        # Set an arbitrary value so that functions can be used
        count = 1
    
    # --- Functions ---

    # --- Pause function ---
    def openmenu(self):

        # Check if ESC pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    # Test data
                    print("Pause")

                # End if
            # End if
        # Next

    # --- Cover the background if dead ---
    def deathscreen(self):

        screen.fill(BLACK)

    # --- Quit from death screen ---
    def checkplay(self):

        # Cover over the game with a black screen
        self.deathscreen()

        # Check if ESC pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    # Shut the game window if true
                    pygame.QUIT()

                # End if
            # End if
        # Next

    # --- Start function ---
    def start(self):

        # Create a player
        myplayer = Player()

        # Add player to sprite groups
        playergroup.add(myplayer)
        allspritegroup.add(playergroup)
        


class Button():

    # --- Constructor ---
    def __init__(self, x, y, image):

        # Assign inputs to values
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # --- Functions ---

    # --- Draw the buttons for menus and check if pressed ---
    def draw(self):

        # Value used to return if a button has been pressed
        action = False

        # Get the mouse position
        pos = pygame.mouse.get_pos()

        # Check if mouse is over button
        if self.rect.collidepoint(pos):
            # Check if button pressed
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                # self.clicked is used to make button only be able to be pressed once at a time
                self.clicked = True
                action = True

            # End if
        # End if

        # Reset the button so it can be clicked again
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # End if

        # Draw the button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # Return if the button has been pressed
        return action



class Scoreboard():

    # --- Constructor ---
    def __init__(self):

        self.score = 0

    # --- Functions ---

    # --- Function for drawing necessary text ---
    def draw_text(self, text, font, text_col, x, y):

        # Create a drawable image
        img = font.render(text, True, text_col)

        # Draw the image
        screen.blit(img, (x, y))

    # --- Check if the player collects coins ---
    def pickupcoins(self, option):

        # Select one of two options for drawing the score
        if option == 1:

            # --- Option for during normal game running ---

            # Draw the text before the number
            self.draw_text("score:", font2, WHITE, Width - 65, 5)

            # Check if the player collides with any coins, then delete any collided with coins
            if pygame.sprite.spritecollide(myplayer, coingroup, True, pygame.sprite.collide_mask):

                # Add 1 to the score if coin is collided with
                self.score += 1

            # End if

            # Convert the score to a string so that it can be drawn on the screen
            score = str(self.score)

            # Draw the score in the top right of the screen
            # Depending on the length of the score, move the scoreboard left so that it all fits on the screen
            if self.score > 99:
                self.draw_text(score, font1, WHITE, Width - 85, 20)
            elif self.score > 9:
                self.draw_text(score, font1, WHITE, Width - 65, 20)
            else:
                self.draw_text(score, font1, WHITE, Width - 45, 20)
            # End if

        else:

            # --- Option for drawing the score on the death screen ---

            # Draw the text in the top-middle of the screen
            self.draw_text("score:", font1, WHITE, 285, 90)
            score = str(self.score)
            self.draw_text(score, font3, WHITE, 435, 85)  

        # End if    

    # --- Score Getter ---
    def getscore(self):

        return self.score

    # --- Check if the player collides with a barrier or laser and delete player if true ---
    def checkplayercollision(self):
        if pygame.sprite.groupcollide(playergroup, barriergroup, False, True, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(playergroup, lasergroup, False, True, pygame.sprite.collide_mask):
            return True
        # End if
    
    # --- Check if the player collides with a coin and delete coins if true ---
    def checkcoincollision(self):
        if pygame.sprite.groupcollide(barriergroup, coingroup, False, True, pygame.sprite.collide_mask):

            # Reset the coin group
            coingroup.empty()
        
        # End if

    # --- Draw the highscore text ---
    def draw_high_score(self, text, font, text_col, x, y):

        # Create a drawable image
        img = font.render(text, True, text_col)

        # Draw the image
        screen.blit(img, (x, y))

    # --- Update the highscore file ---
    def checkscore(self, score, highscore):

        # Check if the current score is higher than the highscore
        if int(score) > int(original_high_score):

            # If true, update the temp highscore variable
            highscore = score

            # Update the external highscore file
            with open('Project/highscore.txt', 'w') as file:
                file.write(str(highscore))

        # End if

    # --- Draw the highscore ---
    def drawhighscoretxt(self, option):

        # Set up two options for drawing the highscore; in normal game running or deathscreen
        if option == 1:

            # Draw the highscore in the top left
            self.draw_text("highscore:", font2, WHITE, 0, 2)

        else:

            # Draw the highscore in the bottom-middle of the screen
            self.draw_text("highscore:", font1, WHITE, 240, 305)

        # End if

    # --- Disply text telling the player a new highscore has been achieve ---
    def checknewscore(self, score, option):
        
        # Allow two options for regular playing and the deathscreen
        if option == 1:

            # If the score is higher than the highscore, display "NEW HIGHSCORE!" at the top-middle of the screen (regular running)
            if int(score) > int(original_high_score):
                self.draw_text("new highscore!", font3, WHITE, 180, 20)

        else:

            # If the score is higher than the highscore, displayer "NEWHIGHSCORE!" at the bottom middle of the screen (deathscreen)
            if int(score) > int(original_high_score):
                self.draw_text("new highscore!", font3, WHITE, 180, 350)

        # End if

    # --- Score setter ---
    def setscore(self, score):
        self.score = score



class Player(pygame.sprite.Sprite):

    # --- Constructor Function ---
    def __init__(self):

        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Load the spritesheet used on the player sprite
        self.image1 = pygame.image.load("Project/Images/BarryRunning.png").convert_alpha()
        
        # Get the correct frame from the spritesheet
        self.image = self.get_image(self.image1, 280, 288, 0)

        # Create a mask for better collisions
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

        # Set Player Position
        self.rect = self.image.get_rect()
        self.rect.x = Width / 3
        self.rect.y = Height - 60 - 20

    # --- Functions ---

    # --- Function to take a chosen frame from the spritesheet ---
    def get_image(self, sheet, width, height, frame):

        # Load the sprite sheet
        image = pygame.Surface((width, height)).convert_alpha()

        # Blit the correct frame
        image.blit(sheet, (0,0), (frame * width, 0, width, height))

        # Scale the image
        image = pygame.transform.scale(image, (50,50))

        # Set background to black
        image.set_colorkey(BLACK)
        return image

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
        


class Fire(pygame.sprite.Sprite):

    # --- Constructor Function ---
    def __init__(self, x, y):
            
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Load the flame image
        image = pygame.image.load("Project/Images/Pixel Flame Spritesheet.png")

        # Scale the flame up
        self.image = pygame.transform.scale(image, (35, 35))

        # Positon
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # --- Spawn the flame underneath the player when flying ---
    def fly(self, x, y):
        
        # Instantiate a Fire object
        myfire = Fire(x, y)

        # Add new object to sprite group
        firegroup.add(myfire)



class Barrier(pygame.sprite.Sprite):

    # --- Constructor Function ---
    def __init__(self, width, height, posX, posY):

        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Load the image for the barrier
        img = pygame.image.load("Project/Images/SpikyStick.png")

        # Scale the image
        self.image = pygame.transform.scale(img, (width, height))

        # Create a mask for better collisions
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()
        
        # Postiion
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    # --- Functions ---

    # --- Spawn the barriers ---
    def spawn():

        # If the number of barriers currently spawn is less than 2, spawn more
        if len(barriergroup) < 2:

            # Random number generated to decide how far away the barriers spawn from the player
            barrierx = random.randint(800,1700)

            # Random number generated to decide how many barriers to be spawned in cluster
            nbarriers = random.randint(3,7)

            # Random number generated to decide how far each barrier is away from one another in a cluster
            barriergap = random.randint(200,250)

            # Loop to spawn the number of needed barriers
            for i in range(1, nbarriers):

                # Random number generated to decide the height of each barrier
                barrierheight = random.randint(120,250)

                # Odd numbered barriers spawn on the floor, even numbered barriers spawn on the ceiling
                if i % 2 == 0:

                    # Instantiate new barrier
                    newbarrier = Barrier(75, barrierheight, barrierx + (i * barriergap), -5)

                    # Add to sprite group
                    barriergroup.add(newbarrier)

                else:

                    # Instantiate new barrier
                    newbarrier = Barrier(75, barrierheight, barrierx + (i * barriergap), Height - 195 + (216 - barrierheight))

                    # Add to sprite group
                    barriergroup.add(newbarrier)

                # End if
            # Next
        # End if

    # --- Update ---
    def update(self):

        # Move barriers left towards the player and increase the speed in accordance to the speed mod
        self.rect.move_ip(COINSPEED * SPEEDMOD, 0)

        # Once the barriers are off the screen, kill them so new ones can be spawned
        if self.rect.x < -75:
            self.kill()
        # End if



class Laser(pygame.sprite.Sprite):#

    # --- Constructor ---
    def __init__(self, length, x, y):

        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Set the length of the line
        self.laserlength = length

        # Create the laser
        self.image = pygame.Surface((self.laserlength, 3))
        self.image.fill(RED)

        # Set the position of the laser
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # --- Functions ---

    # --- Spawn ---
    def spawn():

        # If there are currently no lasers, spawn a new one
        if len(lasergroup) == 0:

            # Set a random length
            laserlength = random.randint(150, 450)

            # Set a random distance from the player
            laserx = random.randint(800, 1700)

            # Set a random height
            lasery = random.randint(30, Height - 30)

            # Instantiate new laser
            newlaser = Laser(laserlength, laserx, lasery)

            # Add new object to the sprite group
            lasergroup.add(newlaser)

            # Spawn the warnings relating to the laser
            Warning.spawn(lasery)

        # End if

    # --- Update ---
    def update(self):

        # Move the laser left towards the player faster than other objects
        self.rect.move_ip(COINSPEED * SPEEDMOD - 10, 0)

        # Once the laser goes off the screen, kill it so another can be spawned
        if self.rect.x + self.laserlength < -50:
            self.kill()
        # End if
    
    # --- y value getter ---
    def gety(self):
        return self.rect.y



class Warning(pygame.sprite.Sprite):

    # --- Constructor ---
    def __init__(self, x, y):

        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Draw the warning symbol on a red square
        self.img = font4.render("!", True, BLACK)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)

        # Get the position of the warning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # --- Functions ---

    # --- Spawn wanrings ---
    def spawn(temp):

        # Instantiate objects at the same height as lasers
        Warning1 = Warning(1, temp - 11)
        Warning2 = Warning(Width - 26, temp - 11)

        # Add the new objects to sprite group
        warninggroup.add(Warning1)
        warninggroup.add(Warning2)

    # --- Update ---
    def update(self):

        screen.blit(self.img, (self.rect.x + 8, self.rect.y + 1))

        # Once the relevant laser is killed, kill the warnings so new ones can be spawned
        if len(lasergroup) == 0:
            self.kill()
    


class Coins(pygame.sprite.Sprite):

    # --- Constructor ---
    def __init__(self, x, y):

        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        # Load the image for the coin sprite
        img = pygame.image.load("Project/Images/coin.png")

        # Scale the image down
        self.image = pygame.transform.scale(img, (15,15))

        # Get the position of the centre of the sprite
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.rect.x = x
        self.rect.y = y

    # --- Functions ---

    # --- Spawn coin clusters ---
    def spawn():

        # Spawn new coins if there are currently none
        if len(coingroup) == 0:

            # Random x coordinate for the first coin in the cluster
            coinx = random.randint(1000, 2500)

            # Random y coorindate for the first coin in the cluster
            coiny = random.randint(40, Height - 100)

            # Random number of coins in the top row of the cluster
            coing = random.randint(5, 17)

            # Spawn the top row of the cluster
            for i in range(0, coing):

                # Instantiate new coins, with each 20 pixels from each other
                newcoin = Coins(coinx + i * 20, coiny)

                # Add each new object to the sprite group
                coingroup.add(newcoin)

            # Next i

            # Spawn the bottom row of the cluster 20 pixel below the top row
            for j in range(0, 25 - coing):

                # Instantiate new coins, with each 20 pixels from each other
                newcoin = Coins(coinx + (j * 20) - 60, coiny + 20)

                # Add each new object to the sprite group
                coingroup.add(newcoin)

            # Next i
        # End if

    # --- Move coins to the left ---
    def movecoins(self):
        self.rect.x -= 1

    # --- Update ---
    def update(self):

        # Move coins to the left
        self.rect.move_ip(COINSPEED * SPEEDMOD, 0)

        # Kill coins once off the screen so that more can be spawned
        if self.rect.x < -50:
            self.kill()
        # End if



# --- Initialise Pygame ---

pygame.init()

# --- Blank Screen ---

size = (Width, Height)
screen = pygame.display.set_mode(size)

# --- Game State Variables ---

game_paused = True
death = False
died = False

# --- Title of new window/screen ---

pygame.display.set_caption("My Window")

# --- Exit game flag set to false ---

done = False

# --- Manage how fast screen refreshes ---

clock = pygame.time.Clock()

# --- Instantiation of necessary classes

menu = Menu()

myplayer = Player()

scoreboard = Scoreboard()

bg = Background()

# --- Draw the buttons for menus ---

startbutton = Button(53, 153, pygame.image.load('Project/Images/start_btn.png').convert_alpha())
endbutton = Button(456, 153, pygame.image.load('Project/Images/exit_btn.png').convert_alpha())

# --- Add the new objects to sprite groups ---

playergroup.add(myplayer)

# --- Add all the sprite groups to one common group ---

allspritegroup.add(playergroup)
allspritegroup.add(barriergroup)
allspritegroup.add(coingroup)
allspritegroup.add(lasergroup)
allspritegroup.add(firegroup)

# --- Game Loop ---

while not done:

    # --- Game States ---

    # --- Death State ---
    # If dead, then display the death screen
    if death == True:

        # Draw the deathscreen - buttons, scores, check for new highscore etc.
        menu.checkplay()
        scoreboard.draw_high_score(high_score, font3, WHITE, 485, 300)
        scoreboard.drawhighscoretxt(2)
        scoreboard.checknewscore(scoreboard.getscore(), 2)
        scoreboard.pickupcoins(2)

        # If the start button is pressed then reset the game
        if startbutton.draw() == True:

            # Set the score to 0
            scoreboard.setscore(0)

            # Reset variables
            scoreboard.pickupcoins(2)
            death = False

            # Kill all of the objects
            barriergroup.empty()
            coingroup.empty()
            lasergroup.empty()
            warninggroup.empty()
            firegroup.empty()

        # End if

        # If the quit button is pressed then close the game
        if endbutton.draw() == True:
            pygame.QUIT()
        # End if

        allspritegroup.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
            # End if
        # Next

    # --- Paused State ---
    # If the game is paused then draw the buttons and stop moving objects
    elif game_paused == True:

        # If start button is pressed then resume the game
        if startbutton.draw() == True:
            game_paused = False
        # End if
        
        # If the quit button is pressed then exit the game
        if endbutton.draw() == True:
            pygame.quit()
        # End if

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
            
            # If ESC key is pressed then resume the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = False
                # End if
            # End if
        # Next

    # --- Normal State ---       
    else:

        # Set the game speed
        clock.tick(FPS)

        # Draw the background
        bg.draw_bg()

        # Draw the ground
        bg.draw_ground()

        # Set the necessary speeds of background and objects
        scroll += 2
        SPEEDMOD = SPEEDMOD * scoreboard.score / 200 + 1

        # Spawn obstacles and coins
        Coins.spawn()
        Barrier.spawn()
        Laser.spawn()

        # If the up key is pressed then fly
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            myplayer.fly(JUMPSPEED)
            
            # If the player is flying, instantiate a fire object underneath the jetpack
            Fire.fly(0,myplayer.get_x(),myplayer.get_y() + 50)
        # End if

        else:

            # If the player is not flying, delete any flames
            firegroup.empty()
        
        # End if

        # Allow there to be only one flame at once
        if len(firegroup) > 1:
            firegroup.empty()
        # End if

        # Prevent player from falling through the floor
        if myplayer.rect.y <= Height - 62 - 20:
            myplayer.rect.y = myplayer.rect.y + GRAVITY
        # End if

        # User input and controls
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
            # End if
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Pause")
                    game_paused = True
            # End If

        # Next

        # --- Deal with objects ---

        # Draw the objects on the screen
        playergroup.draw(screen)
        coingroup.draw(screen)
        barriergroup.draw(screen)
        lasergroup.draw(screen)
        warninggroup.draw(screen)
        firegroup.draw(screen)

        # Update all the objects
        allspritegroup.update()
        coingroup.update()
        barriergroup.update()
        lasergroup.update()
        warninggroup.update()
        firegroup.update()

        # Check for changes to score, collisions with coins or objects etc.
        scoreboard.pickupcoins(1)
        scoreboard.checkcoincollision()
        scoreboard.drawhighscoretxt(1)
        scoreboard.checknewscore(scoreboard.getscore(), 1)

        # If the player hits a laser or a barrier then change to the death game state
        if scoreboard.checkplayercollision() == True:
            death = True
        # End if

        # Draw the score and highscore
        scoreboard.draw_high_score(high_score, font1, WHITE, 45, 20)
        scoreboard.checkscore(scoreboard.getscore(), high_score)
        
        # Update the highscore if higher than the score
        if int(scoreboard.getscore()) > int(high_score):
            high_score = scoreboard.getscore()
            high_score = str(high_score)
        # End if

    # End if

    # Flip display to reveal new position of objects
    pygame.display.flip()

# End While - End of game loop
pygame.quit()