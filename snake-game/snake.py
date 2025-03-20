import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake and food properties
snake_block = 20
base_speed = 10  # Starting speed (slower than original 15)
max_speed = 25   # Maximum speed limit

# Initialize clock
clock = pygame.time.Clock()

# Font for score and messages
font = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 30)

# Global variable for best score
best_score = 0

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [x, y])

def show_score(score, best_score, current_speed):
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    best_score_text = score_font.render(f"Best Score: {best_score}", True, WHITE)
    speed_text = score_font.render(f"Speed: {current_speed}", True, WHITE)
    window.blit(score_text, [0, 0])
    window.blit(best_score_text, [0, 30])
    window.blit(speed_text, [0, 60])

def gameLoop():
    global best_score
    
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    current_score = 0
    snake_speed = base_speed  # Start with base speed

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            window.fill(BLACK)
            message("You Lost!", RED, width/6, height/3)
            message("Press Q-Quit or C-Play Again", WHITE, width/6, height/2)
            show_score(current_score, best_score, snake_speed)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        show_score(current_score, best_score, snake_speed)
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            current_score += 1
            # Increase speed every 5 points, but don't exceed max_speed
            if current_score % 5 == 0:
                snake_speed = min(base_speed + (current_score // 5) * 2, max_speed)
            if current_score > best_score:
                best_score = current_score

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
