import pygame
import random

game_on = True

screen = pygame.display.set_mode((800, 600))
game_on = True

player_x = 400
player_y = 300

food_x = 0
food_y = 0

def food():
    pygame.draw.rect(screen, (255,0,0), (x, y, 20, 20), 5)




while game_on:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
            
    pygame.draw.rect(screen, (255,0,0), (player_x, player_y, 20, 20), 5)

    while True:
        food_x = random.randint(0, 800)
        food_y = random.randint(0, 600)
        if (food_x <= player_x - 20 or food_x >= player_x + 20) and (food_y <= player_y - 20 or food_y >= player_y + 20):
            break
        
    pygame.draw.rect(screen, (255,0,0), (food_x, food_y, 20, 20), 5)
    
    pygame.display.update()

        









