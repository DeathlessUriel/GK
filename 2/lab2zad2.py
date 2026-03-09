import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kształt")

WHITE = (220, 220, 220)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # prostokąt
    rect = pygame.Rect(200, 260, 200, 80)
    pygame.draw.rect(screen, BLUE, rect)

    # górny trójkąt (styka się z prostokątem)
    top_triangle = [(260, 160), (340, 160), (300, 260)]
    pygame.draw.polygon(screen, BLUE, top_triangle)

    # dolny trójkąt (styka się z prostokątem)
    bottom_triangle = [(260, 440), (340, 440), (300, 340)]
    pygame.draw.polygon(screen, BLUE, bottom_triangle)

    pygame.display.flip()
    clock.tick(60)