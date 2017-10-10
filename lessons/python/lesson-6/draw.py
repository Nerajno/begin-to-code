import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Example')

screen.fill((255, 255, 255))

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == 8:
                print('COMMAND: Clear screen')
                screen.fill((255, 255, 255))
                pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 20, 0)
            pygame.display.update()

pygame.quit()
