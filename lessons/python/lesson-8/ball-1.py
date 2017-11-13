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
    # Rendering
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
    pygame.display.update()

pygame.quit()
