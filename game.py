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

class Canvas():
    def __init__(self, screen, width, height, pos, border=1):
        self.screen = screen
        self.width = width
        self.height = height
        self.border = border
        self.pos = pos

    def setup(self):
        pygame.draw.rect(self.screen, Color.BLACK.value, [self.pos[0], self.pos[1], self.width, self.height], self.border)

    def draw(self):
        """ handles drawing on the canvas """

    def clear(self):
        """ clears the canvas of any drawings """



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
selected_color = pygame.draw.rect(screen, Color.BLACK.value, [20, 50, 50, 50])
# acts as the canvas that can be drawn on
canvas = Canvas(screen, 465, 565, [20, 110])
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
                    # draw a line between start pos and end pos

        if event.type == pygame.MOUSEBUTTONUP:
            drag = False
    # flip updates the screen with what you draw

    # draw the selected color rect
    pygame.display.flip()

pygame.quit()
