import pygame
import sys
from pygame.math import Vector2
import random


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1, 0)
        self.ab = False

    def draw_snake(self):
        for block in self.body:
            sb_rect = pygame.Rect(int(block.x*cell_size),int(block.y*cell_size),cell_size,cell_size)
            pygame.draw.rect(screen, (0,0,255),sb_rect)
    
    def move_snake(self):
        if self.ab:
            body_old = self.body[:]
        else:
            body_old = self.body[:-1]
        body_old.insert(0,body_old[0]+self.direction)
        self.body = body_old
        self.ab = False

    def add_block(self):
        self.ab = True

class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x)*cell_size,int(self.pos.y)*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255, 0, 0),fruit_rect)
    
    def randomize(self, available):
        self.pos = random.choice(available)
        

class Main:

    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            a = []

            for row in range(cell_number):
                for col in range(cell_number):
                    if Vector2(row, col) in self.snake.body:
                        pass
                    else:
                        a.append(Vector2(row, col))
            
            if len(a) < 1:
                self.game_over()
            self.fruit.randomize(available=a)
            self.snake.add_block()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        return False

    def game_over(self):
        pygame.quit()
        sys.exit()
    
    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score = game_font.render(score_text,True,(56, 74, 12))

        score_rect = score.get_rect(center=(int(cell_size*cell_number-60), int(cell_size*cell_number-40)))
        screen.blit(score, score_rect)
cell_size = 40
cell_number = 20

pygame.init()
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()

main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

game_font = pygame.font.Font(None, 25)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snake.direction == Vector2(0, 1):
                    pass
                else:
                    main_game.snake.direction.x = 0
                    main_game.snake.direction.y = -1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction == Vector2(0, -1):
                    pass
                else:
                    main_game.snake.direction.x = 0
                    main_game.snake.direction.y = 1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction == Vector2(-1, 0):
                    pass
                else:
                    main_game.snake.direction.x = 1
                    main_game.snake.direction.y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snake.direction == Vector2(1, 0):
                    pass
                else:
                    main_game.snake.direction.x = -1
                    main_game.snake.direction.y = 0
            
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(120)