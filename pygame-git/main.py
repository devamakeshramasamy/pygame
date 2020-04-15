#import pygame

import pygame
# initialization
pygame.init()

# infinite loop


# Screen for game
screen = pygame.display.set_mode((800, 500))
#title and icon

pygame.display.set_caption("Coronavirus")
icon = pygame.image.load("D:\Python\pygame\icom.png")
pygame.display.set_icon(icon)

# game loop
value = True
while value:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            value = False
    screen.fill((255, 223, 0))
    pygame.display.update()
