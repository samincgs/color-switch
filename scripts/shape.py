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
        
        self.counted = False
            
    def update(self):
        # self.pos[0] += random.randint(1, 3)
        self.pos[1] += self.speed
    
    def render(self, surf):
        if self.type == 'rectangle':
            rect = pygame.Rect(*self.pos, *self.size)
            self.displayed_rect = pygame.draw.rect(surf, self.color, rect)
        if self.type == 'circle':
            self.displayed_rect = pygame.draw.circle(surf, self.color, self.pos, self.radius)
        if self.type == 'triangle':
            point1 = (self.pos[0], self.pos[1] - self.size[1] // 2)  # Top vertex
            point2 = (self.pos[0] - self.size[0] // 2, self.pos[1] + self.size[1] // 2)  # Bottom left vertex
            point3 = (self.pos[0] + self.size[0] // 2, self.pos[1] + self.size[1] // 2)  # Bottom right vertex
            self.displayed_rect = pygame.draw.polygon(surf, self.color, [point1, point2, point3])
            
    
            
            
            
    
    
    