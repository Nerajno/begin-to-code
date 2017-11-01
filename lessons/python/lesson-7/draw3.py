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

last_pos_x = None
last_pos_y = None
pen_down = False

width = 5

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pen_down = False
                print("COMMAND: pen up")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pen_down = True
                print("COMMAND: pen down")
            elif event.key == 8:
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
            elif event.key == pygame.K_UP:
                width += 1
                print("COMMAND: increased width to %d" % width)
            elif event.key == pygame.K_DOWN:
                if width > 1:
                    width -= 1
                    print("COMMAND: decreased width to %d" % width)
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            if pen_down and last_pos_x and last_pos_y:
                pygame.draw.line(
                    screen,
                    color,
                    (last_pos_x, last_pos_y),
                    (x, y),
                    width)
                pygame.display.update()
            last_pos_x = x
            last_pos_y = y

pygame.quit()
