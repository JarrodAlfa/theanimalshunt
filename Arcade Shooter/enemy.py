import pygame, random

class Enemy:
    def __init__(self, image, scale, score, window_width, window_height, flip_direction, player):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_frect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = random.randint(window_width//2 - 150, window_width//2 + 150), window_height + 200

        self.score = score
        self.alive = True
        self.speedy = random.randint(200, 350)
        self.speedx = random.randint(-350, 350)
        self.inframe = False
        self.flip_direction = flip_direction
        self.player = player

        self.lastdeath = 0
        self.respawn_cooldown = random.randint(5, 8) * 1000

    def update(self, dt, screen, screen_width, screen_height):
        now = pygame.time.get_ticks()
        screen_rect = screen.get_frect()
        if self.alive:
            self.spawn(screen)
            self.rect.y -= self.speedy * dt
            self.rect.x += self.speedx * dt
            if screen_rect.contains(self.rect):
                self.inframe = True
            if self.inframe:
                self.movement(screen_width, screen_height)
            if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                if self.player.ammo > 0:
                    self.player.ammo -= 1
                    screen.fill((255, 255, 255))
                    self.lastdeath = now
                    self.alive = False
        else:
            if now - self.lastdeath > self.respawn_cooldown:
                self.respawn(screen_width, screen_height)


    def respawn(self, window_width, window_height):
        self.rect.center = random.randint(window_width//2 - 150, window_width//2 + 150), window_height + 200
        self.speedy = random.randint(200, 350)
        self.speedx = random.randint(-350, 350)
        self.inframe = False
        self.alive = True


    def spawn(self, screen):
        screen.blit(self.image, self.rect)

    def movement(self, screen_width, screen_height):
        if self.rect.right > screen_width:
            self.speedx = -self.speedx
            if self.flip_direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip_direction = "left"
        if self.rect.left < 0:
            self.speedx = -self.speedx
            if self.flip_direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip_direction = "right"
        if self.rect.top < 0:
            self.speedy = -self.speedy
        if self.rect.bottom > screen_height:
            self.speedy = -self.speedy
