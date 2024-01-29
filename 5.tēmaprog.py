import pygame
import sys
import time
import random

# Inicializējam Pygame
pygame.init()

# Iestatījumi
width, height = 640, 480
cell_size = 20
snake_speed = 15

# Krāsas
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Uzstādījumi ekrāna
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Funkcija, lai zīmētu čūsku
def draw_snake(snake, cell_size):
    for segment in snake:
        pygame.draw.rect(screen, white, [segment[0], segment[1], cell_size, cell_size])

# Funkcija, lai zīmētu augli
def draw_apple(apple_position, cell_size):
    pygame.draw.rect(screen, red, [apple_position[0], apple_position[1], cell_size, cell_size])

# Spēles galvenā funkcija
def game():
    # Sākuma stāvoklis čūskas un augļa
    snake = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction
    score = 0

    # Izvietojam pirmo augli
    apple_position = [random.randrange(1, (width//cell_size)) * cell_size,
                      random.randrange(1, (height//cell_size)) * cell_size]

    while True:
        # Apstrādājam notikumus
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Izmaiņas virzienā
        if change_to == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'

        # Kustējam čūsku
        if direction == 'UP':
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = snake[i - 1].copy()
            snake[0][1] -= cell_size
        if direction == 'DOWN':
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = snake[i - 1].copy()
            snake[0][1] += cell_size
        if direction == 'LEFT':
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = snake[i - 1].copy()
            snake[0][0] -= cell_size
        if direction == 'RIGHT':
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = snake[i - 1].copy()
            snake[0][0] += cell_size

        # Čūska ēd augli
        if snake[0][0] == apple_position[0] and snake[0][1] == apple_position[1]:
            # Izveidojam jaunu augli
            apple_position = [random.randrange(1, (width//cell_size)) * cell_size,
                              random.randrange(1, (height//cell_size)) * cell_size]
            # Pieskaitām punktus
            score += 1
        else:
            # Ja čūska nav ēdusi augli, tad noņemam pēdējo segmentu
            snake.pop()

        # Pārbaudam sadursmes ar sienām
        if snake[0][0] < 0 or snake[0][0] == width or snake[0][1] < 0 or snake[0][1] == height:
            pygame.quit()
            sys.exit()

        # Pārbaudam sadursmes ar pašu sevi
        for segment in snake[1:]:
            if snake[0][0] == segment[0] and snake[0][1] == segment[1]:
                pygame.quit()
                sys.exit()

        # Zīmējam ekrānu
        screen.fill(black)
        draw_snake(snake, cell_size)
        draw_apple(apple_position, cell_size)

        # Atjaunojam ekrānu
        pygame.display.update()

        # Noteiksim čūskas ātrumu
        pygame.time.Clock().tick(snake_speed)

# Izpildīsim spēli
game()
