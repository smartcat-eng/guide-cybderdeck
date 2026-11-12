import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)
screenW, screenH = screen.get_size()

button = pygame.Rect(0,150, screenW, 75)
size = 75
start = 75
names = ["Back", "Button1", "Button2", "Button3", "Button4", "Button5", "Button6"]

threshold = 50
acumulated = 0

font = pygame.font.Font(None, 50)
highlight = pygame.Rect(0, 0, screenW, size)
surfaces = []

for i, a in enumerate(names):
    surfaces.append(font.render(">" + " " + names[i], True, (255, 255, 255)))

idx = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        dx, dy = pygame.mouse.get_rel()
        acumulated += dy
        if acumulated > threshold:
            acumulated = 0;
            idx = (idx + 1) % len(surfaces)
        if acumulated < -threshold:
            acumulated = 0
            idx = (idx - 1) % len(surfaces)

    screen.fill((10, 12, 12))
    textRect = surfaces[idx].get_rect(topleft=(0, start + (size * idx)))
    highlight.centery = textRect.centery
    pygame.draw.rect(screen, (70, 192, 22), highlight)
    for i, a in enumerate(surfaces):
        if i !=0:
            screen.blit(surfaces[i], (0, (start + (size * (i-1)))))
        else:
            screen.blit(surfaces[i], (0, screenW - 100))

    pygame.display.flip()