import pygame
pygame.font.init()
class Button:
    def __init__(self, x ,y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont('Arial', 100)

    def draw(self, screen):
        button_rect = pygame.FRect(self.x, self.y, 350, 100)
        pygame.draw.rect(screen, (144, 144, 144), button_rect, 0, 4)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_frect(center=button_rect.center)

        screen.blit(text_surf, text_rect)
