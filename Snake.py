import pygame
import random
import numpy as np
from enum import Enum

pygame.init()

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class Snake():

    def __init__(self):
        self.x = 400
        self.y = 300
        self.head = []
        self.list = []
        self.length = 4
        self.direction = 2
        self.mask = pygame.mask.Mask((20, 20), True)
        self.head.append(self.x)
        self.head.append(self.y)
        self.list.append(self.head)

    def draw_snake(self, screen):
        for x in self.list:
            pygame.draw.rect(screen, (255, 0, 0), [x[0], x[1], 20, 20], 5)

    def collision(self):
        if self.x < 0 or self.x > 800 or self.y > 600 or self.y < 0:
            return True
        if self.head in self.list[:-1]:
            return True
        return False

class Food():

    def __init__(self):
        self.x, self.y = self.make_food()
        self.mask = pygame.mask.Mask((20, 20), True)
        self.exist = True
    
    def make_food():
        x = round(random.randrange(0, 800 - 20) / 20.0) * 20.0
        y = round(random.randrange(0, 600 - 20) / 20.0) * 20.0
        return x, y

    def draw_food(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 20), 5)

class SnakeGameAI:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 25)
        self.title = pygame.font.Font(pygame.font.get_default_font(), 40)
        self.clock = pygame.time.Clock()
        self.reset()
    
    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.score = 0
    
    def offset(self):
        return int(self.snake.x - self.food.x), int(self.snake.y - self.food.y)

    def play_step(self, action):

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        self.screen.fill((0,0,0))
        text = self.font.render("Score: " + str(score), True, (255, 255, 255))
        self.screen.blit(text, [0, 0])
        pygame.display.set_caption('Snake') 

        if len(self.snake.list) > self.snake.length:
            del self.snake.list[0]

        reward = 0
        
        if self.snake.collision():
            self.game_over = True
            reward = -100
            return reward, self.game_over, self.score
        
        if self.snake.mask.overlap(self.food.mask, self.offset(self)):
            self.score += 1
            self.snake.length += 1
            reward = 10
            self.food = Food()
        
        pygame.display.update()

        self.clock.tick(15)

        return self.get_state(), reward, self.game_over, self.score
    
    def get_state(self):
        snake_head = self.snake.head

        check_left = snake_head[0] - 20
        check_right = snake_head[0] + 20
        check_up = snake_head[1] - 20
        check_down = snake_head[1] + 20

        is_leftdir = self.snake.direction == Direction.LEFT
        is_rightdir = self.snake.direction == Direction.RIGHT
        is_updir = self.snake.direction == Direction.UP
        is_downdir = self.snake.direction == Direction.DOWN

        state = [

            (is_leftdir and self.snake.collision(check_left)) or
            (is_rightdir and self.snake.collision(check_right)) or 
            (is_updir and self.snake.collision(check_up)) or
            (is_downdir and self.snake.collision(check_down)),

            (is_leftdir and self.snake.collision(check_up)) or 
            (is_rightdir and self.snake.collision(check_down)) or
            (is_updir and self.snake.collision(check_right)) or
            (is_downdir and self.snake.collision(check_left)),

            (is_leftdir and self.snake.collision(check_down)) or 
            (is_rightdir and self.snake.collision(check_up)) or
            (is_updir and self.snake.collision(check_left)) or
            (is_downdir and self.snake.collision(check_right)),

            is_leftdir,
            is_rightdir,
            is_updir,
            is_downdir,

            self.snake_head[0] > self.food.x, #food left
            self.snake_head[0] < self.food.x, #food right
            self.snake_head[1] > self.food.y, #food up
            self.snake_head[1] < self.food.y, #food down
        ]

        return np.array(state, dtype=int)
    
def controls_west_east(snake_direction):
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        player.action = [0,0,1,0,0]
    elif pygame.key.get_pressed()[pygame.K_LEFT] == True:
        player.action = [0,1,0,0,0]
    
    if np.array_equal(player.action, [0,0,1,0,0]):
        player.player_x_dir = 20
        player.player_y_dir = 0
        snake_direction = 4
        player.action = [1,0,0,0,0]

    if np.array_equal(player.action, [0,1,0,0,0]):
        player.player_x_dir = -20
        player.player_y_dir = 0
        snake_direction = 3
        player.action = [1,0,0,0,0]

    return snake_direction

def controls_north_south(snake_direction):
    if pygame.key.get_pressed()[pygame.K_UP] == True:
        player.action = [0,0,0,1,0]

    if np.array_equal(player.action, [0,0,0,1,0]):
        player.player_x_dir = 0
        player.player_y_dir = -20
        snake_direction = 1
        player.action = [1,0,0,0,0]

    if pygame.key.get_pressed()[pygame.K_DOWN] == True:
        player.action = [0,0,0,0,1]

    if np.array_equal(player.action, [0,0,0,0,1]):
        player.player_x_dir = 0
        player.player_y_dir = 20
        snake_direction = 2
        player.action = [1,0,0,0,0]

    return snake_direction


def gameStart():
    while game_on:


        pygame.display.set_caption('Snake')    

        player.player_x += player.player_x_dir
        player.player_y += player.player_y_dir

        if snake_direction == 1:
            snake_direction = controls_west_east(snake_direction)
        elif snake_direction == 2:
            snake_direction = controls_west_east(snake_direction)
        elif snake_direction == 3:
            snake_direction = controls_north_south(snake_direction)
        elif snake_direction == 4:
            snake_direction = controls_north_south(snake_direction)









