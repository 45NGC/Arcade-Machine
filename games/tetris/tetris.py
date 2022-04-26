import pygame
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)

# Create colors
black = (0,0,0)
grey = (90,90,90)
white = (255,255,255)
yellow = (255, 204, 0)
green = (51, 204, 51)
purple = (153, 0, 255)
orange = (255, 153, 0)
red = (179, 0, 0)
blue = (0, 64, 255)
turquoise = (0, 255, 255)

# Panels
tetris_panel_width = 400  
tetris_panel_height = 800

hold_panel_width = 150
hold_panel_height = 200

score_panel_width = 150
score_panel_height = 300

next_panel_width = 150
next_panel_height = 400

pause_size = 100

# Buttons

# Block
block_size = 40

# Pieces
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


main_path = 'main.py'

## TETRIS MAIN LOOP ##
while True:

	for event in pygame.event.get():
		print(event)
	
		if event.type == pygame.QUIT:
			pygame.quit()
			exec(open(main_path).read())
	
	# pygame.draw.rect(screen, white, [5,5, block_size, block_size])
	# pygame.draw.rect(screen, yellow, [5,105, block_size, block_size])
	# pygame.draw.rect(screen, green, [5,205, block_size, block_size])
	# pygame.draw.rect(screen, purple, [5,305, block_size, block_size])
	# pygame.draw.rect(screen, orange, [5,405, block_size, block_size])
	# pygame.draw.rect(screen, red, [5,505, block_size, block_size])
	# pygame.draw.rect(screen, blue, [5,605, block_size, block_size])
	# pygame.draw.rect(screen, turquoise, [5,705, block_size, block_size])

	# Tetris panel
	pygame.draw.rect(screen, white, [250,25, tetris_panel_width, tetris_panel_height])

	# Hold panel
	pygame.draw.rect(screen, white, [50,50, hold_panel_width, hold_panel_height])
	
	# Score panel
	pygame.draw.rect(screen, white, [50,500, score_panel_width, score_panel_height])

	# Next panel
	pygame.draw.rect(screen, white, [700,50, next_panel_width, next_panel_height])

	# Pause panel
	pygame.draw.rect(screen, white, [725,650, pause_size, pause_size])
	pygame.display.flip()