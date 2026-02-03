import pygame, sys
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
dt = 0

player_position = (pygame.Vector2(screen_width / 2, screen_height - 50))
player = pygame.image.load("images/player.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    pygame.draw.aacircle(screen, (255,0,0), player_position,40)
    screen.blit(player,(player_position.x,player_position.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position.x -= 100 * dt
    if keys[pygame.K_RIGHT]:
        player_position.x += 100 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000
