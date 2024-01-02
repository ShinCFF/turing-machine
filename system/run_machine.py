import pygame
import config.scr as scr
from system.machine import Turing
from system.character import Tape
from config.text import accept, reject, Font
from config.colors import GREY, WHITE, BLACK
pygame.init()

screen = pygame.display.set_mode((scr.width, scr.height))
pygame.display.set_icon(scr.cap_img)
pygame.display.set_caption("Turing Machine Demo")

#input 
input_rect = pygame.Rect(scr.input_x, scr.input_y, scr.input_width, scr.input_height)
color_active = pygame.Color(BLACK)
color_passive = pygame.Color(GREY)
color = color_passive
active = False

user_text = ''
run_rect = scr.run_img.get_rect(center = (scr.run_x, scr.run_y))
run_button = True   
running = True
clock = pygame.time.Clock()
FPS = 6

def get(text):
    lst = []
    cur = int((scr.tape_num - len(text)) / 2)
    for i in range(0, len(text)):
        if text[i] == '_':
            lst.append([' ', cur + i])
        else:
            lst.append([text[i], cur + i])
    return lst
        
def outputLst(a):
    for i in range(0, len(a)):
        Tape().write(screen, a[i][0], a[i][1])

lst = []
all_step = []
pos = ok = 0

def render(word):
    if word == 'Accept':
        screen.blit(accept, (500, 400))
    elif word == 'Reject':
        screen.blit(reject, (500, 400))
    run_button = 1

word_state = ''
last_word = ''
auto_run = 0
while running: 
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else: 
                active = False
            if run_rect.collidepoint(event.pos):
                run_button = 1 - run_button
                if run_button == 0 and len(last_word) > 0:
                    auto_run = 1
                print(run_button)
            if scr.next_rect.collidepoint(event.pos) and len(all_step) > 0:
                lst = all_step[0][0]
                pos = all_step[0][1]
                all_step.remove(all_step[0])
            if scr.reset_rect.collidepoint(event.pos) and len(last_word) > 0:
                all_step = []
                lst = get(last_word)
                ans = Turing.run(last_word)
                word_state = ans[-1]
                for i in range(len(ans)-1):
                    tmp = get(ans[i][0][:len(ans[i][0])-1])
                    all_step.append([tmp, tmp[0][1] + ans[i][1]])
                lst = all_step[0][0]
                pos = all_step[0][1]
                all_step.remove(all_step[0])

        if event.type == pygame.KEYDOWN and active == True:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                all_step = []
                last_word = user_text
                lst = get(user_text)
                print(lst)
                ans = Turing.run(user_text)
                word_state = ans[-1]
                for i in range(len(ans)-1):
                    tmp = get(ans[i][0][:len(ans[i][0])-1])
                    all_step.append([tmp, tmp[0][1] + ans[i][1]])
                user_text = ''
                active = False
                lst = all_step[0][0]
                pos = all_step[0][1]
                all_step.remove(all_step[0])
            else:
                user_text += event.unicode

    Tape().draw(screen)   
    
    if auto_run == 1:
        if len(all_step) > 0:
            lst = all_step[0][0]
            pos = all_step[0][1]
            all_step.remove(all_step[0])
        else:
            run_button = 1
            auto_run = 0

    print(lst)

    if len(all_step) == 0:
        render(word_state)
    outputLst(lst) 

    Tape().drawPointer(screen, pos)
    screen.blit(scr.next_img, scr.next_rect)
    if run_button:
        screen.blit(scr.run_img, scr.run_rect)
        auto_run = 0
    else:
        screen.blit(scr.pause_img, scr.run_rect)
    screen.blit(scr.reset_img, scr.reset_rect)
    if active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(screen, color, input_rect, 5)
    text_surface = Font[0].render(user_text, True, BLACK)
    screen.blit(text_surface, (scr.input_x + 20, scr.input_y + 20))  
    pygame.display.update()
    clock.tick(FPS)