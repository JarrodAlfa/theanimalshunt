import pygame, sys

from simulation import Simulation
# pygame setup
pygame.init()

winWidth = 1280
winHeight = 720
fps = 12
cellSize = 8

#colors
grey = (29,29,29)

window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

simulation = Simulation(winWidth, winHeight, cellSize)

#Simulation loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life RUNNING")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life STOPPED")
            elif event.key == pygame.K_f:
                fps += 2
            elif event.key == pygame.K_s:
                if fps > 5:
                    fps -= 2

    # Updating state
    simulation.update()

    # Drawing
    window.fill(grey)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(fps)