import pygame
import config.scr as scr
from config.colors import YELLOW
from config.scr import cell_size
from config.text import Text

class Tape:
    def __init__(self):
        self.x = scr.tape_x
        self.y = scr.tape_y
        self.width = scr.tape_width
        self.height = scr.tape_height
        self.num = scr.tape_num
        self.color = scr.tape_color
        
    def write(self, screen, character, pos):
        rect_y = (self.y  - 1) * cell_size
        rect_x = (self.x - 1) * cell_size + pos * self.width - pos * 2
        if character != ' ':
            character_id = ord(character) - 32
        else:
            character_id = 0
        text_rect = Text[character_id].get_rect(center = (rect_x + self.width / 2 + 20, rect_y + self.height / 2 + 20))
        screen.blit(Text[character_id], text_rect)
        
    def draw(self, screen):
        for i in range(self.num):
            rect_y = self.y * cell_size
            rect_x = self.x * cell_size + i * self.width - i * 2
            pygame.draw.rect(screen, self.color, (rect_x, rect_y, self.width, self.height), 3)
            
    def drawPointer(self, screen, pos, Color = YELLOW):
        rect_y = (self.y  - 1) * cell_size
        rect_x = (self.x - 1) * cell_size + pos * self.width - pos * 2
        pygame.draw.rect(screen, Color, (rect_x, rect_y, self.width + 2 * cell_size, self.height + 2*cell_size), 3)
            
