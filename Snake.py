import pygame
import random

#north: 1; south: 2; west: 3; east: 4;

class player():
    player_x = 400
    player_y = 300
    player_x_dir = 20
    player_y_dir = 0
    player_mask = pygame.mask.Mask((20, 20), True)

pygame.init()

game_on = True
font = pygame.font.Font(pygame.font.get_default_font(), 25)
screen = pygame.display.set_mode((800, 600))
game_on = True
snack_exist = False
score = 0

food_x = 0
food_y = 0
food_mask = pygame.mask.Mask((20, 20), True)

clock = pygame.time.Clock()

snake_list = []
snake_length = 1
snake_direction = 4

def offset():
    return int(player.player_x - food_x), int(player.player_y - food_y)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (255, 0, 0), [x[0], x[1], 20, 20], 5)

def collision(snake_list):
    if player.player_x - 20 < 0 or player.player_x + 21 > 800 or player.player_y + 21 > 600 or player.player_y - 20 < 0:
        return True

    return False

def controls_west_east():
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        player.player_x_dir = 20
        player.player_y_dir = 0
        snake_direction = 4
    elif pygame.key.get_pressed()[pygame.K_LEFT] == True:
        player.player_x_dir = -20
        player.player_y_dir = 0
        snake_direction = 3

def controls_north_south():
    if pygame.key.get_pressed()[pygame.K_UP] == True and snake_direction != 2:
        player.player_x_dir = 0
        player.player_y_dir = -20
        snake_direction = 1
    elif pygame.key.get_pressed()[pygame.K_DOWN] == True and snake_direction != 1:
        player.player_x_dir = 0
        player.player_y_dir = 20
        snake_direction = 2

while game_on:
    screen.fill((0,0,0))

    text = font.render("Score: " + str(score), True, (255, 255, 255))

    screen.blit(text, [0, 0])

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    pygame.display.set_caption('Snake')    

    player.player_x += player.player_x_dir
    player.player_y += player.player_y_dir

    snake_head = []
    snake_head.append(player.player_x)
    snake_head.append(player.player_y)
    snake_list.append(snake_head)
    
    if len(snake_list) > snake_length:
        del snake_list[0]
    
    for x in snake_list[:-1]:
        if x == snake_head:
            player.player_x_dir = 0
            player.player_y_dir = 0

    draw_snake(snake_list)
    

    while snack_exist == False:
        # Make it so that it works with body
        food_x = round(random.randrange(0, 800 - 20) / 20.0) * 20.0
        food_y = round(random.randrange(0, 600 - 20) / 20.0) * 20.0
        snack_exist = True

    pygame.draw.rect(screen, (255,0,0), (food_x, food_y, 20, 20), 5)
    
    if snake_direction == 1:
        controls_west_east()
    elif snake_direction == 2:
        controls_west_east()
    elif snake_direction == 3:
        controls_north_south()
    elif snake_direction == 4:
        controls_north_south()
        
    if collision(snake_list):
        player.player_x_dir = 0
        player.player_y_dir = 0

    if player.player_mask.overlap(food_mask, offset()):
        score += 1
        snake_length += 1
        snack_exist = False

    pygame.display.update()

    clock.tick(15)

        









