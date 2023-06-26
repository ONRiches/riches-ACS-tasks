import pygame
import winsound
# -- Global Constants
ball_width = 20
x_val = 320
y_val = 240
x_padd = 0
y_padd = 20
padd_length = 15
padd_width = 60
xspeed = 1
yspeed = 1
score = 0

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Pong")
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
 # -- User input and controls
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    #End If
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   done = True
 #End If
 if event.type == pygame.KEYDOWN:
  if event.key == pygame.K_UP:
    if y_padd > 0:
      # - write logic that happens on key press here
      y_padd = y_padd - 7
  elif event.key == pygame.K_DOWN:
    if y_padd < 420:
      y_padd = y_padd + 7
    #End If
  #End If

 #Next event

 # -- Game logic goes after this comment

 x_val = x_val + xspeed
 y_val = y_val + yspeed

 bottom_left_x = x_val
 bottom_left_y = y_val + ball_width
 bottom_right_x = x_val + ball_width
 bottom_right_y = y_val + ball_width
 top_right_x = x_val + ball_width
 top_right_y = y_val

 if bottom_left_y >= 480:
  yspeed = yspeed * -1
  winsound.Beep(700,40)
 #End if
 
 if bottom_right_x >= 640:
  xspeed = xspeed * -1
  winsound.Beep(700,40)
 #End if

 if top_right_x < -4:
  winsound.Beep(500,500)
  winsound.Beep(200,1000)
  x_val = 320
  y_val = 240
  xspeed = 1
  yspeed = 1
  score = 0
 #End if

 if y_val <= 0:
  yspeed = yspeed * -1
  winsound.Beep(700,40)
 #End if

 if (y_val >= y_padd):
  if (y_val <= y_padd + 60):
    if x_val <= x_padd + 15:
      xspeed = xspeed * - 1
      xspeed = xspeed + 0.5

      if(yspeed > 0):
        yspeed = yspeed + 0.5
      else:
        yspeed = yspeed - 0.5
      #End if

      score = score + 1
      
      winsound.Beep(1200,40)
    #End if
  #End if

 elif (bottom_left_y >= y_padd):
  if (bottom_left_y <= y_padd + 60):
    if x_val <= x_padd + 15:
      xspeed = xspeed * - 1
      xspeed = xspeed + 1

      if(yspeed > 0):
        yspeed = yspeed + 1
      else:
        yspeed = yspeed - 1
      #End if
      
      score = score + 1

      winsound.Beep(1200,40)
    #End if
  #End if
 #End if

 # -- Screen background is BLACK
 screen.fill (BLACK)
 # -- Draw here
 
 pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))

 pygame.draw.rect(screen, WHITE, (x_padd,y_padd,padd_length,padd_width))

 score1 = font.render("Score: " + str(score), True, (255, 255, 255))
 screen.blit(score1, (500, 10))

 #Next event 

 # -- flip display to reveal new position of objects
 pygame.display.flip()
 # - The clock ticks over
 clock.tick(60)
#End While - End of game loop
pygame.quit()