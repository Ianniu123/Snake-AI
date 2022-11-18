import pygame
import random

class player():
    player_x = 400
    player_y = 300
    player_x_dir = 20
    player_y_dir = 0
    player_mask = pygame.mask.Mask((20, 20), True)

game_on = True

screen = pygame.display.set_mode((800, 600))
game_on = True
snack_exist = False

score = 0

food_x = 0
food_y = 0
food_mask = pygame.mask.Mask((20, 20), True)

clock = pygame.time.Clock()

def offset():
    return int(player.player_x - food_x), int(player.player_y - food_y)

def collision():
    if player.player_x - 20 < 0 or player.player_x + 21 > 800 or player.player_y + 21 > 600 or player.player_y - 20 < 0:
        return True

    return False

while game_on:
    screen.fill((0,0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    pygame.display.set_caption('Snake')    

    player.player_x += player.player_x_dir
    player.player_y += player.player_y_dir

    pygame.draw.rect(screen, (255,0,0), (player.player_x, player.player_y, 20, 20), 5)

    while snack_exist == False:
        food_x = random.randint(0, 800)
        food_y = random.randint(0, 600)
        if (food_x <= player.player_x - 20 or food_x >= player.player_x + 20) and (food_y <= player.player_y - 20 or food_y >= player.player_y + 20) and food_x % 20 == 0 and food_y % 20 == 0:
            snack_exist = True
            break

    pygame.draw.rect(screen, (255,0,0), (food_x, food_y, 20, 20), 5)

    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        player.player_x_dir = 20
        player.player_y_dir = 0
    elif pygame.key.get_pressed()[pygame.K_LEFT] == True:
        player.player_x_dir = -20
        player.player_y_dir = 0
    elif pygame.key.get_pressed()[pygame.K_UP] == True:
        player.player_x_dir = 0
        player.player_y_dir = -20
    elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
        player.player_x_dir = 0
        player.player_y_dir = 20
        
    if collision():
        player.player_x_dir = 0
        player.player_y_dir = 0

    if player.player_mask.overlap(food_mask, offset()):
        score += 1
        snack_exist = False


    pygame.display.update()

    clock.tick(10)

        









