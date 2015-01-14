import sys
import pygame

pygame.init()
displayResolution = (1366, 768)
screen = pygame.display.set_mode(displayResolution)

class Colors:
    def dark_blue(self):
        return (0, 0, 128)

    def blue(self):
        return (0, 0, 255)

    def black(self):
        return (0, 0, 0)

    def white(self):
        return (255, 255, 255)

class Board:
#    boardSize # Board size, eventually this will be an option on start.
                  # Small: 8x8x8 (512 sectors), Medium: 10x10x10 (1000 sectors), or Huge: 12x12x12 (1728 sectors)
#    screen =  # Holds the screen object to draw upon
#    resolution =  # Holds a tuple with the resolution of the main screen object

    def __init__(self, screen, boardSize):
        colors = Colors()
        self.screen = screen
        self.boardSize = boardSize
        self.resolution = screen.get_size()
        self.lineColor = colors.blue()    # dark blue
        self.widthSegment = self.resolution[0] / self.boardSize
        self.heightSegment = self.resolution[1] / self.boardSize
        print self.widthSegment
        print self.heightSegment

    def draw(self):
        self.draw_verticals()
        self.draw_horizontals()
        pygame.display.update()

    def draw_horizontals(self):
        for point in range(0, self.boardSize):
            pygame.draw.lines(self.screen, self.lineColor, False, [(point * self.widthSegment, self.resolution[0]), (point * self.widthSegment, self.resolution[0])], 3)

    def draw_verticals(self):
        for point in range(0, self.boardSize):
            pygame.draw.lines(self.screen, self.lineColor, False, [(point * self.heightSegment, self.resolution[1]), (point * self.heightSegment, self.resolution[1])], 3)

    def segment_size(self, plane):
        return self.screen.get_width() if (plane == 0) else self.screen.get_height()


board = Board(screen, 8)
board.draw()


# Loop to keep window open until game closed
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


# pygame draw rect
# pygame.draw.rect(screen, color, (x,y,width,height), thickness)

# pygame draw lines
# pygame.draw.lines(screen, color, closed, pointlist, thickness)

# draws a series of lines, connecting the points specified in pointlist
# pointlist is a list of tuples, specifying a series of points, e.g. to draw a V you might use [(100,100), (150,200), (200,100)], with closed = False
# closed should be either True or False, indicating whether to connect the last point back to the first
# thickness is the thickness of the line (in pixels).
# Example: pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)
