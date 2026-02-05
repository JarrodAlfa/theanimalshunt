import pygame
pygame.mixer.init()
class Player:
    def __init__(self, crosshair_img, scale, sniper_img, sniper_scale, max_ammo, sniper_sound):
        cwidth, cheight = crosshair_img.get_width(), crosshair_img.get_height()
        swidth, sheight = sniper_img.get_width(), sniper_img.get_height()
        self.image = pygame.transform.scale(crosshair_img, (int(cwidth * scale), int(cheight * scale)))
        self.rect = self.image.get_frect()
        self.sniper_image = pygame.transform.scale(sniper_img, (int(swidth * sniper_scale), int(sheight * sniper_scale)))
        self.sniper_rect = self.sniper_image.get_frect()
        self.max_ammo = max_ammo
        self.ammo = max_ammo
        self.sniper_sound = sniper_sound
        self.lastshot = pygame.time.get_ticks()
        self.shootcooldown = 300
        self.reload_start_time = 0
        self.reload_time = 2000
        self.reloading = False

    def update(self, screen, screen_width, screen_height):
        now = pygame.time.get_ticks()
        if self.reloading:
            if now - self.reload_start_time >= self.reload_time:
                self.ammo = self.max_ammo
                self.reloading = False
        screen.blit(self.image, self.rect)
        screen.blit(self.sniper_image, self.sniper_rect)
        mx, my = pygame.mouse.get_pos()
        self.rect.center = mx, my
        self.sniper_rect.center = screen_width - 75, screen_height -75
        self.shoot(screen)

    def shoot(self, screen):
        if self.reloading:
            return
        now = pygame.time.get_ticks()
        if pygame.mouse.get_just_pressed()[0] and self.ammo > 0:
            if now - self.lastshot > self.shootcooldown:
                self.sniper_sound.play()
                self.ammo -= 1
                self.lastshot = now
                screen.fill('White')

    def reload(self):
        if self.ammo < self.max_ammo and not self.reloading:
            self.reloading = True
            self.reload_start_time = pygame.time.get_ticks()