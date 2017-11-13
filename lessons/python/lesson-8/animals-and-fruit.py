import pygame
import random
import math

pygame.init()
font = pygame.font.Font(None, 50)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Happy Panda')

hero = pygame.image.load('images/animals/panda-100.png')
reward = pygame.image.load('images/fruits/banana-100.png')
villain = pygame.image.load('images/animals/snake-100.png')

hero_x = 0
hero_y = 0
hero_step_size = 100

reward_x = 700
reward_y = 500

villain_x = 600
villain_y = 400
villain_step_size = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (64, 128, 0)

won = False
lose = False
you_won_text = font.render('YOU WON!!!', True, WHITE)
you_lose_text = font.render('YOU LOSE!!!', True, WHITE)
enter_to_play_again_text = font.render('Hit ENTER to play again', True, WHITE)

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                won = False
                lose = False
                hero_x = 0
                hero_y = 0
                reward_x = 700
                reward_y = 500
                villain_x = 600
                villain_y = 400
            if not won and not lose:
                if event.key == pygame.K_UP:
                    hero_y -= hero_step_size
                if event.key == pygame.K_DOWN:
                    hero_y += hero_step_size
                if event.key == pygame.K_LEFT:
                    hero_x -= hero_step_size
                if event.key == pygame.K_RIGHT:
                    hero_x += hero_step_size

    if not won and not lose:
        villain_choice = random.randint(1, 15)
        if villain_choice == 1:
            villain_y -= villain_step_size
            if villain_y < 0:
                villain_y = 0
        elif villain_choice == 2:
            villain_y += villain_step_size
            if villain_y + 100 > SCREEN_HEIGHT:
                villain_y -= villain_step_size
        elif villain_choice == 3:
            villain_x -= villain_step_size
            if villain_x < 0:
                villain_x = 0
        elif villain_choice == 4:
            villain_x += villain_step_size
            if villain_x + 100 > SCREEN_WIDTH:
                villain_x -= villain_step_size

        distance_from_reward =\
        math.sqrt(math.pow(hero_x - reward_x, 2)\
        + math.pow(hero_y - reward_y, 2))
        if distance_from_reward <= 75:
            won = True

        distance_from_villain =\
        math.sqrt(math.pow(hero_x - villain_x, 2)\
        + math.pow(hero_y - villain_y, 2))
        if distance_from_villain <= 75:
            lose = True

    screen.fill(BACKGROUND_COLOR)
    if not won:
        screen.blit(reward, (reward_x, reward_y))
    if not lose:
        screen.blit(hero, (hero_x, hero_y))
    screen.blit(villain, (villain_x, villain_y))

    if won:
        screen.blit(you_won_text, (300, 300))
        screen.blit(enter_to_play_again_text, (200, 400))
    elif lose:
        screen.blit(you_lose_text, (300, 300))
        screen.blit(enter_to_play_again_text, (200, 400))

    pygame.display.update()

pygame.quit()
