# Example file showing a basic pygame "game loop"
import os

import pygame

# pygame setup
_max_width = 1280
_max_height = 720

pygame.init()
screen = pygame.display.set_mode((_max_width, _max_height))
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
surf = pygame.image.load(os.path.join('space.jpg')).convert()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(surf)

    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()