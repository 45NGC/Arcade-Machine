import pygame
from game_scripts.utilities import draw_button2
from pygame import image
pygame.init()

# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
purple = (153,0,255)

# CHESS PIECES

w_pawn = image.load('resources/chess-images/pieces/white/Wpawn.png')
w_knight = image.load('resources/chess-images/pieces/white/Wknight.png')
w_bishop = image.load('resources/chess-images/pieces/white/Wbishop.png')
w_rook = image.load('resources/chess-images/pieces/white/Wrook.png')
w_queen = image.load('resources/chess-images/pieces/white/Wqueen.png')
w_king = image.load('resources/chess-images/pieces/white/Wking.png')
white_pieces = [w_pawn, w_knight, w_bishop, w_rook, w_queen, w_king]

b_pawn = image.load('resources/chess-images/pieces/black/Bpawn.png')
b_knight = image.load('resources/chess-images/pieces/black/Bknight.png')
b_bishop = image.load('resources/chess-images/pieces/black/Bbishop.png')
b_rook = image.load('resources/chess-images/pieces/black/Brook.png')
b_queen = image.load('resources/chess-images/pieces/black/Bqueen.png')
b_king = image.load('resources/chess-images/pieces/black/Bking.png')
black_pieces = [b_pawn, b_knight, b_bishop, b_rook, b_queen, b_king]

square_coordinates = [50, 125, 200, 275, 350, 425, 500, 575]



def draw_chess_menu(screen, mouse) :
	# Title
	chess_title_string = 'CHESS'
	chess_label_background1 = pygame.Rect(300, 30, 300, 250)
	chess_label_background2 = pygame.Rect(310, 40, 280, 230)
	pygame.draw.ellipse(screen, white, chess_label_background1)
	pygame.draw.ellipse(screen, black, chess_label_background2)

	chess_title_font = pygame.font.Font('resources/fonts/ARCADECLASSIC.TTF', 70)
	chess_title = chess_title_font.render(chess_title_string, True, white)
	screen.blit(chess_title, (350,120))

	# Game modes buttons
	mode1_string  = 'PLAY'
	draw_button2(screen, 330, 330, mode1_string, mouse)


def draw_pieces(screen, board_piece_positions):
	piece_coordinates = [65, 140, 215, 290, 365, 440, 515, 590]
	positions = [0, 1, 2, 3, 4, 5, 6, 7]

	for x in zip(board_piece_positions, positions):
		for y in zip(x[0], positions):

			if y[0] < 0 and y[0] > -7:
				screen.blit(black_pieces[(y[0]*-1)-1], (piece_coordinates[y[1]], piece_coordinates[x[1]]))
			elif y[0] > 0 and y[0] < 7:
				screen.blit(white_pieces[(y[0])-1], (piece_coordinates[y[1]], piece_coordinates[x[1]]))
			else:
				pass

def selected_square(x_coordinate, y_coordinate):
	selected_square_x = None
	selected_square_y = None
	x_square_index = None
	y_square_index = None

	if x_coordinate > 50 and y_coordinate > 50 and x_coordinate < 650 and y_coordinate < 650:

		for x_square_coordinate in square_coordinates:
			
			if x_coordinate >= x_square_coordinate and x_coordinate < x_square_coordinate+75:
				selected_square_x = x_square_coordinate
				x_square_index = square_coordinates.index(selected_square_x)

		for y_square_coordinate in square_coordinates:
			
			if y_coordinate >= y_square_coordinate and y_coordinate < y_square_coordinate+75:
				selected_square_y = y_square_coordinate
				y_square_index = square_coordinates.index(selected_square_y)
		
	else:
		return None
	
	# print('x_coordinate : '+str(x_coordinate))
	# print('y_coordinate : '+str(y_coordinate))	
	# print('selected_square_x : '+str(selected_square_x))
	# print('selected_square_y : '+str(selected_square_y))

	return selected_square_x, selected_square_y, x_square_index, y_square_index

def avaiable_squares(piece, piece_square, board_piece_positions):
	x = piece_square[1]
	y = piece_square[0]
	avaiable_squares = []

	if piece == 1:

		# PUSH
		if board_piece_positions[y-1][x] == 0:
			avaiable_squares.append((square_coordinates[y-1],square_coordinates[x]))
			
		# FIRST PUSH 
		if y == 6 and board_piece_positions[y-1][x] == 0 and board_piece_positions[y-2][x] == 0:
			avaiable_squares.append((square_coordinates[y-2],square_coordinates[x]))

	return avaiable_squares

		
	
