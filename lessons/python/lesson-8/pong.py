import pygame

pygame.init()
font = pygame.font.Font(None, 40)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

player1_score = 0
player2_score = 0
paddle1_y = SCREEN_HEIGHT / 2
paddle1_delta_y = 1.8
paddle1_x = 50
paddle2_y = SCREEN_HEIGHT / 2
paddle2_x = SCREEN_WIDTH - 50
ball_x = 400
ball_y = 300
ball_delta_x = 5
ball_delta_y = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.MOUSEMOTION:
            y = event.pos[1]
            paddle2_y = min(y, 500)

    ball_x += ball_delta_x
    ball_y += ball_delta_y

    if paddle1_y + 50 > ball_y and ball_delta_y < 0:
        paddle1_y -= paddle1_delta_y
    if paddle1_y + 50 < ball_y and ball_delta_y > 0:
        paddle1_y += paddle1_delta_y

    if ball_x + 5 > paddle2_x\
    and ball_x + 5 <= paddle2_x + 10\
    and ball_y < paddle2_y + 100\
    and ball_y > paddle2_y:
        ball_delta_x *= -1
        ball_x += ball_delta_x
    if ball_x - 5 < paddle1_x\
    and ball_x - 5 >= paddle1_x - 10\
    and ball_y < paddle1_y + 100\
    and ball_y > paddle1_y:
        ball_delta_x *= -1
        ball_x += ball_delta_x
    if ball_y + 5 > SCREEN_HEIGHT:
        ball_delta_y *= -1
        ball_y += ball_delta_y
    if ball_y - 5 < 0:
        ball_delta_y *= -1
        ball_y += ball_delta_y

    if ball_x >= SCREEN_WIDTH:
        player1_score += 1
        paddle1_y = 300
        paddle2_y = 300
        ball_x = 400
        ball_y = 300
    if ball_x <= 0:
        player2_score += 1
        paddle1_y = 300
        paddle2_y = 300
        ball_x = 400
        ball_y = 300

    screen.fill(BLACK)
    score1 = font.render(str(player1_score), False, WHITE)
    screen.blit(score1, (300, 100))
    score2 = font.render(str(player2_score), False, WHITE)
    screen.blit(score2, (500, 100))
    pygame.draw.circle(
        screen,
        WHITE,
        (ball_x, ball_y),
        5)
    pygame.draw.line(screen,
        WHITE,
        (paddle1_x, paddle1_y),
        (paddle1_x, paddle1_y + 100),
        10)
    pygame.draw.line(screen,
        WHITE,
        (paddle2_x, paddle2_y),
        (paddle2_x, paddle2_y + 100),
        10)
    pygame.display.update()

pygame.quit()
