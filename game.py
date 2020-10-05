import pygame, sys
from enum import Enum

pygame.init()

size = width, height = 500, 700

screen = pygame.display.set_mode(size)


class Color():
    COLORS = {
        "RED":  (255, 0, 0),
        "BLUE": (0, 0, 255),
        "GREEN": (0, 255, 0),
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "YELLOW": (255, 255, 0),
        "ORANGE": (255, 64, 0),
        "PURPLE": (191, 0, 255),
        "PINK": (255, 0, 191)
    }
    
    def __init__(self, color):
        self.color = self.COLORS[color]
        self.rect = None

    def draw(self, screen, dimensions):
        if not isinstance(dimensions, list):
            raise ValueError("dimensions must be a List")
        self.rect = pygame.draw.rect(screen, self.color, dimensions)

class Canvas(pygame.Rect):
    def __init__(self, left, top, width, height, screen, border=1, children=[]): 
        pygame.Rect.__init__(self, left, top, width, height)
        self.screen = screen
        self.border = border
        self.children = children

    def setup(self):
        pygame.draw.rect(self.screen, Color("BLACK").color, [self.left, self.top, self.width, self.height], self.border) 

    def draw(self, color, x, y):
        """ handles drawing on the canvas """
        if self.collidepoint(x, y):
            pygame.draw.rect(self.screen, color, [x, y, 20, 20])

    def clear(self):
        """ clears the canvas of any drawings """
        
        

screen.fill(Color("WHITE").color)

colors = [Color("RED"), Color("BLUE"), Color("GREEN"), Color("BLACK"), Color("YELLOW"), Color("ORANGE"), Color("PURPLE"), Color("PINK")]
color_left, color_top, color_width, color_height = 20, 20, 20, 20
for color in colors:
    color.draw(screen, [color_top, color_left, color_width, color_height])
    color_top += 20

selected_color_rect = pygame.draw.rect(screen, Color("BLACK").color, [20, 50, 50, 50])
selected_color = Color("BLACK").color
# acts as the canvas that can be drawn on
canvas = Canvas(20, 110, 465, 565, screen)
canvas.setup()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
            x, y = event.pos
            for color in colors:
                if color.rect.collidepoint(x, y):
                    selected_color = color.color
                    selected_color_rect = pygame.draw.rect(screen, selected_color, [20, 50, 50, 50])
            canvas.draw(selected_color, x, y)

        if event.type == pygame.MOUSEBUTTONUP:
            drag = False
    # flip updates the screen with what you draw

    # draw the selected color rect
    pygame.display.flip()

pygame.quit()
