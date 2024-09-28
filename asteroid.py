import random

import pygame

from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def reset(self, x, y):
        super().reset(x, y)

    def update(self, dt):
        self.position += self.velocity * dt

    def get_score(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            return 50  # Small asteroid
        elif self.radius == ASTEROID_MIN_RADIUS * 2:
            return 35  # Medium asteroid
        else:
            return 25  # Large asteroid

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
