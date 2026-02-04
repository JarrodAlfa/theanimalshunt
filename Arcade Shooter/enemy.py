import pygame, random
class Enemy:
    def __init__(self, x, y, image, scale, enemy_type):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_frect()
        self.rect.center = (x, y)
        self.alive = True
        self.mask = pygame.mask.from_surface(self.image)
        self.type = enemy_type
        self.lastdeath = 0
        self.cooldown = random.randint(10, 30) * 1000

    def update(self, screen, dt, windowwidth):
        mouse_pos = pygame.mouse.get_pos()

        if self.alive and self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_just_pressed()[0] == 1:
                self.alive = False
                self.lastdeath = pygame.time.get_ticks()

        self.movement(dt, windowwidth)

        if self.alive:
            screen.blit(self.image, self.rect)

    def movement(self, dt, windowwidth):
        now = pygame.time.get_ticks()

        if self.type == "flyer_right":
            if self.alive:
                self.rect.x += 100 * dt
                if self.rect.x > windowwidth + 100:
                    self.kill()
            else:
                if now - self.lastdeath >= self.cooldown:
                    self.respawn(-100)

        elif self.type == "flyer_left":
            if self.alive:
                self.rect.x -= 100 * dt
                if self.rect.x < -100:
                    self.kill()
            else:
                if now - self.lastdeath >= self.cooldown:
                    self.respawn(windowwidth + 100)

    def kill(self):
        self.alive = False
        self.lastdeath = pygame.time.get_ticks()

    def respawn(self, x):
        self.rect.x = x
        self.alive = True