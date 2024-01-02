import pygame 
from config.colors import BLACK

width, height = 1500, 900
cell_size = 20

# initilize images
cap_img = pygame.image.load('images/alan-turing.png')
next_img = pygame.image.load('images/next.png')
run_img = pygame.image.load('images/fast-foward.png')
reset_img  = pygame.image.load('images/restart.png')
pause_img = pygame.image.load('images/pause.png')

# initilize tape
tape_x = 10
tape_y = 30
tape_width = 100
tape_height = 100
tape_num = 10
tape_color = BLACK

#initilize button 
next_x,next_y = 30 * cell_size, 38 * cell_size
run_x,run_y = 50 * cell_size, 38 * cell_size
reset_x,reset_y = 10 * cell_size, 38 * cell_size

#initilize input
input_x, input_y = 30,50
input_width, input_height = 500,100


next_rect = next_img.get_rect(center = (next_x, next_y))
reset_rect = reset_img.get_rect(center = (reset_x, reset_y))
run_rect = run_img.get_rect(center = (run_x, run_y))