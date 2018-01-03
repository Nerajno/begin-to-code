import pygame

def draw_car(screen, x, y):
    pygame.draw.circle(screen, BLUE, (x, y), 50)

def draw_tree(screen, x, y):
    pygame.draw.polygon(
        screen,
        GREEN,
        [(x, y), (x + 50, y + 50), (x - 50, y + 50)])
    pygame.draw.polygon(
        screen,
        GREEN,
        [(x, y + 20), (x + 50, y + 70), (x - 50, y + 70)])
    pygame.draw.polygon(
        screen,
        GREEN,
        [(x, y + 40), (x + 50, y + 90), (x - 50, y + 90)])
    pygame.draw.rect(screen, GREEN, (x - 20, y + 40, 40, 40))

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ball')
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialization
tree_x = SCREEN_WIDTH
exit_game = False

while not exit_game:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            exit_game = True

    # Automatic Updates
    tree_x -= 5

    # Rendering
    screen.fill(BLACK)
    draw_car(screen, 100, 300)
    draw_tree(screen, tree_x, 300)
    pygame.display.update()

pygame.quit()
