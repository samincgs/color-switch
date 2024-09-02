import pygame
import random

class Shape:
    def __init__(self, s_type, color, size, pos, speed):
        
        self.type = s_type
        self.size = size
        self.color = color
        self.pos = list(pos)
        self.speed = speed
        self.radius = random.randint(20, 30)
            
    def update(self):
        # self.pos[0] += random.randint(1, 3)
        self.pos[1] += self.speed
    
    def render(self, surf):
        if self.type == 'rectangle':
            rect = pygame.Rect(*self.pos, *self.size)
            pygame.draw.rect(surf, self.color, rect, 4)
        if self.type == 'circle':
            pygame.draw.circle(surf, self.color, self.pos, self.radius, 4)
            
        # TODO add triangle
            
            
            
    
    
    