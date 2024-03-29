import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

Width = 800
Height = 432

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Endless Scroll")

bg1 = pygame.image.load("Project/Images/plx-1.png").convert_alpha()
bg1_width = bg1.get_width()

bg2 = pygame.image.load("Project/Images/plx-2.png").convert_alpha()
bg2_width = bg2.get_width()

bg3 = pygame.image.load("Project/Images/plx-3.png").convert_alpha()
bg3_width = bg3.get_width()

bg4 = pygame.image.load("Project/Images/plx-4.png").convert_alpha()
bg4_width = bg4.get_width()

bg5 = pygame.image.load("Project/Images/plx-5.png").convert_alpha()
bg5_width = bg5.get_width()


scroll = 0
tiles1 = math.ceil(Width / bg2_width) + 1
tiles2 = math.ceil(Width / bg2_width) + 1
tiles3 = math.ceil(Width / bg3_width) + 1
tiles4 = math.ceil(Width / bg4_width) + 1
tiles5 = math.ceil(Width / bg5_width) + 1

run = True
while run:

    clock.tick(FPS)

    for i in range(0, tiles1):
       screen.blit(bg1, (i * bg1_width + scroll, 0))

    for i in range(0, tiles2):
       screen.blit(bg2, (i * bg2_width + scroll + 0.1, 0))
       
    for i in range(0, tiles3):
       screen.blit(bg3, (i * bg3_width + scroll + 0.2, 0))
       
    for i in range(0, tiles4):
       screen.blit(bg4, (i * bg4_width + scroll + 0.3, 0))

    for i in range(0, tiles5):
       screen.blit(bg5, (i * bg5_width + scroll + 0.4, 0))

    scroll -= 5

    if abs(scroll) > bg1_width:
        scroll = 0

    if abs(scroll) > bg2_width:
        scroll = 0

    if abs(scroll) > bg3_width:
        scroll = 0

    if abs(scroll) > bg4_width:
        scroll = 0

    if abs(scroll) > bg5_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit