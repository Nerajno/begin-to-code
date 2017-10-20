import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
