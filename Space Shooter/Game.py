import sys
import math
from random import randint, uniform

import pygame
from pygame import sprite
from pygame.locals import *
from os.path import join

class Player(sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.original_image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_frect(center = (SCREENWIDTH / 2, SCREENHEIGHT / 2))
        self.dir = pygame.math.Vector2()
        self.speed = 300
        self.last_angle = None
        self.lives = 3

        #Cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

        #Mask
        self.mask = pygame.mask.from_surface(self.image)

    def damage(self):
        self.lives -= 1
        if self.lives <= 0:
            global game_state, final_score
            final_score = (pygame.time.get_ticks() - start_time) // 100
            game_state = 'game_over'

    def mouse_look(self):
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - self.rect.centerx, my - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90

        angle = round(angle, 2)

        if angle != self.last_angle:
            self.image = pygame.transform.rotate(self.original_image, angle)
            self.rect = self.image.get_frect(center=self.rect.center)
            self.last_angle = angle

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self , dt):
        self.mouse_look()

        keys = pygame.key.get_pressed()
        self.dir.x = int(keys[K_d]) - int(keys[K_a])
        self.dir.y = int(keys[K_s]) - int(keys[K_w])
        self.dir = self.dir.normalize() if self.dir else self.dir
        self.rect.center += self.dir * self.speed * dt
        self.rect.clamp_ip(DISPLAYSURF_RECT)

        recent_keys = pygame.key.get_pressed()
        recent_mouse = pygame.mouse.get_pressed()
        if recent_keys[K_SPACE] and self.can_shoot or recent_mouse[0] and self.can_shoot:
            radians = math.radians(self.last_angle + 90)
            direction = pygame.math.Vector2(math.cos(radians), -math.sin(radians))

            Laser(laser_surf, self.rect.center, direction, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()

        self.laser_timer()

class Star(sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = pygame.transform.rotate(surf, randint(0, 360))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_frect(center = (randint(0, SCREENWIDTH), randint(0, SCREENHEIGHT)))

class Laser(sprite.Sprite):
    def __init__(self, surf, pos, direction, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.direction = direction.normalize()
        self.speed = 500
        angle = math.degrees(math.atan2(-self.direction.y, self.direction.x)) - 90
        self.image = pygame.transform.rotate(surf, angle)

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if self.rect.bottom < 0 or self.rect.top > SCREENHEIGHT or self.rect.right < 0 or self.rect.left > SCREENWIDTH:
            self.kill()

class Meteor(sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.original_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(400, 500)
        self.rotation_speed = randint(40, 80)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time > self.lifetime:
            self.kill()
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)
        self.rect = self.image.get_frect(center = self.rect.center)

class AnimatedExplosion(sprite.Sprite):
    def __init__(self, frames, pos ,groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = pos)
        explosion_sound.play()

    def update(self, dt):
        self.frame_index += 20 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

def draw_start_menu():
    DISPLAYSURF.fill('#3a2e3f')
    title = font.render('SPACE SHOT', True, (240, 240, 240))
    start_button = font.render('S - start', True, (240, 240, 240))
    DISPLAYSURF.blit(title, (SCREENWIDTH / 2 - title.get_width() / 2, SCREENHEIGHT / 2 - title.get_height() / 2))
    DISPLAYSURF.blit(start_button, (SCREENWIDTH / 2 - start_button.get_width() / 2, SCREENHEIGHT / 2 + start_button.get_height() / 2))
    pygame.display.update()

def draw_game_over_screen():
    DISPLAYSURF.fill('#3a2e3f')
    game_over = font.render('GAME OVER', True, (240, 240, 240))
    score = font.render(str(final_score), True, (240, 240, 240))
    quit_game = font.render('Q - quit', True, (240, 240, 240))
    restart = font.render('R - restart', True, (240, 240, 240))
    DISPLAYSURF.blit(game_over, (SCREENWIDTH / 2 - game_over.get_width() / 2, SCREENHEIGHT / 2 - game_over.get_height() / 3))
    DISPLAYSURF.blit(quit_game, (SCREENWIDTH / 2 - quit_game.get_width() / 2, SCREENHEIGHT / 1.9 + quit_game.get_height()))
    DISPLAYSURF.blit(restart, (SCREENWIDTH / 2 - restart.get_width() / 2, SCREENHEIGHT / 2 + restart.get_height() / 2))
    DISPLAYSURF.blit(score, (SCREENWIDTH / 2 - score.get_width() / 2, SCREENHEIGHT / 1.9 / 2 + score.get_height()))
    pygame.display.update()

def collisions():
    if sprite.spritecollide(player, meteor_sprites, True, sprite.collide_mask):
        AnimatedExplosion(explosion_frames, player.rect.midtop, all_sprites)
        player.damage()

    for laser in laser_sprites:
        collided_sprites = sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()
            AnimatedExplosion(explosion_frames, laser.rect.midtop, all_sprites)

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 100
    text_surf = font.render(str(current_time), True, (240, 240, 240))
    text_rect = text_surf.get_frect(midbottom = (SCREENWIDTH / 2, SCREENHEIGHT - 50))
    DISPLAYSURF.blit(text_surf, text_rect)
    pygame.draw.rect(DISPLAYSURF, (240,240,240), text_rect.inflate(20,10).move(0,-8), 5, 10)

def display_hp():
    hp_surf = font.render('Lives:' + str(player.lives), True, (240, 240, 240))
    hp_rect = hp_surf.get_frect(topleft=(20, 20))
    DISPLAYSURF.blit(hp_surf, hp_rect)
    pygame.draw.rect(DISPLAYSURF, (240,240,240), hp_rect.inflate(20,10).move(0,-8), 5, 10)

pygame.init()
clock = pygame.time.Clock()

#Display
SCREENWIDTH = 1280
SCREENHEIGHT = 720
DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
DISPLAYSURF_RECT = DISPLAYSURF.get_frect()
pygame.display.toggle_fullscreen()
pygame.display.set_caption('Space shooter')

#Import
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 40)
explosion_frames = [pygame.image.load(join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]

laser_sound = pygame.mixer.Sound(join('audio', 'laser.wav'))
laser_sound.set_volume(0.5)

explosion_sound = pygame.mixer.Sound(join('audio', 'explosion.wav'))
explosion_sound.set_volume(0.5)

damage_sound = pygame.mixer.Sound(join('audio', 'damage.ogg'))
damage_sound.set_volume(0.5)

game_music = pygame.mixer.Sound(join('audio', 'game_music.wav'))
game_music.set_volume(0.3)
game_music.play(loops = -1)

#Sprites
all_sprites = sprite.Group()
meteor_sprites = sprite.Group()
laser_sprites = sprite.Group()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

#Custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 300)
game_state = 'start_menu'
final_score = 0
start_time = 0

#Game loop begins
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_event:
            x, y = randint(0, SCREENWIDTH), randint(-200, -100)
            Meteor(meteor_surf, (x,y), (all_sprites, meteor_sprites))
    if game_state == 'start_menu':
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[K_s]:
            start_time = pygame.time.get_ticks()
            game_state = 'game'

    if game_state == 'game':
        dt = clock.tick() / 1000
        # Update
        all_sprites.update(dt)
        collisions()

        # Draw the game
        DISPLAYSURF.fill('#3a2e3f')
        display_score()
        display_hp()
        all_sprites.draw(DISPLAYSURF)

        pygame.display.update()

    if game_state == 'game_over':
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[K_r]:
            start_time = pygame.time.get_ticks()
            player.lives = 3
            all_sprites.empty()
            meteor_sprites.empty()
            laser_sprites.empty()
            for i in range(20):
                Star(all_sprites, star_surf)
            all_sprites.add(player)
            game_state = 'game'
        elif keys[K_q]:
            pygame.quit()
            sys.exit()
