import pygame
class Enemy:
    def __init__(self, x, y, image, scale):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_frect()
        self.rect.center = (x, y)
        self.alive = True

    def draw(self, screen):
        if not self.alive:
            return False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_just_pressed()[0] == 1:
                self.image.fill((255,255,255))
                self.alive = False

        screen.blit(self.image, self.rect)
        return None
