import pygame
import random
import math

# Global Constants

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# Initialise PyGame
pygame.init()

# Font***

font = pygame.font.Font('freesansbold.ttf', 28)

# Blank Screen
size = (1000,800)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("Space Bar to Shoot")



# Define the class Player which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for Player
    def __init__(self, color, width, height, score):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.score = 20
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 700
        # Set speed of the sprite
        self.speed = 0
    # Returns player x 
    def get_x(self):
        return self.rect.x
    # Class update function - runs for each pass through the game loop
    def update(self):
        print("")
    # Score functions
    def hitTarget(self):
        self.score = self.score + 1
    def missTarget(self):
        self.score = self.score - 1
        

# Define the class Invader which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for Invader
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1000)
        self.rect.y = random.randrange(-150,50)
    def update(self):
        self.rect.y = self.rect.y + 2
        # Respawn code
        if self.rect.y > 800:
            self.rect.y = -5
            self.rect.x = random.randrange(0,995)
            player.missTarget()

# Define the class Bullet which is a sprite like Invader, but spawned in differently
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
        self.rect.x = player.get_x() + 10
        self.rect.y = 700
    def update(self):
        # Move bullet up 
        self.rect.y = self.rect.y - 4
        if pygame.sprite.groupcollide(bullet_list, Invader_group, True, True, collided = None):
            player.hitTarget()
            print("******")
        

# Exit game flag set to false
done = False

# Create a list of the Invader blocks
Invader_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
# Create a list of all bullets
bullet_list = pygame.sprite.Group()


# Create the Invaders
number_of_enemies = 30
for x in range(number_of_enemies):
    my_Invader = Invader(WHITE, 25, 5)
    Invader_group.add(my_Invader)
    all_sprites_group.add(my_Invader)
    
# Create the Player
player = Player(YELLOW, 25, 25, 20)
all_sprites_group.add(player)

# Procedure to fire bullet
def fire():
    print("shot")
    mybullet = Bullet(RED, 5, 12)
    all_sprites_group.add(mybullet)
    bullet_list.add(mybullet)
    # bullet_count = bullet_count - 1
    
# Manages how fast screen refreshes
clock = pygame.time.Clock()


### Game Loop


while not done:
    # User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # p1PadY = p1PadY - 20
                print("left")
            elif event.key == pygame.K_RIGHT:
                # p1PadY = p1PadY + 20
                print("right")
            elif event.key == pygame.K_SPACE:
                # p1PadY = p1PadY + 20
                print("up")
                fire()
    # Code that somehow makes moving smooth
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.rect.x < 0:
            player.rect.x = 0
        else:
            player.rect.x = player.rect.x - 15
    if keys[pygame.K_RIGHT]:
        if player.rect.x >= 1000 - 25:
            player.rect.x = 1000 - 25
        else:
            player.rect.x = player.rect.x + 15

    # Game logic goes after this comment
    
    all_sprites_group.update()

    
    # Screen background is BLACK
    screen.fill(BLACK)
    
    # Draw here
    
    all_sprites_group.draw(screen)
    # pygame.draw.rect(screen, BLUE, (220,165,200,150))
    # pygame.draw.circle(screen, YELLOW, (40,100),40,0)
    
    # Score
    
    score1 = font.render("Score : " + str(player.score), True, (255, 255, 255))
    screen.blit(score1, (100, 50))
    
    msg1 = font.render("Press space to fire, arrow keys to move", True, (255, 255, 0))
    screen.blit(msg1, (100, 120))
    
    msg2 = font.render("When you hit a target, score += 1", True, (255, 0, 0))
    screen.blit(msg2, (100, 170))
    
    msg3 = font.render("When you miss a target, score -= 1", True, (255, 0, 0))
    screen.blit(msg3, (100, 220))
    
    # Flip display to reveal new position of objects
    pygame.display.flip()
    
    # The clock ticks over
    clock.tick(60)
    
    # End While End of game loop
pygame.quit()