import pygame
from pygame.locals import *
import time
from fer import FER  



def quit(loop_variable):
    for event in pygame.event.get():
        if event.type == QUIT:
            loop_variable = False
        elif event.type == KEYDOWN and event.key == K_q:
            loop_variable = False            
    return loop_variable



# For text box display and taking values
def text1():
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100,100,140,32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_q:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        done = True
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        if done == False:    
            # screen.fill(bg_color)
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            clock.tick(30)
    
    return text

if __name__ == "__main__":
    pygame.init()
    width=59
    height=451
    pygame.display.set_caption("Hope")


    screen = pygame.display.set_mode((1200,600) )#flags = pygame.FULLSCREEN)
    
    bg_color = pygame.Color(255, 129, 170)    
    screen.fill(bg_color)    
    pygame.font.init()

    # For loop variable
    flag = True  
    
    img_directory = "E://Projects//Pygame experiment//images_without_bg//"
    ball = pygame.image.load(img_directory + "ball.png")
    screen.blit(ball,ball.get_rect())

    text = text1()
    print("Text received: ", text)

    # screen.fill(bg_color)    
    pygame.display.update()
    while flag:
        # text1("Please enter your name", 700, 30)
        flag = quit(flag)
        screen.fill(bg_color)
                        
