import pygame
pygame.font.init()
class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 30)
        self.text_surf = self.font.render('Score: ' + str(int(self.score)), True, (255, 255, 255))
        self.text_rect = self.text_surf.get_frect()

    def draw(self, screen, window_height, window_width):
        self.text_rect.bottomright = window_width - 5, window_height - 5
        screen.blit(self.text_surf, self.text_rect)

    def add_score(self, score):
        self.score += score
        self.text_surf = self.font.render('Score: ' + str(int(self.score)),True,(255, 255, 255))
        self.text_rect = self.text_surf.get_frect()

    def get_score(self):
        return self.score