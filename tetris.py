import pygame

# lol I stole some code to TechWithTim.

pygame.init()
pygame.font.init()

WIDTH = 300
HEIGHT = 600
BOARD_WIDTH = 200
BOARD_HEIGHT = 400
BLOCK_SIZE = BOARD_WIDTH // 10

TOP_LEFT_X = (WIDTH - BOARD_WIDTH) // 2
TOP_LEFT_Y = (HEIGHT - BOARD_HEIGHT) // 2

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

pygame.display.set_caption("Bad Tetris - By Cookie")
pygame.display.set_icon(pygame.image.load('./img/icon.png'))

win = pygame.display.set_mode((WIDTH, HEIGHT))

def make_grid():
      for i in range(10):
            pygame.draw.line(win, (100, 100, 100), ((i+1) * BLOCK_SIZE + TOP_LEFT_X, TOP_LEFT_Y), 
                        ((i+1) * BLOCK_SIZE + TOP_LEFT_X, TOP_LEFT_Y  + BOARD_HEIGHT), 2)
      for i in range(20):
            pygame.draw.line(win, (100, 100, 100), (TOP_LEFT_X, (i+1) * BLOCK_SIZE + TOP_LEFT_Y), 
                        (TOP_LEFT_X + BOARD_WIDTH, (i+1) * BLOCK_SIZE + TOP_LEFT_Y), 2)

def draw():
      win.fill((0, 0, 0))

      make_grid()

      pygame.draw.line(win, (255, 255, 255), (TOP_LEFT_X, TOP_LEFT_Y), (TOP_LEFT_X + BOARD_WIDTH, TOP_LEFT_Y), 2)
      pygame.draw.line(win, (255, 255, 255), (TOP_LEFT_X, TOP_LEFT_Y), (TOP_LEFT_X, TOP_LEFT_Y + BOARD_HEIGHT), 2)
      pygame.draw.line(win, (255, 255, 255), (TOP_LEFT_X, TOP_LEFT_Y + BOARD_HEIGHT), 
                        (TOP_LEFT_X + BOARD_WIDTH, TOP_LEFT_Y + BOARD_HEIGHT), 2)
      pygame.draw.line(win, (255, 255, 255), (TOP_LEFT_X + BOARD_WIDTH, TOP_LEFT_Y + BOARD_HEIGHT), 
                        (TOP_LEFT_X + BOARD_WIDTH, TOP_LEFT_Y), 2)


run = True

while run:      
      pygame.time.delay(int(1000 / 60))
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      draw()
      pygame.display.update()


pygame.quit()