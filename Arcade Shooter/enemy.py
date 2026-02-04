import pygame, random

class Enemy:
    def __init__(self, image, scale, score, window_width, window_height, flip_direction):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_frect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = random.randint(window_width//2 - 250, window_width//2 + 250), window_height + 200

        self.score = score
        self.alive = True
        self.speedy = random.randint(200, 350)
        self.speedx = random.randint(-350, 350)
        self.inframe = False
        self.flip_direction = flip_direction

    def update(self, dt, screen, screen_width, screen_height):
        screen_rect = screen.get_frect()
        self.spawn(screen)
        self.rect.y -= self.speedy * dt
        self.rect.x += self.speedx * dt
        if screen_rect.contains(self.rect):
            self.inframe = True
        if self.inframe:
            self.movement(screen_width, screen_height)
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
