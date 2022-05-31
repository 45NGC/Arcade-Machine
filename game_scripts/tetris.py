from tarfile import BLOCKSIZE
from tkinter.tix import WINDOW
from game_scripts.utilities import draw_button2
import random
import pygame
pygame.init()


# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
dark_grey = (40,40,40)
grey = (60,60,60)
light_grey = (100,100,100)
yellow = (255,204,0)
green = (51,204,51)
purple = (153,0,255)
orange = (255, 153, 0)
red = (255, 57, 57)
blue = (0, 64, 255)
turquoise = (0, 255, 255)

# FONTS
font_h1 = pygame.font.Font('resources\\fonts\\Gameplay.ttf', 30)
font_h2 = pygame.font.Font('resources\\fonts\\Gameplay.ttf', 25)
font_h3 = pygame.font.Font('resources\\fonts\\Gameplay.ttf', 20)

tetris_panel_width = 400  
tetris_panel_height = 800
tetris_panel_X = 250
tetris_panel_Y = 25
tetris_panel = pygame.Rect(tetris_panel_X, tetris_panel_Y, tetris_panel_width, tetris_panel_height)
hold_panel_width = 150
hold_panel_height = 200
hold_panel_X = 50
hold_panel_Y = 50
next_panel_width = 150
next_panel_height = 400
next_panel_X = 700
next_panel_Y = 50

BLOCKSIZE = 40
TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5
WINDOWWIDTH = 900
WINDOWHEIGHT = 850
ROWS = 20
COLUMNS = 10
BLANK = '.'


# TETRIS UI FUNCTIONS
def draw_tetris_panels(screen) :
	tetris_panel_border = pygame.Rect(tetris_panel_X-2, tetris_panel_Y-2, tetris_panel_width+4, tetris_panel_height+4)
	tetris_panel = pygame.Rect(tetris_panel_X, tetris_panel_Y, tetris_panel_width, tetris_panel_height)

	hold_panel_border = pygame.Rect(hold_panel_X-2, hold_panel_Y-2, hold_panel_width+4, hold_panel_height+4)
	hold_panel = pygame.Rect(hold_panel_X, hold_panel_Y, hold_panel_width, hold_panel_height)
	hold_space = pygame.Rect(hold_panel_X+10, hold_panel_Y+60, hold_panel_width-20, hold_panel_height-70)

	score_panel_width = 150
	score_panel_height = 300
	score_panel_X = 50
	score_panel_Y = 500
	score_panel_border = pygame.Rect(score_panel_X-2, score_panel_Y-2, score_panel_width+4, score_panel_height+4)
	score_panel = pygame.Rect(score_panel_X, score_panel_Y, score_panel_width, score_panel_height)
	score_space = pygame.Rect(score_panel_X+10, score_panel_Y+60, score_panel_width-20, 50)
	lines_space = pygame.Rect(score_panel_X+10, score_panel_Y+220, score_panel_width-20, 50)

	next_panel_border = pygame.Rect(next_panel_X-2, next_panel_Y-2, next_panel_width+4, next_panel_height+4)
	next_panel = pygame.Rect(next_panel_X, next_panel_Y, next_panel_width, next_panel_height)
	next_space = pygame.Rect(next_panel_X+10, next_panel_Y+60, next_panel_width-20, next_panel_height-70)

	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650
	pause_button_border = pygame.Rect(pause_button_X-2, pause_button_Y-2, pause_button_size+4, pause_button_size+4)
	pause_button = pygame.Rect(pause_button_X, pause_button_Y, pause_button_size, pause_button_size)
	pause_button_simbol_1 = pygame.Rect(pause_button_X+30, pause_button_Y+15, 10, 70)
	pause_button_simbol_2 = pygame.Rect(pause_button_X+60, pause_button_Y+15, 10, 70)

	# 	- TETRIS
	# Panel
	pygame.draw.rect(screen, pink, tetris_panel_border)
	pygame.draw.rect(screen, dark_grey, tetris_panel)


	# 	- HOLD
	# Panel
	pygame.draw.rect(screen, pink, hold_panel_border)
	pygame.draw.rect(screen, dark_grey, hold_panel)
	pygame.draw.rect(screen, black, hold_space, border_radius = 10)

	# Text
	hold_string = 'HOLD'
	hold_text = font_h2.render(hold_string, True, white)
	screen.blit(hold_text, (hold_panel_X+40, hold_panel_Y+15))


	# 	- SCORE / LINES
	# Panel
	pygame.draw.rect(screen, pink, score_panel_border)
	pygame.draw.rect(screen, dark_grey, score_panel)
	pygame.draw.rect(screen, black, score_space, border_radius = 10)
	pygame.draw.rect(screen, black, lines_space, border_radius = 10)

	# Text
	score_string = 'SCORE'
	lines_string = 'LINES'
	score_text = font_h2.render(score_string, True, white)
	lines_text = font_h2.render(lines_string, True, white)
	screen.blit(score_text, (score_panel_X+30, score_panel_Y+15))
	screen.blit(lines_text, (score_panel_X+35, score_panel_Y+175))

	#score = font_h3.render(str(score).center(7), True, white)
	#lines = font_h3.render(str(lines).center(7), True, white)
	#screen.blit(score, (score_panel_X+30, score_panel_Y+70))
	#screen.blit(lines, (score_panel_X+30, score_panel_Y+230))


	# 	- NEXT
	# Panel
	pygame.draw.rect(screen, pink, next_panel_border)
	pygame.draw.rect(screen, dark_grey, next_panel)
	pygame.draw.rect(screen, black, next_space, border_radius = 10)

	# Text
	next_string = 'NEXT'
	next_text = font_h2.render(next_string, True, white)
	screen.blit(next_text, (next_panel_X+40, next_panel_Y+15))


	# 	- PAUSE
		# Button
	pygame.draw.rect(screen, pink, pause_button_border, border_radius = 20)
	pygame.draw.rect(screen, black, pause_button, border_radius = 20)
	pygame.draw.rect(screen, white, pause_button_simbol_1)
	pygame.draw.rect(screen, white, pause_button_simbol_2)

def draw_tetris_board(screen) :
	for i in range(ROWS):
			pygame.draw.line(screen, light_grey, (tetris_panel_X, tetris_panel_Y+ i*BLOCKSIZE), (tetris_panel_X + tetris_panel_width, tetris_panel_Y + i * BLOCKSIZE))
			for j in range(COLUMNS):
					pygame.draw.line(screen, light_grey, (tetris_panel_X + j * BLOCKSIZE, tetris_panel_Y), (tetris_panel_X + j * BLOCKSIZE, tetris_panel_Y + tetris_panel_height))

def draw_tetris_menu(screen, mouse) :
	# TETRIS LABEL
	tetris_title_string = 'TETRIS'
	tetris_label_width = 300
	tetris_label_height = 110
	tetris_label_X = 300
	tetris_label_Y = 75
	
	pygame.draw.rect(screen, pink, [tetris_label_X-10, tetris_label_Y-10, tetris_label_width+20, tetris_label_height+20])
	pygame.draw.rect(screen, pink, [tetris_label_X+99-10, tetris_label_Y-10, tetris_label_height+20, tetris_label_width-100+20])

	pygame.draw.rect(screen, purple, [tetris_label_X-8, tetris_label_Y-8, tetris_label_width+16, tetris_label_height+16])
	pygame.draw.rect(screen, purple, [tetris_label_X+99-8, tetris_label_Y-8, tetris_label_height+16, tetris_label_width-100+16])

	pygame.draw.rect(screen, pink, [tetris_label_X-2, tetris_label_Y-2, tetris_label_width+4, tetris_label_height+4])
	pygame.draw.rect(screen, pink, [tetris_label_X+99-2, tetris_label_Y-2, tetris_label_height+4, tetris_label_width-100+4])

	pygame.draw.rect(screen, black, [tetris_label_X, tetris_label_Y, tetris_label_width, tetris_label_height])
	pygame.draw.rect(screen, black, [tetris_label_X+99, tetris_label_Y, tetris_label_height, tetris_label_width-100])

	tetris_font = pygame.font.Font('resources\\fonts\\UniformBold.ttf', 100)
	tetris_text = tetris_font.render(tetris_title_string, True, white)
	screen.blit(tetris_text, (tetris_label_X+18, tetris_label_Y))

	# START BUTTON
	play_string = '    PLAY'
	play_button_X = 325
	play_button_Y = 350
	draw_button2(screen, play_button_X, play_button_Y, play_string, mouse)

	# HIGH SCORES TABLE
	highscores_string = 'HIGH SCORES'
	highscores_panel_width = 340
	highscores_panel_height = 320
	highscores_panel_X = 280
	highscores_panel_Y = 470
	highscores_panel_border = pygame.Rect(highscores_panel_X-2, highscores_panel_Y-2, highscores_panel_width+4, highscores_panel_height+4)
	highscores_panel = pygame.Rect(highscores_panel_X, highscores_panel_Y, highscores_panel_width, highscores_panel_height)
	record_1 = pygame.Rect(highscores_panel_X+15, highscores_panel_Y+60, highscores_panel_width-30, 47) 
	record_2 = pygame.Rect(highscores_panel_X+15, highscores_panel_Y+109, highscores_panel_width-30, 47)
	record_3 = pygame.Rect(highscores_panel_X+15, highscores_panel_Y+158, highscores_panel_width-30, 47)
	record_4 = pygame.Rect(highscores_panel_X+15, highscores_panel_Y+207, highscores_panel_width-30, 47)
	record_5 = pygame.Rect(highscores_panel_X+15, highscores_panel_Y+256, highscores_panel_width-30, 47)

	pygame.draw.rect(screen, pink, highscores_panel_border)
	pygame.draw.rect(screen, black, highscores_panel)

	pygame.draw.rect(screen, grey, record_1)
	pygame.draw.rect(screen, light_grey, record_2)
	pygame.draw.rect(screen, grey, record_3)
	pygame.draw.rect(screen, light_grey, record_4)
	pygame.draw.rect(screen, grey, record_5)

	highscores_text = font_h1.render(highscores_string, True, white)
	screen.blit(highscores_text, (highscores_panel_X+60, highscores_panel_Y+10))

def draw_tetris_pause(screen, mouse) :
	# Cover background
	pygame.draw.rect(screen, light_grey, tetris_panel)

	# Menu
	pause_string = 'PAUSE'
	pause_menu_size = 350
	pause_menu_X = 275
	pause_menu_Y = 220
	pause_menu_border = pygame.Rect(pause_menu_X-2, pause_menu_Y-2, pause_menu_size+4, pause_menu_size+4)
	pause_menu = pygame.Rect(pause_menu_X, pause_menu_Y, pause_menu_size, pause_menu_size)
	pygame.draw.rect(screen, pink, pause_menu_border)
	pygame.draw.rect(screen, black, pause_menu)
	pause_label = font_h1.render(pause_string, True, white)
	screen.blit(pause_label, (pause_menu_X+125, pause_menu_Y+20))

	# Buttons
	resume_string = '  RESUME'
	controls_string = 'CONTROLS'
	quit_string = '     QUIT'
	resume_button_X = 325
	resume_button_Y = 300
	controls_button_X = 325
	controls_button_Y = 390
	quit_button_X = 325
	quit_button_Y = 480
	draw_button2(screen, resume_button_X, resume_button_Y, resume_string, mouse)
	draw_button2(screen, controls_button_X, controls_button_Y, controls_string, mouse)
	draw_button2(screen, quit_button_X, quit_button_Y, quit_string, mouse)

	# Pause button
	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650
	pause_button_border = pygame.Rect(pause_button_X-2, pause_button_Y-2, pause_button_size+4, pause_button_size+4)
	pause_button = pygame.Rect(pause_button_X, pause_button_Y, pause_button_size, pause_button_size)
	pause_button_simbol_1 = pygame.Rect(pause_button_X+30, pause_button_Y+15, 10, 70)
	pause_button_simbol_2 = pygame.Rect(pause_button_X+60, pause_button_Y+15, 10, 70)
	pygame.draw.rect(screen, purple, pause_button_border, border_radius = 20)
	pygame.draw.rect(screen, black, pause_button, border_radius = 20)
	pygame.draw.rect(screen, pink, pause_button_simbol_1)
	pygame.draw.rect(screen, pink, pause_button_simbol_2)


# TETRIS GAME FUNCTIONS

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

COLORS = [green, red, blue, orange, turquoise, yellow, purple]


def get_piece():
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(ROWS / 2) - int(TEMPLATEWIDTH / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': COLORS[list(PIECES.keys()).index(shape)]}
    return newPiece

def get_empty_board():
	# returns a 10x20 array filled with blanks (.)
    board = []
    for i in range(COLUMNS):
        board.append([BLANK] * ROWS)
    return board

def is_valid_position(board, piece, ad_X=0, ad_Y=0):
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            above_board = y + piece['y'] + ad_Y < 0
            if above_board or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not (0 <= (x + piece['x'] + ad_X) < COLUMNS and (y + piece['y'] + ad_Y) < ROWS):
                return False
            if board[x + piece['x'] + ad_X][y + piece['y'] + ad_Y] != BLANK:
                return False
    return True

def add_piece_to_board(board, piece):
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][x][y] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

def draw_board_blocks(screen, board):
    for x in range(COLUMNS):
        for y in range(ROWS):
            draw_block(screen, x, y, board[x][y])

def draw_block(screen, blockx, blocky, color, x_axis=None, y_axis=None):
	# blockx and blocky are variables for the board pieces
	# x_axis and y_axis are variables for drawing the next and hold pieces
    if color == BLANK:
        return
    if x_axis == None and y_axis == None:
        x_axis, y_axis = tetris_panel_X + (blockx * BLOCKSIZE), tetris_panel_Y + (blocky * BLOCKSIZE) 
    pygame.draw.rect(screen, color, (x_axis, y_axis, BLOCKSIZE , BLOCKSIZE))

def draw_piece(screen, piece, pixelx=None, pixely=None):
    piece_shape = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        # if pixelx & pixely are specified, use the location stored in the piece data structure
        pixelx, pixely = tetris_panel_X + (piece['x'] * BLOCKSIZE), tetris_panel_Y + (piece['y'] * BLOCKSIZE)

    # draw each of the boxes that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if piece_shape[y][x] != BLANK:
                draw_block(screen, None, None, piece['color'], pixelx + (x * BLOCKSIZE), pixely + (y * BLOCKSIZE))


def draw_next_pieces(screen, piece1, piece2):
	if piece1 != None : draw_piece(screen, piece1,  pixelx=next_panel_X, pixely=next_panel_Y)
	if piece2 != None : draw_piece(screen, piece2,  pixelx=next_panel_X, pixely=next_panel_Y+100)
