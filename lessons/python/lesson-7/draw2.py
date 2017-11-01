import pygame

colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]

color = colors[0]

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Example')

screen.fill((255, 255, 255))

exit_game = False
while not exit_game:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == 8:
                print('COMMAND: Clear screen')
                screen.fill((255, 255, 255))
                pygame.display.update()
            elif event.key == pygame.K_1:
                color = colors[0]
                print("COMMAND: change color to %r" % (color,))
            elif event.key == pygame.K_2:
                color = colors[1]
                print("COMMAND: change color to %r" % (color,))
            elif event.key == pygame.K_3:
                color = colors[2]
                print("COMMAND: change color to %r" % (color,))
            elif event.key == pygame.K_4:
                color = colors[3]
                print("COMMAND: change color to %r" % (color,))
            elif event.key == pygame.K_5:
                color = colors[4]
                print("COMMAND: change color to %r" % (color,))
            elif event.key == pygame.K_6:
                color = colors[5]
                print("COMMAND: change color to %r" % (color,))
            elif event.key == pygame.K_7:
                color = colors[6]
                print("COMMAND: change color to %r" % (color,))
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            pygame.draw.circle(screen, color, (x, y), 20, 0)
            pygame.display.update()

pygame.quit()
