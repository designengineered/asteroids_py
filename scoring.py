import pygame
from constants import *


class Scoring:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def reset(self):
        self.score = 0

    def add_score(self, asteroid_radius):
        if asteroid_radius == ASTEROID_MIN_RADIUS:
            self.score += 50  # Small asteroid
        elif asteroid_radius == ASTEROID_MIN_RADIUS * 2:
            self.score += 35  # Medium asteroid
        else:
            self.score += 25  # Large asteroid

    def draw(self, screen):
        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def get_score(self):
        return self.score
