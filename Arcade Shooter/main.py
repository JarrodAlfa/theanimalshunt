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
sniper_img = pygame.image.load('sniper.png').convert_alpha()

#player
player = player.Player(crosshair_img, 0.1, sniper_img, 0.3, 5)
# create enemy types
bat_enemy = enemy.Enemy(bat_img, 0.2, game_score, window_width, window_height, 'right', player)
ptero_enemy = enemy.Enemy(ptero_img, 0.2, game_score, window_width, window_height, 'right', player)
eagle_enemy = enemy.Enemy(eagle_img, 0.15, game_score, window_width, window_height, 'left', player)

while True:
    screen.blit(level_1)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # draw the game
    bat_enemy.update(dt,screen, window_width, window_height)
    ptero_enemy.update(dt,screen, window_width, window_height)
    eagle_enemy.update(dt,screen, window_width, window_height)
    game_score.draw(screen, window_height, window_width)

    player.update(screen, window_width, window_height)

    pygame.display.flip()

    dt = clock.tick(fps) / 1000