import pygame
import random

pygame.init()

win_color = (110, 163, 204)
win_width = 1250
win_height = 800
height = 120
width = 20
pos1_x = 30
pos2_x = 1200
pos1_y = (win_height / 2) - (height / 2)
pos2_y = (win_height / 2) - (height / 2)
x_ball = (win_width / 2) - (width / 2)
y_ball = (win_height / 2) - (width / 2)
vel = 8
player_score1 = 0 
player_score2 = 0
ball_x_vel = 4
ball_y_vel = 2
running = True
run = True
font = pygame.font.Font(None, 36)

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pong")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(win_color)
    Player1 = pygame.draw.rect(window, (0, 0, 0), (pos1_x, pos1_y, width, height))
    Player2 = pygame.draw.rect(window, (0, 0, 0), (pos2_x, pos2_y, width, height))
    Ball = pygame.draw.rect(window, (0, 0, 0), (x_ball, y_ball, width, width))

    if Ball.colliderect(Player1):
        ball_x_vel = -ball_x_vel
        # Adjust ball position to avoid getting stuck
        if x_ball < pos1_x + width:
            x_ball = pos1_x + width
    if Ball.colliderect(Player2):
        ball_x_vel = -ball_x_vel
        # Adjust ball position to avoid getting stuck
        if x_ball > pos2_x + width:
            x_ball = pos2_x + width
    # Key movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pos1_y > 0:
        pos1_y -= vel
    if keys[pygame.K_s] and pos1_y < win_height - height:
        pos1_y += vel
    if keys[pygame.K_UP] and pos2_y > 0:
        pos2_y -= vel
    if keys[pygame.K_DOWN] and pos2_y < win_height - height:
        pos2_y += vel

    if running:
        x_ball += ball_x_vel
        y_ball += ball_y_vel
        # Ball collision with walls
        if x_ball >= win_width - width:
            player_score1 += 1
        if x_ball <= 0:
            player_score2 += 1

        if y_ball >= win_height - width or y_ball <= 0:
            ball_y_vel = -ball_y_vel
    
    # Render score texts
    score1 = font.render(str(player_score1), True, (0, 0, 0))
    score1_rect = score1.get_rect(center=(win_width//4, 50))

    score2 = font.render(str(player_score2), True, (0, 0, 0))
    score2_rect = score2.get_rect(center=(win_width*3//4, 50))

    # Blit score texts onto window
    window.blit(score1, score1_rect)
    window.blit(score2, score2_rect)
    
    pygame.time.delay(8)
    pygame.display.update()

pygame.quit()
