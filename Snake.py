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
title = pygame.font.Font(pygame.font.get_default_font(), 40)
screen = pygame.display.set_mode((800, 600))
score = 0

food_x = 0
food_y = 0
food_mask = pygame.mask.Mask((20, 20), True)
food_exist = False

clock = pygame.time.Clock()

snake_list = []
snake_length = 4
snake_direction = 4

width = screen.get_width()
height = screen.get_height()

title_1 = title.render('Snake' , True , (255,255,255)) 

text_1 = font.render('Start game' , True , (255,255,255)) 
pygame.draw.rect(screen, (255,255,255), (width/2 - 65, height/2 - 45, 150, 40), 1)

text_2 = font.render('Rules' , True , (255,255,255)) 
pygame.draw.rect(screen, (255,255,255), (width/2 - 65, height/2 + 20, 150, 40), 1)

text_3 = font.render('Quit' , True , (255,255,255)) 
pygame.draw.rect(screen, (255,255,255), (width/2 - 65, height/2 + 85, 150, 40), 1)


def offset():
    return int(player.player_x - food_x), int(player.player_y - food_y)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (255, 0, 0), [x[0], x[1], 20, 20], 5)

def collision(snake_list, snake_head):
    if player.player_x < 0 or player.player_x > 800 or player.player_y > 600 or player.player_y < 0:
        return True
    if snake_head in snake_list[:-1]:
        return True
    return False

def controls_west_east(snake_direction):
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        player.player_x_dir = 20
        player.player_y_dir = 0
        snake_direction = 4
    if pygame.key.get_pressed()[pygame.K_LEFT] == True:
        player.player_x_dir = -20
        player.player_y_dir = 0
        snake_direction = 3
    return snake_direction

def controls_north_south(snake_direction):
    if pygame.key.get_pressed()[pygame.K_UP] == True:
        player.player_x_dir = 0
        player.player_y_dir = -20
        snake_direction = 1

    if pygame.key.get_pressed()[pygame.K_DOWN] == True:
        player.player_x_dir = 0
        player.player_y_dir = 20
        snake_direction = 2
    return snake_direction

def game_over(score):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            screen.fill((0,0,0))

            title_1 = title.render(f'Your final score is {score}' , True , (255,255,255)) 
            screen.blit(title_1, (width/2 - 160, height/2 - 120))

            text_1 = font.render('Play Again' , True , (255,255,255)) 
            pygame.draw.rect(screen, (255,255,255), (width/2 - 65, height/2 - 45, 150, 40), 1)
            screen.blit(text_1, (width/2 - 55, height/2 - 40))

            text_2 = font.render('Quit' , True , (255,255,255)) 
            pygame.draw.rect(screen, (255,255,255), (width/2 - 65, height/2 + 20, 150, 40), 1)
            screen.blit(text_2, (width/2 - 25, height/2 + 30)) 

            mouse_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 - 65 <= mouse_pos[0] <= width/2 + 95 and height/2 - 45 <= mouse_pos[1] <= height/2 - 5:
                    return False
                elif width/2 - 65 <= mouse_pos[0] <= width/2 + 95 and height/2 + 20 <= mouse_pos[1] <= height/2 + 60:
                    return True

            pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    screen.blit(title_1, (width/2 - 50,height/2 - 120))
    screen.blit(text_1, (width/2 - 55,height/2 - 40))
    screen.blit(text_2, (width/2 - 25,height/2 + 30)) 
    screen.blit(text_3, (width/2 - 20,height/2 + 95)) 

    mouse_pos = pygame.mouse.get_pos()

    if e.type == pygame.MOUSEBUTTONDOWN:
        if width/2 - 65 <= mouse_pos[0] <= width/2 + 95 and height/2 - 45 <= mouse_pos[1] <= height/2 - 5:
            break
        elif width/2 - 65 <= mouse_pos[0] <= width/2 + 95 and height/2 + 20 <= mouse_pos[1] <= height/2 + 60:
            print("Rules")
        elif width/2 - 65 <= mouse_pos[0] <= width/2 + 95 and height/2 + 85 <= mouse_pos[1] <= height/2 + 125:
            exit()

    pygame.display.update()
        
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

    draw_snake(snake_list)

    if snake_direction == 1:
        snake_direction = controls_west_east(snake_direction)
    elif snake_direction == 2:
        snake_direction = controls_west_east(snake_direction)
    elif snake_direction == 3:
        snake_direction = controls_north_south(snake_direction)
    elif snake_direction == 4:
        snake_direction = controls_north_south(snake_direction)

    while food_exist == False:
        # Make it so that it works with body
        food_x = round(random.randrange(0, 800 - 20) / 20.0) * 20.0
        food_y = round(random.randrange(0, 600 - 20) / 20.0) * 20.0
        food_exist = True

    pygame.draw.rect(screen, (255,0,0), (food_x, food_y, 20, 20), 5)
    
    pygame.display.update()

    if collision(snake_list, snake_head):
        if not game_over(score):
            score = 0
            snake_list = []
            snake_length = 4
            player.player_x = 400
            player.player_y = 300
            player.player_x_dir = 20
            player.player_y_dir = 0
            snake_head = []
            food_exist = False

        elif game_over(score):
            exit()

    if player.player_mask.overlap(food_mask, offset()):
        score += 1
        snake_length += 1
        food_exist = False

    pygame.display.update()

    clock.tick(15)

        









