import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

image = pygame.image.load('images/LOLCat.jpg')

screen.fill((0, 0, 0))
screen.blit(image, (0, 0))

pygame.display.update()

while True:
    pass
