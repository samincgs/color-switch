import pygame
import sys
from scripts.color_board import ColorBoard
from scripts.shape import Shape
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Color Switch')
        self.display = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        
        self.color_board = ColorBoard((self.display.get_width(), 80), (0, 520))
        self.shape_list = []
        
        self.score = 0
        
        
    def run(self):
        
        while True:
            
            self.display.fill((0, 0, 0)) # TODO maybe add a background
            
            if not self.shape_list:
                shape_type = random.choice(['rectangle', 'circle', 'triangle'])
                shape_color = random.choice(['Red', 'Blue', 'Green', 'Yellow'])
                shape_size = (random.randint(42, 54), random.randint(42, 54)) # TODO change to make it look better
                shape_pos =  [random.randint(shape_size[0], self.display.get_width() - shape_size[1]), 0]
                shape_speed = random.uniform(4, 6)
                self.shape_list.append(Shape(shape_type, shape_color, shape_size,shape_pos, shape_speed))
            
            for shape in self.shape_list:
                shape.update()
                shape.render(self.display)
                
                # if the falling shapes color and the color of the board matches
                if shape.color == self.color_board.color  and not shape.counted:
                    # collision detection between falling shapes and color board at the bottom
                    if shape.displayed_rect.bottom >= self.color_board.pos[1] and shape.displayed_rect.top <= self.color_board.pos[1]:
                        # increment the score by 100
                        self.score += 100
                        shape.counted = True
                
                # shape removal to make sure shape_list isnt wasting memory
                if shape.pos[1] - shape.size[1] >= self.display.get_height() - self.color_board.size[1]:
                    self.shape_list.remove(shape)
                
            self.color_board.render(self.display)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    # if event.key == pygame.K_SPACE:
                    #     self.color_board.change_color()
                    if event.key == pygame.K_RIGHT:
                        self.color_board.change_color_right()
                    if event.key == pygame.K_LEFT:
                        self.color_board.change_color_left()
                    
                    
            pygame.display.update()
            self.clock.tick(60)
            
            
if __name__ == '__main__':
    Game().run()

