import pygame

pygame.init()
pygame.display.set_caption('Mickey Mouse')
screen = pygame.display.set_mode((600, 400))

screen.fill((255, 255, 255))
pygame.draw.circle(screen, (0, 0, 0), (220, 120), 50, 0)
pygame.draw.circle(screen, (0, 0, 0), (380, 120), 50, 0)
pygame.draw.circle(screen, (0, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
