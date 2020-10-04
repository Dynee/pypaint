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
selected_color = "BLACK"

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for color in colors:
                if color['rect'].collidepoint(x, y):
                    selected_color = color['color']
    print(selected_color)
    # flip updates the screen with what you draw
    pygame.display.flip()

pygame.quit()
