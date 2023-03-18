import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Создание окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Настройки игры
BLOCK_SIZE = 10
SPEED = 10


# Функция рисования змейки
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])


# Главная функция игры
def game_loop():
    # Начальное положение змейки
    snake_list = []
    snake_length = 1
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    x_change = 0
    y_change = 0

    # Начальное положение еды
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    # Основной цикл игры
    game_over = False
    while not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Перемещение змейки
        x += x_change
        y += y_change

        # Проверка на столкновение со стеной
        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_over = True

        # Проверка на столкновение с едой
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        # Отрисовка фона
        screen.fill(BLACK)

        # Отрисовка еды
        pygame.draw.rect(screen, WHITE, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Добавление головы змейки
        snake_head = [x, y]
        snake_list.append(snake_head)

        # Удаление хвоста змейки, если ее длина больше, чем snake_length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Отрисовка змейки
        draw_snake(snake_list)

        # Обновление экрана
        pygame.display.update()

        # Задержка для создания эффекта анимации
        pygame.time.Clock().tick(20)

        # Закрытие окна Pygame
    pygame.quit()


# Запуск игры
game_loop()
