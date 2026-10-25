import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid (CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw (self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector_a = self.velocity.rotate(angle)
            vector_b =self.velocity.rotate(angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_r)
            asteroid_1.velocity = vector_a * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_r)
            asteroid_2.velocity = vector_b * 1.2
