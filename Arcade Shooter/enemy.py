import pygame, random
class Enemy:
    def __init__(self, image, scale, score, window_width, window_height, flip_direction, player, type):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_frect()
        self.mask = pygame.mask.from_surface(self.image)

        self.score = score
        self.alive = True
        self.speedy = random.randint(200, 350)
        self.speedx = random.randint(-350, 350)
        self.inframe = False
        self.flip_direction = flip_direction
        self.player = player
        self.lastshot = pygame.time.get_ticks()
        self.type = type
        self.walker_side = ""
        self.walker_speed = random.randint(100, 250)

        if self.type == "flyer":
            self.rect.center = random.randint(window_width // 2 - 150, window_width // 2 + 150), window_height + 200
        elif self.type == "walker":
            side = random.choice(["left", "right"])
            pos_y = window_height - 70
            if side == "left":
                x_pos = -150
                self.walker_side = "left"
                self.flip_direction = 'right'
            else:
                x_pos = window_width + 150
                self.walker_side = "right"
                self.flip_direction = 'left'
            self.rect.center = x_pos, pos_y

        self.lastdeath = 0
        self.respawn_cooldown = random.randint(5, 8) * 1000

    def update(self, dt, screen, screen_width, screen_height):
        if self.type == "flyer":
            self.flyer_logic(dt, screen, screen_width, screen_height)
        if self.type == "walker":
            self.walker_logic(dt, screen, screen_width, screen_height)


    def respawn(self, window_width, window_height):
        if self.type == "flyer":
            self.rect.center = random.randint(window_width // 2 - 150, window_width // 2 + 150), window_height + 200
        elif self.type == "walker":
            side = random.choice(["left", "right"])
            pos_y = window_height - 70
            if side == "left":
                x_pos = -150
                self.walker_side = "left"
            else:
                x_pos = window_width + 150
                self.walker_side = "right"
            self.rect.center = x_pos, pos_y
        self.speedy = random.randint(200, 350)
        self.speedx = random.randint(-350, 350)
        self.inframe = False
        self.alive = True


    def spawn(self, screen):
        screen.blit(self.image, self.rect)

    def movement(self, screen_width, screen_height):
        self.lefty(screen_width)
        self.righty()
        if self.rect.top < 0:
            self.speedy = -self.speedy
        if self.rect.bottom > screen_height:
            self.speedy = -self.speedy

    def lefty(self, screen_width):
        if self.rect.right > screen_width:
            if self.type == "flyer":
                self.speedx = -self.speedx
            if self.flip_direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip_direction = "left"
    def righty(self):
        if self.rect.left < 0:
            if self.type == "flyer":
                self.speedx = -self.speedx
            if self.flip_direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip_direction = "right"

    def walker_logic(self, dt, screen, screen_width, screen_height):
        now = pygame.time.get_ticks()
        screen_rect = screen.get_frect()
        if self.alive:
            self.spawn(screen)
            if self.walker_side == "left":
                self.rect.x += self.walker_speed * dt
            else:
                self.rect.x -= self.walker_speed * dt
            if screen_rect.contains(self.rect):
                self.inframe = True
            if self.inframe:
                self.lefty(screen_width)
                self.righty()
                if self.rect.left < 0:
                    self.walker_side = "left"
                    self.rect.left = 0
                if self.rect.right > screen_width:
                    self.walker_side = "right"
                    self.rect.right = screen_width
            self.shoot_logic()
        else:
            if now - self.lastdeath > self.respawn_cooldown:
                self.respawn(screen_width, screen_height)
    def flyer_logic(self,dt, screen, screen_width, screen_height):
        now = pygame.time.get_ticks()
        screen_rect = screen.get_frect()
        if self.alive:
            self.spawn(screen)
            self.rect.y -= self.speedy * dt
            self.rect.x += self.speedx * dt
            if not self.inframe:
                self.lefty(screen_width)
                self.righty()
            if screen_rect.contains(self.rect):
                self.inframe = True
            if self.inframe:
                self.movement(screen_width, screen_height)
            self.shoot_logic()
        else:
            if now - self.lastdeath > self.respawn_cooldown:
                self.respawn(screen_width, screen_height)

    def shoot_logic(self):
        now = pygame.time.get_ticks()
        if not self.player.reloading:
            if pygame.mouse.get_just_pressed()[0]:
                if now - self.lastshot > 300:
                    if self.rect.collidepoint(pygame.mouse.get_pos()) and self.player.ammo > 0:
                        self.lastdeath = now
                        self.lastshot = now
                        self.score.add_score(random.choice([1000, 1250, 1500, 2000]))
                        self.alive = False