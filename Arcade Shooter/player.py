import pygame
class Player:
    def __init__(self, image, scale):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_frect()

    def update(self, screen):
        self.rect.center = pygame.mouse.get_pos()

        screen.blit(self.image, self.rect)