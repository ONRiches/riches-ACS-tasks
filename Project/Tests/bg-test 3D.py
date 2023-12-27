import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

Width = 800
Height = 432

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Endless Scroll 3D")

scroll = 0

class Background():

    def __init__(self):
        self.ground_image = pygame.image.load("Project/Images/ground.png").convert()
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
            print(self.ground_height)



bg = Background()
run = True
while run:

    clock.tick(FPS)

    bg.draw_bg()
    bg.draw_ground()

    scroll += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit