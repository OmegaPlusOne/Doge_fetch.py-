import pygame

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

fps_clock = pygame.time.Clock()
fps = 60

throw = False
throw_count = 10


def draw(ball_x, ball_y):
    global walk_count

    game_display.fill(black)
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

    pygame.display.update()

def game_loop():
    ball_x = 100
    ball_y = 100
    ball_size = 75

    global left
    global right
    global up
    global down
    global standing

    left = False
    right = False
    up = False
    down = False
    standing = False
    vel = 5

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

            # if keys[pygame.K_SPACE]:
            #     throw = True
            #     left = False
            #     right = False
            #     up = False
            #     down = False
            #     walk_count = 0

        # else:
        #     if throw_count >= -10:
        #         neg = 1
        #         if throw_count < 0:
        #             neg = -1
        #         ball_y -= (throw_count ** 2) * .3 * neg
        #         throw_count -= 1
        #     else:
        #         throw = False
        #         throw_count = 10

        draw(ball_x, ball_y)
        fps_clock.tick(fps)


game_loop()
pygame.quit()
quit()
