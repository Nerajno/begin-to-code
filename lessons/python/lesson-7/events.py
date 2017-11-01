import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))

while True:
    new_events = pygame.event.get()
    for event in new_events:
        print('Got event', event)
        # if event.type == pygame.QUIT:
        #     print('You are quitting!!!')
        # else:
        #     print('Other', event.type)

pygame.quit()
