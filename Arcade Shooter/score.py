import pygame
pygame.font.init()
class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 30)
        self.text_surf = self.font.render('Score: ' + str(int(self.score)), True, (255, 255, 255))

    def draw(self, screen, window_height, window_width):
        screen.blit(self.text_surf, (window_width - 150, window_height - 50))

    def add_score(self, score):
        self.score += score
        self.text_surf = self.font.render('Score: ' + str(int(self.score)),True,(255, 255, 255))