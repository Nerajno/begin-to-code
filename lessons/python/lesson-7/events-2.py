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

print('Bye!!!')
pygame.quit()
