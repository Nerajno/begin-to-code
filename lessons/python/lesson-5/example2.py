import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Example')

while True:
    for event in pygame.event.get():
        print("Got event %r" % event)
