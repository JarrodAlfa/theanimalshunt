import pygame
from map import GameMap

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animals Forest Shooter")
clock = pygame.time.Clock()

game_map = GameMap(WIDTH, HEIGHT)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_map.update()
    game_map.draw(screen)
    pygame.display.flip()

pygame.quit()