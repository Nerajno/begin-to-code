import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Pygame Example')

ball_x = 250
ball_y = 250

screen.fill((255, 255, 255))

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.MOUSEMOTION:
            ball_x = event.pos[0]
            ball_y = event.pos[1]

    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 20, 0)
    pygame.display.update()

pygame.quit()
