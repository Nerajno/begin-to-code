import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))

finished = False
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            print('event.unicode', event.unicode)
            print('event.key', event.key)
            print('event.mod', event.mod)
        elif event.type == pygame.MOUSEBUTTONDOWN or \
             event.type == pygame.MOUSEBUTTONUP:
            print('event.pos', event.pos)
            print('event.button', event.button)
        elif event.type == pygame.MOUSEMOTION:
            print('event.pos', event.pos)
            print('event.buttons', event.buttons)
            print('event.rel', event.rel)

print('Bye!!!')
pygame.quit()
