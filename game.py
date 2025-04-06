import pygame
from pygame.locals import *
from snake import *
from apple import *

Running = True
WINDOW_SIZE = 800
SPEED = 10

pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()
snake = Snake()
apple = Apple()
apple.set_random_position(WINDOW_SIZE)
score = 0
font = pygame.font.Font(None, 36)

def display_score(score):
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text,(350, 10))

def display_game_over(score):
    screen.fill((0, 0, 0))
    text = font.render(f'GAME OVER! Score: {score}', True, (255, 0, 0))
    screen.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, WINDOW_SIZE // 2 - text.get_height() //2))
    pygame.display.update()
    pygame.time.wait(3000)

while Running:
    clock.tick(SPEED)
    snake.crawl()

    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False

        if event.type == KEYDOWN:
            if event.key==K_UP and snake.direction != DOWN:
                print("UP")
                snake.direction = UP
            elif event.key==K_LEFT and snake.direction != RIGHT:
                print("LEFT")
                snake.direction = LEFT
            elif event.key==K_DOWN and snake.direction != UP:
                print("DOWN")
                snake.direction  = DOWN
            elif event.key==K_RIGHT and snake.direction != LEFT:
                print("RIGHT")
                snake.direction = RIGHT
    if snake.wall_collision(WINDOW_SIZE) or snake.self_collision():
        display_game_over(score)
        Running = False

    if snake.snake_eat_apple(apple.position):
        apple.set_random_position(WINDOW_SIZE)
        snake.snake_bigger()
        score += 10
        SPEED += 1.0

    screen.fill((0, 0, 0))
    for snake_pos in snake.snake[0:-1]:
        screen.blit(snake.skin, snake_pos)
    screen.blit(snake.head, snake.snake[-1])
    screen.blit(apple.apple, apple.position)
    display_score(score)

    pygame.display.update()

pygame.quit()