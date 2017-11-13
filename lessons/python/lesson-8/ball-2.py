import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ball')
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialization
ball_x = 300
ball_y = 200
exit_game = False

while not exit_game:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= 5
            elif event.key == pygame.K_DOWN:
                ball_y += 5
            elif event.key == pygame.K_LEFT:
                ball_x -= 5
            elif event.key == pygame.K_RIGHT:
                ball_x += 5

    # Rendering
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
    pygame.display.update()

pygame.quit()
