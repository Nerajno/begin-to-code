import pygame

pygame.init()
pygame.display.set_caption('A House')
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Draw the rectangle for the house's front wall
pygame.draw.rect(screen, GREEN, (300, 300, 200, 150))

# Two windows
pygame.draw.rect(screen, BLUE, (320, 320, 50, 50))
pygame.draw.rect(screen, BLUE, (430, 320, 50, 50))

# A door
pygame.draw.rect(screen, RED, (375, 375, 50, 75))

# The door nob
pygame.draw.circle(screen, GREEN, (412, 415), 5, 0)

# The roof
pygame.draw.polygon(screen, RED, [(400, 150), (275, 300), (525, 300)])

pygame.display.update()
while True:
    pass
