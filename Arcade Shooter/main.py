import pygame, sys
import enemy, player, score, button

# general setup
pygame.init()
pygame.mixer.init()
window_width, window_height = 1280, 720
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
fps = 60
dt = 0
game_score = score.Score()
game_state = 'game'

pygame.display.set_caption('Arcade Shooter')
pygame.display.set_icon(pygame.image.load('logo.png').convert_alpha())

# import images
start_screen = pygame.image.load('startscreen.jpg').convert()
start_screen = pygame.transform.scale(start_screen, (window_width, window_height))
quit_button = button.Button(100, 200, "QUIT")

#levels
level_1 = pygame.image.load('level1.jpg').convert()
level_1 = pygame.transform.scale(level_1, (window_width, window_height))

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
sniper_sound = pygame.mixer.Sound('sniper_geluid.mp3')
sniper_sound.set_volume(0.5)
reload_sound = pygame.mixer.Sound('reload.mp3')
reload_sound.set_volume(0.5)
player = player.Player(crosshair_img, 0.1, sniper_img, 0.3, 5, sniper_sound, reload_sound)

# create enemy types
bat_enemy = enemy.Enemy(bat_img, 0.2, game_score, window_width, window_height, 'right', player, "flyer")
ptero_enemy = enemy.Enemy(ptero_img, 0.2, game_score, window_width, window_height, 'right', player, "flyer")
eagle_enemy = enemy.Enemy(eagle_img, 0.15, game_score, window_width, window_height, 'left', player, "flyer")
wolf_enemy = enemy.Enemy(wolf_img, 0.15, game_score, window_width, window_height, 'left', player, "walker")
gorilla_enemy = enemy.Enemy(gorilla_img, 0.5, game_score, window_width, window_height, 'right', player, "walker")

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 7:
                player.reload()
    # draw the game
    if game_state == 'start_screen':
        screen.blit(start_screen)
        quit_button.draw(screen)
        pygame.display.flip()
    if game_state == 'game':
        screen.blit(level_1)
        #draw all enemies
        bat_enemy.update(dt,screen, window_width, window_height)
        ptero_enemy.update(dt,screen, window_width, window_height)
        eagle_enemy.update(dt,screen, window_width, window_height)
        wolf_enemy.update(dt,screen, window_width, window_height)
        gorilla_enemy.update(dt,screen, window_width, window_height)

        #draw gui
        player.update(screen, window_width, window_height)
        game_score.draw(screen, window_height, window_width)

        pygame.display.flip()
        dt = clock.tick(fps) / 1000