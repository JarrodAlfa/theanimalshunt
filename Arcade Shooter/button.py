import pygame
pygame.font.init()
class Button:
    def __init__(self, x ,y, text, size):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont('Arial', size)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_frect()
        self.text_rect.center = (self.x, self.y)

    def draw(self, screen):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.text_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_just_pressed()[0] == 1:
                action = True

        screen.blit(self.text_surf, self.text_rect)

        return action

    def draw_nouse(self, screen):
        screen.blit(self.text_surf, self.text_rect)
