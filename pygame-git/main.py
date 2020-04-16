#import pygame

import pygame
# initialization
pygame.init()

# infinite loop


# Screen for game
screen = pygame.display.set_mode((800, 600))
#title and icon

pygame.display.set_caption("Star War")
icon = pygame.image.load(r"D:\Python\pygame\pygame-git\villain (1).png")
pygame.display.set_icon(icon)
player_image_path = r"D:\Python\pygame\pygame-git\space-invaders.png"
player_image = pygame.image.load(player_image_path)
player_x = 350
player_y = 500
player_x_change = 0
enemy_image_path = r"D:\Python\pygame\pygame-git\cartoon.png"
enemy_image = pygame.image.load(enemy_image_path)
enemy_x = 350
enemy_y = 50


def player(x, y):
    screen.blit(player_image, (x, y))


def enemy(x, y):
    screen.blit(enemy_image, (x, y))


# game loop
value = True
while value:
    screen.fill((255, 223, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            value = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            elif event.key == pygame.K_RIGHT:
                player_x_change = +0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            print("key is release")

    player_x += player_x_change
    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()
