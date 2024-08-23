import pygame
import random
import math
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)
        self.image = self.generate_asteroid_shape()
        self.rect = self.image.get_rect(center=(x, y))
    
    def generate_asteroid_shape(self):
        # Create a new surface with the size of the asteroid
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))  # Fill with transparent background

        # Center of the surface
        center = (self.radius, self.radius)
        
        # Generate the asteroid shape with some irregularities
        num_points = 8
        angle_step = 2 * math.pi / num_points
        points = []
        
        for i in range(num_points):
            angle = i * angle_step
            # Add some random variation to the radius
            r = self.radius + random.uniform(-self.radius * 0.2, self.radius * 0.2)
            x = center[0] + r * math.cos(angle)
            y = center[1] + r * math.sin(angle)
            points.append((x, y))

        # Draw the irregular circle shape
        pygame.draw.polygon(surface, (128, 128, 128), points)
        
        return surface

    def update(self, dt):
        self.position += self.velocity * dt
        # Update the position of the rect for rendering
        self.rect.center = (self.position.x, self.position.y)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2

        return asteroid1, asteroid2
