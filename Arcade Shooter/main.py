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
game_state = 'start_screen'

pygame.display.set_caption('Arcade Shooter')
pygame.display.set_icon(pygame.image.load('logo.png').convert_alpha())

music = pygame.mixer.Sound('lassolady.ogg')
music.set_volume(0.3)
music.play(loops=-1)

# import images
start_screen = pygame.image.load('startscreen.jpg').convert()
start_screen = pygame.transform.scale(start_screen, (window_width, window_height))
quit_button = button.Button(380, window_height-100, "QUIT", 100)
credits_button = button.Button(380, window_height-300, "CREDITS", 100)
start_button = button.Button(380, window_height-500, "START", 100)
credit_text1 = button.Button(380, window_height-600, "credits:", 30)
credit_text2 = button.Button(380, window_height-500, "Mohammad, music, sfx, level design",30)
credit_text3 = button.Button(380, window_height-400, "Safa, Graphic design and level design",30)
credit_text4 = button.Button(380, window_height-300, "Jarrod, programming and level design", 30)
credit_text5 = button.Button(380, window_height-200, "published by The Animals",30)
credits_back = button.Button(100, 50, "BACK", 50)
#levels
level_1 = pygame.image.load('level1.jpg').convert()
level_1 = pygame.transform.scale(level_1, (window_width, window_height))
level_2 = pygame.image.load('sky.png').convert()
level_2 = pygame.transform.scale(level_2, (window_width, window_height))
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
woolly_rhino = pygame.image.load('woollyrhino.png').convert_alpha()
argy_img = pygame.image.load('argy.png').convert_alpha()

# player
crosshair_img = pygame.image.load('crosshair.png').convert_alpha()
sniper_img = pygame.image.load('sniper.png').convert_alpha()
sniper_sound = pygame.mixer.Sound('sniper_geluid.mp3')
sniper_sound.set_volume(0.5)
reload_sound = pygame.mixer.Sound('reload.mp3')
reload_sound.set_volume(0.5)
player = player.Player(crosshair_img, 0.1, sniper_img, 0.3, 5, sniper_sound, reload_sound)

# create enemy types
bat_enemy = enemy.Enemy(bat_img, 0.175, game_score, window_width, window_height, 'right', player, "flyer")
ptero_enemy = enemy.Enemy(ptero_img, 0.2, game_score, window_width, window_height, 'right', player, "flyer")
eagle_enemy = enemy.Enemy(eagle_img, 0.1, game_score, window_width, window_height, 'left', player, "flyer")
wolf_enemy = enemy.Enemy(wolf_img, 0.15, game_score, window_width, window_height, 'left', player, "walker")
gorilla_enemy = enemy.Enemy(gorilla_img, 0.5, game_score, window_width, window_height, 'right', player, "walker")
alligator_enemy = enemy.Enemy(alligator_img, 0.17, game_score, window_width, window_height, 'left', player, "walker")
tiger_enemy = enemy.Enemy(tiger_img, 0.5, game_score, window_width, window_height, 'right', player, "walker")
bear_enemy = enemy.Enemy(bear_img, 0.1, game_score, window_width, window_height, 'left', player, "walker")
rex_enemy = enemy.Enemy(rex_img, 0.25, game_score, window_width, window_height, 'left', player, "walker")
woolly_rhino_enemy = enemy.Enemy(woolly_rhino, 0.5, game_score, window_width, window_height, 'left', player, "walker")
argy_enemy = enemy.Enemy(argy_img, 0.2, game_score, window_width, window_height, 'left', player, "flyer")

while True:
    # event loop
    dt = clock.tick(fps) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_just_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 7:
                player.reload()
    # draw the game
    if game_state == 'start_screen':
        screen.blit(start_screen)
        if quit_button.draw(screen):
            pygame.quit()
            sys.exit()
        if credits_button.draw(screen):
            game_state = "credit_screen"
        if start_button.draw(screen):
            game_state = 'game'
            pygame.event.clear(pygame.MOUSEBUTTONDOWN)
        pygame.display.flip()

    if game_state == 'credit_screen':
        screen.blit(start_screen)
        credit_text1.draw_nouse(screen)
        credit_text2.draw_nouse(screen)
        credit_text3.draw_nouse(screen)
        credit_text4.draw_nouse(screen)
        credit_text5.draw_nouse(screen)
        if credits_back.draw(screen):
            game_state = 'start_screen'
        pygame.display.flip()

    score = game_score.get_score()
    if score <= 50000:
        if game_state == 'game':
            screen.blit(level_1)
            #draw all enemies
            enemies = [bat_enemy, ptero_enemy, gorilla_enemy, alligator_enemy, tiger_enemy, rex_enemy]

            for e in enemies:
                e.update(dt, screen, window_width, window_height)

            #draw gui
            player.update(screen, window_width, window_height)
            game_score.draw(screen, window_height, window_width)

            pygame.display.flip()
    elif score >= 50000:
        screen.blit(level_2)
        enemies = [bat_enemy, eagle_enemy, wolf_enemy,
                       bear_enemy, woolly_rhino_enemy, argy_enemy]
        for e in enemies:
            e.update(dt, screen, window_width, window_height)

        player.update(screen, window_width, window_height)
        game_score.draw(screen, window_height, window_width)
        pygame.display.flip()