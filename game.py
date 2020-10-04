import pygame, sys
from enum import Enum

pygame.init()

size = width, height = 500, 700

screen = pygame.display.set_mode(size)

class Color(Enum):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 64, 0)
    PURPLE = (191, 0, 255)
    PINK = (255, 0, 191)

class Canvas(pygame.Rect):
    def __init__(self, left, top, width, height, screen, border=1, children=[]): 
        pygame.Rect.__init__(self, left, top, width, height)
        self.screen = screen
        self.border = border
        self.children = children

    def setup(self):
        pygame.draw.rect(self.screen, Color.BLACK.value, [self.left, self.top, self.width, self.height], self.border) 

    def draw(self, color, x, y):
        """ handles drawing on the canvas """
        if self.collidepoint(x, y):
            pygame.draw.rect(self.screen, color, [x, y, 20, 20])

    def clear(self):
        """ clears the canvas of any drawings """


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_colors(screen):
    """
    This will draw the colors on a screen that can be selected like in paint
    draw a 20, 20 rect for each color in the colors enum

    """
    colors = []
    top, left, width, height = 20, 20, 20, 20
    for color in Color:
        c_rect = pygame.draw.rect(screen, color.value, [top, left, width, height])
        # next rect should be 20 to the right
        top += 20
        colors.append({'color': color.name, 'rect': c_rect})
    return colors
        
        

screen.fill(Color.WHITE.value)
colors = draw_colors(screen)
selected_color_rect = pygame.draw.rect(screen, Color.BLACK.value, [20, 50, 50, 50])
selected_color = "BLACK"
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
                if color['rect'].collidepoint(x, y):
                    selected_color = color['color']
                    selected_color_rect = pygame.draw.rect(screen, Color[selected_color].value, [20, 50, 50, 50])
            canvas.draw(Color[selected_color].value, x, y)

        if event.type == pygame.MOUSEBUTTONUP:
            drag = False
    # flip updates the screen with what you draw

    # draw the selected color rect
    pygame.display.flip()

pygame.quit()
