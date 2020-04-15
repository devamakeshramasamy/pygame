#import pygame

import pygame
# initialization
pygame.init()

# infinite loop


# Screen for game
screen = pygame.display.set_mode((800, 500))
#title and icon

pygame.display.set_caption("Star War")
icon = pygame.image.load(r"D:\Python\pygame\pygame-git\villain (1).png")
pygame.display.set_icon(icon)
player_image_path = r"D:\Python\pygame\pygame-git\space-invaders.png"
player_image = pygame.image.load(player_image_path)
player_x = 350
player_y = 400


def player():
    screen.blit(player_image, (player_x, player_y))


# game loop
value = True
while value:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            value = False
    screen.fill((255, 223, 0))
    player()
    pygame.display.update()
