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

game_display = pygame.display.set_mode((width, height))

pygame.display.set_caption("doge.init()")

walk_left = [pygame.image.load("images/walk_left01.png"), pygame.image.load("images/walk_left02.png"),
             pygame.image.load("images/walk_left03.png"), pygame.image.load("images/walk_left04.png")]
walk_right = [pygame.image.load("images/walk_right01.png"), pygame.image.load("images/walk_right02.png"),
              pygame.image.load("images/walk_right03.png"), pygame.image.load("images/walk_right04.png")]
walk_up = [pygame.image.load("images/walking_up01.png"), pygame.image.load("images/walking_up02.png"),
           pygame.image.load("images/walking_up03.png"), pygame.image.load("images/walking_up04.png")]
walk_down = [pygame.image.load("images/walking_forward01.png"), pygame.image.load("images/walking_forward02.png"),
             pygame.image.load("images/walking_forward03.png"), pygame.image.load("images/walking_forward04.png")]
sitting = [pygame.image.load("images/sit04.png")]
heart_img = [pygame.image.load("images/h2.png")]

font = pygame.font.SysFont('8bitoperatorregular', 20)

fps_clock = pygame.time.Clock()
fps = 60


def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_screen(msg, color):
    text_surface, text_rect = text_objects(msg, color)
    text_rect.center = (width/2), (height/2)
    game_display.blit(text_surface, text_rect)


def draw(ball_x, ball_y):
    global walk_count

    if walk_count + 1 >= 24:
        walk_count = 0

    if left:
        game_display.blit(walk_left[walk_count//6], (ball_x, ball_y))
        walk_count += 1
    elif right:
        game_display.blit(walk_right[walk_count // 6], (ball_x, ball_y))
        walk_count += 1
    elif up:
        game_display.blit(walk_up[walk_count // 6], (ball_x, ball_y))
        walk_count += 1
    elif down:
        game_display.blit(walk_down[walk_count // 6], (ball_x, ball_y))
        walk_count += 1
    else:
        game_display.blit(sitting[0], (ball_x, ball_y))


def game_loop():
    ball_x = 100
    ball_y = 100
    ball_size = 70
    apple_size = 25
    lv = 0

    global left
    global right
    global up
    global down
    global standing
    global throw
    global throw_count

    throw = False
    throw_count = 10
    left = False
    right = False
    up = False
    down = False
    standing = False
    vel = 5

    apple_x = round(random.randrange(0, width - apple_size))
    apple_y = round(random.randrange(0, height - apple_size))

    global walk_count
    walk_count = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if not throw:
            if keys[pygame.K_ESCAPE]:
                run = False

            if keys[pygame.K_LEFT] and ball_x > vel:
                ball_x -= vel
                left = True
                right = False
                up = False
                down = False

            elif keys[pygame.K_RIGHT] and ball_x < width - ball_size - vel:
                ball_x += vel
                left = False
                right = True
                up = False
                down = False

            elif keys[pygame.K_UP] and ball_y > vel:
                ball_y -= vel
                left = False
                right = False
                up = True
                down = False

            elif keys[pygame.K_DOWN] and ball_y < height - ball_size - vel:
                ball_y += vel
                left = False
                right = False
                up = False
                down = True

            else:
                left = False
                right = False
                up = False
                down = False
                walk_count = 0

            if keys[pygame.K_SPACE]:
                throw = True
                left = False
                right = False
                up = False
                down = False
                walk_count = 0

        else:
            if throw_count >= -10:
                neg = 1
                if throw_count < 0:
                    neg = -1
                ball_y -= (throw_count ** 2) * .3 * neg
                throw_count -= 1
            else:
                throw = False
                throw_count = 10

        game_display.fill(black)
        message_screen(("times loved: " + str(lv)), white)
        game_display.blit(heart_img[0], (apple_x, apple_y))
        draw(ball_x, ball_y)
        pygame.display.update()

        if ball_x > apple_x and ball_x < apple_x + apple_size or ball_x + ball_size > apple_x and ball_x + ball_size < apple_x + apple_size:
            if ball_y > apple_y and ball_y < apple_y + apple_size or ball_y + ball_size > apple_y and ball_y + ball_size < apple_y + apple_size:
                apple_x = round(random.randrange(0, width - apple_size) / 10.0) * 10
                apple_y = round(random.randrange(0, height - apple_size) / 10.0) * 10
                lv += 1

        fps_clock.tick(fps)


game_loop()
pygame.quit()
quit()
