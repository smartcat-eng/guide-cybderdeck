import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screenW, screenH = screen.get_size()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            movement = event.rel


    screen.fill((50, 50, 50))
    pygame.display.flip()