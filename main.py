#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_text(screen, text, font, font_color, position, anti_aliased=True, italic=False, bold=False):
    img = font.render(text, True, font_color)
    screen.blit(img, position,)

def draw_rect(screen,x,y,width,height):
    pygame.draw.rect(screen,config.PURPLE,(x,y, width, height))

def handle_events (x1,y1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return x1,y1, False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]and y1>0:
        y1 -=10
    if keys[pygame.K_DOWN]and y1<580:
        y1+=10
    if keys[pygame.K_LEFT]and x1>0:
        x1-=10
    if keys[pygame.K_RIGHT] and x1<760:
        x1+=10
        
    return x1,y1, True
def main():
    
    screen = init_game()
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('airal',55)

    x1 , y1 = (300,250)
    
    running = True
    while running:
        x1, y1, running = handle_events(x1,y1)
        screen.fill(config.WHITE) # Use color from config
        
        # Add code to draw stuff (for example) below this comment

        draw_rect(screen,x1,y1, 40 ,20)

        draw_text(screen, 'Use Arrow Keys To Move',font, config.BLACK, (190,100))

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
