import pygame
from config.colors import RED, BLACK
pygame.font.init()

Font = [pygame.font.Font('freesansbold.ttf', 60), pygame.font.Font('freesansbold.ttf', 90)]
accept = Font[1].render('Palindrome', True, RED)
reject = Font[1].render('Not Palindrome', True, RED)
Text = []
Text.append(Font[0].render('', True, BLACK))


for i in range(33,128):
    Text.append(Font[0].render(chr(i), True, BLACK))