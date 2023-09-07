import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

Width = 768
Height = 432

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Endless Scroll")

bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"Project/plx-{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

ground = pygame.image.load("Project/ground.png").convert()
ground_width = ground.get_width()
ground_height = ground.get_height()

scroll = 0
gtiles = math.ceil(Width / ground_width) + 1

run = True
while run:

    print(ground_width)

    clock.tick(FPS)

    for i in range(0, gtiles):
       screen.blit(ground, (i * ground_width + scroll, Height - ground_height))

    scroll -= 5

    if abs(scroll) > ground_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit