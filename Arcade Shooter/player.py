import pygame
class Player:
    def __init__(self, crosshair_img, scale, sniper_img, sniper_scale, max_ammo):
        cwidth, cheight = crosshair_img.get_width(), crosshair_img.get_height()
        swidth, sheight = sniper_img.get_width(), sniper_img.get_height()
        self.image = pygame.transform.scale(crosshair_img, (int(cwidth * scale), int(cheight * scale)))
        self.rect = self.image.get_frect()
        self.sniper_image = pygame.transform.scale(sniper_img, (int(swidth * sniper_scale), int(sheight * sniper_scale)))
        self.sniper_rect = self.sniper_image.get_frect()
        self.max_ammo = max_ammo
        self.ammo = max_ammo

    def update(self, screen, screen_width, screen_height):
        screen.blit(self.image, self.rect)
        screen.blit(self.sniper_image, self.sniper_rect)
        mx, my = pygame.mouse.get_pos()
        self.rect.center = mx, my
        self.sniper_rect.center = screen_width - 75, screen_height -75
        self.shoot(screen)

    def shoot(self, screen):
        if pygame.mouse.get_just_pressed()[0] and self.ammo > 0:
            self.ammo -= 1
            screen.fill('White')