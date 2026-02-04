import pygame, sys
import enemy, player, score

# general setup
pygame.init()
window_width, window_height = 1280, 720
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
fps = 60
dt = 0
game_score = score.Score()

pygame.display.set_caption('Arcade Shooter')
pygame.display.set_icon(pygame.image.load('logo.png').convert_alpha())

# import images
#levels
level_1 = pygame.image.load('level1.jpg').convert()
# animals
wolf_img = pygame.image.load('wolf.png').convert_alpha()
bat_img = pygame.image.load('bat.png').convert_alpha()
bear_img = pygame.image.load('bear.png').convert_alpha()
tiger_img = pygame.image.load('tiger.png').convert_alpha()
gorilla_img = pygame.image.load('gorilla.png').convert_alpha()
alligator_img = pygame.image.load('alligator.png').convert_alpha()
rex_img = pygame.image.load('rex.png').convert_alpha()
ptero_img = pygame.image.load('ptero.png').convert_alpha()
eagle_img = pygame.image.load('eagle.png').convert_alpha()
# player
crosshair_img = pygame.image.load('crosshair.png').convert_alpha()

# create enemy types
# wolf_enemy = enemy.Enemy(100, 100, wolf_img, 0.2)
bat_enemy = enemy.Enemy(-100, 100, bat_img, 0.2, "flyer_right", game_score)
# bear_enemy = enemy.Enemy(700, 300, bear_img, 0.1)
# tiger_enemy = enemy.Enemy(800, 600, tiger_img, 0.4)
# gorilla_enemy = enemy.Enemy(900, 400, gorilla_img, 0.4)
# alligator_enemy = enemy.Enemy(500, 100, alligator_img, 0.2)
# rex_enemy = enemy.Enemy(1000, 150, rex_img, 0.2)
ptero_enemy = enemy.Enemy(-100, 300, ptero_img, 0.2, "flyer_right", game_score)
eagle_enemy = enemy.Enemy(1380, 200, eagle_img, 0.15, "flyer_left", game_score)

# create player
player = player.Player(crosshair_img, 0.1)

while True:
    screen.blit(level_1)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # draw the game
    # wolf_enemy.update(screen)
    bat_enemy.update(screen, dt, window_width)
    # bear_enemy.update(screen)
    # tiger_enemy.update(screen)
    # gorilla_enemy.update(screen)
    # alligator_enemy.update(screen)
    # rex_enemy.update(screen)
    ptero_enemy.update(screen, dt, window_width)
    eagle_enemy.update(screen, dt, window_width)
    game_score.draw(screen, window_height, window_width)

    player.update(screen)

    pygame.display.flip()

    dt = clock.tick(fps) / 1000