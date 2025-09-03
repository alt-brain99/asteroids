import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        r = self.radius
        pos = pygame.Vector2(self.position) 
        vel = pygame.Vector2(self.velocity)

        self.kill()
        if r <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        v1 = vel.rotate(angle) * 1.2
        v2 = vel.rotate(-angle) * 1.2
        new_r = r - ASTEROID_MIN_RADIUS

        a1 = Asteroid(pos.x, pos.y, new_r)
        a1.velocity = v1
        a2 = Asteroid(pos.x, pos.y, new_r)
        a2.velocity = v2
