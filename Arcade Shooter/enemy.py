import pygame
class Enemy:
    def __init__(self, x, y, image, scale, enemy_type):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_frect()
        self.rect.center = (x, y)
        self.alive = True
        self.mask = pygame.mask.from_surface(self.image)
        self.type = enemy_type

    def update(self, screen, dt, windowwidth):
        if not self.alive:
            return False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_just_pressed()[0] == 1:
                self.alive = False

        self.movement(dt, windowwidth)

        screen.blit(self.image, self.rect)
        return None

    def movement(self, dt, windowwidth):
        if self.type == "flyer_right":
            self.rect.x += 100 * dt
            if self.rect.x > windowwidth + 100:
                self.rect.x = windowwidth - windowwidth - 100
        if self.type == "flyer_left":
            self.rect.x += -100 * dt
            if self.rect.x < windowwidth - windowwidth - 100:
                self.rect.x = windowwidth + 100