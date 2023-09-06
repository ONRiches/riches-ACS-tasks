import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

Width = 1500
Height = 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Endless Scroll")

bg1 = pygame.image.load("Project/TreesBG.jpg").convert()
bg = pygame.transform.scale(bg1, (Width, Height))
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(Width / bg_width) + 1

run = True
while run:

    clock.tick(FPS)

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit