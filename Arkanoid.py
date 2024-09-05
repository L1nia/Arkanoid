import pygame
from pygame.locals import *
import sys

pygame.init()

# Определяем параметры окна
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

# Создаем окно игры
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")

# Параметры мяча
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
velocity = [4, 4]

# Параметры платформы
platform = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 20, 120, 10)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and platform.left > 0:
        platform.left -= 5
    if keys[K_RIGHT] and platform.right < WIDTH:
        platform.right += 5

    ball.left += velocity[0]
    ball.top += velocity[1]

    if ball.left <= 0 or ball.right >= WIDTH:
        velocity[0] = -velocity[0]
    if ball.top <= 0 or ball.colliderect(platform):
        velocity[1] = -velocity[1]

    if ball.top >= HEIGHT:
        ball.left, ball.top = WIDTH // 2 - 15, HEIGHT // 2 - 15
        velocity = [4, 4]

    window.fill(WHITE)
    pygame.draw.ellipse(window, (255, 0, 0), ball)
    pygame.draw.rect(window, (0, 0, 255), platform)
    pygame.display.flip()

    pygame.time.Clock().tick(FPS)

