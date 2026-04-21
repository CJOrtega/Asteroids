import random

import pygame

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        x = self.position[0]
        y = self.position[1]
        angle = random.uniform(20, 50)
        rotate1 = self.velocity.rotate(angle)
        rotate2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(x, y, new_radius)
        asteroid2 = Asteroid(x, y, new_radius)
        asteroid1.velocity = rotate1 * 1.2
        asteroid2.velocity = rotate2 * 1.2

