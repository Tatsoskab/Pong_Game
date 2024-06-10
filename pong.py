import pygame
import random

pygame.init()

win_color = (110, 163, 204)
win_width = 1250
win_height = 800
height = 120
width = 20
x_pos = 20
y_pos = (win_height / 2) - height
x_ball = (win_width / 2) - width
y_ball = (win_height / 2) - width
vel = 8
ball_x_vel = 4
ball_y_vel = 2
running = True
run = True

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pong")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Key movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y_pos > 0:
        y_pos -= vel
    if keys[pygame.K_s] and y_pos < win_height - height:
        y_pos += vel

    if running:
        x_ball += ball_x_vel
        y_ball += ball_y_vel

        # Ball collision with walls
        if x_ball >= win_width - width or x_ball <= 0:
            ball_x_vel = -ball_x_vel
        if y_ball >= win_height - width or y_ball <= 0:
            ball_y_vel = -ball_y_vel

    window.fill(win_color)
    Player = pygame.draw.rect(window, (0, 0, 0), (x_pos, y_pos, width, height))
    Ball = pygame.draw.rect(window, (0, 0, 0), (x_ball, y_ball, width, width))

    pygame.time.delay(8)
    pygame.display.update()

pygame.quit()
