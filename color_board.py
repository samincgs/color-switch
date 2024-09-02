import pygame
import random

class ColorBoard:
    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.board = pygame.Surface((size))
        self.color_list = ['Red', 'Blue', 'Green', 'Yellow']
        self.color_index = random.randint(0, 2)
        self.color = self.color_list[self.color_index]
        
    def render(self, surf):
        self.board.fill(self.color)
        surf.blit(self.board, self.pos)
    
    def change_color_right(self):
        self.color_index = (self.color_index + 1) % len(self.color_list)
        self.color = self.color_list[self.color_index]
        
    def change_color_left(self):
        self.color_index = (self.color_index - 1) % len(self.color_list)
        self.color = self.color_list[self.color_index]