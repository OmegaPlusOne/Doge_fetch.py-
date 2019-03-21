import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
apple_red = (145, 28, 20)
deep_red = (127, 19, 19)
head_color = (37, 84, 49)
background = (178, 178, 178)

width = 800
height = 600

ball_x = width/7
ball_y = height/2
ball_x_change = 0
ball_y_change = 0

fps_clock = pygame.time.Clock()
fps = 90

move_x = False
move_x_count = 10
move_y = False
move_y_count = 10
reset = False
dist = 10


ball_size = 10

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("doge.fetch")

game_exit = False

while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if not move_x and not move_y:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("you Just threw the ball (feature added later)")
                move_x = True
                move_y = True

    keys = pygame.key.get_pressed()

    if not move_x and not move_y:
        if keys[pygame.K_ESCAPE]:
            game_exit = True
        if keys[pygame.K_SPACE]:
            move_x = True
            move_y = True
    else:
        if move_x_count >= -10:
            neg = 1
            if move_x_count < 0:
                neg = -1

            ball_x += 25
            ball_y -= (move_y_count ** 2) * .3 * neg
            move_x_count -= 1
            move_y_count -= 1
        else:
            move_x = False
            move_x_count = 10
            move_y_count = 10
            move_y = False
            reset = True

    if reset:
        pygame.time.delay(1000)
        ball_y = height / 2
        ball_x = width / 7
        reset = False

    game_display.fill(black)
    pygame.draw.rect(game_display, white, (ball_x, ball_y, ball_size, ball_size))
    pygame.display.update()
    fps_clock.tick(fps)

pygame.quit()
quit()
