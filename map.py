import sys
import pygame

pygame.init()
displayResolution = (640, 480)
screen = pygame.display.set_mode(displayResolution)

class Colors:
    def dark_blue(self):
        darkBlue = (0,0,128)
        return darkBlue


class Board:

    boardSize = 8
    lineColor = (0,0,128)
    screen = None

    def __init__(self, screen):
        self.screen = screen

    def draw_verticals(self):
        for point in range(self.boardSize):
            pygame.draw.lines(self.screen, self.lineColor, [(point,100), (screen.max(),100)], 1)

    def draw_horizontals(self):
        for point in range(self.boardSize):
            pygame.draw.lines(self.screen, self.lineColor, [(0,point), (100,screen.max())], 1)

    def segment_size(self):
        return self.screen / self.boardSize



pygame.display.update()
board = Board(screen)
board.draw_horizontals()
pygame.display.update()
print board.segment_size()


# pygame draw rect
# pygame.draw.rect(screen, color, (x,y,width,height), thickness)

# pygame draw lines
# pygame.draw.lines(screen, color, closed, pointlist, thickness)

# draws a series of lines, connecting the points specified in pointlist
# pointlist is a list of tuples, specifying a series of points, e.g. to draw a V you might use [(100,100), (150,200), (200,100)], with closed = False
# closed should be either True or False, indicating whether to connect the last point back to the first
# thickness is the thickness of the line (in pixels).
# Example: pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)
