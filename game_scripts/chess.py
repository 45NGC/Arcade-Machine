import copy
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

# IMAGES

w_pawn = image.load('resources/chess-images/pieces/white/Wpawn.png')
w_knight = image.load('resources/chess-images/pieces/white/Wknight.png')
w_bishop = image.load('resources/chess-images/pieces/white/Wbishop.png')
w_rook = image.load('resources/chess-images/pieces/white/Wrook.png')
w_queen = image.load('resources/chess-images/pieces/white/Wqueen.png')
w_king = image.load('resources/chess-images/pieces/white/Wking.png')
white_pieces = [w_pawn, w_knight, w_bishop, w_rook, w_rook, w_queen, w_king]

b_pawn = image.load('resources/chess-images/pieces/black/Bpawn.png')
b_knight = image.load('resources/chess-images/pieces/black/Bknight.png')
b_bishop = image.load('resources/chess-images/pieces/black/Bbishop.png')
b_rook = image.load('resources/chess-images/pieces/black/Brook.png')
b_queen = image.load('resources/chess-images/pieces/black/Bqueen.png')
b_king = image.load('resources/chess-images/pieces/black/Bking.png')
black_pieces = [b_pawn, b_knight, b_bishop, b_rook, b_rook, b_queen, b_king]

king_moves = [[0, 1], [0, -1], [1, 0], [1, -1], [1, 1], [-1, 0], [-1, -1], [-1, 1]]
square_coordinates = [50, 125, 200, 275, 350, 425, 500, 575]

# CLASSES
class SelectedSquare:
	def __init__(self, x_coordinate, y_coordinate, x_index, y_index, value):
		self.x_coordinate = x_coordinate
		self.y_coordinate = y_coordinate
		self.x_index = x_index
		self.y_index = y_index
		self.value = value
	
	def __str__(self):
		return "coordinates : x -> "+str(self.x_coordinate)+" = "+str(self.x_index)+"    y -> "+str(self.y_coordinate)+" = "+str(self.y_index)
    



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

			if y[0] < 0 and y[0] > -8:
				screen.blit(black_pieces[(y[0]*-1)-1], (piece_coordinates[y[1]], piece_coordinates[x[1]]))
			elif y[0] > 0 and y[0] < 8:
				screen.blit(white_pieces[(y[0])-1], (piece_coordinates[y[1]], piece_coordinates[x[1]]))
			else:
				pass

def selected_square(x_coordinate, y_coordinate, board):
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

	selected_square = SelectedSquare(selected_square_x, selected_square_y, x_square_index, y_square_index, board[y_square_index][x_square_index])

	return selected_square


def available_squares(piece, piece_square, board_piece_positions, attacked_squares, on_peasant_square):
	x = piece_square[1]
	y = piece_square[0]

	if piece < 0:
		turn = -1
	else: 
		turn = 1

	available_squares = {
		'coordinates' 	: [],
		'indexes'		: []
	}


	if attacked_squares == False:

		# PAWN
		if piece in [1, -1]:

			# PUSH
			if board_piece_positions[y-piece][x] == 0:
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x], piece):
					available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x]))
				
			# FIRST PUSH
			if ((y == 6 and piece == 1) or (y == 1 and piece == -1)) and board_piece_positions[y-piece][x] == 0 and board_piece_positions[y-(piece*2)][x] == 0:
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-(piece*2), x], piece):
					available_squares['coordinates'].append((square_coordinates[y-(piece*2)],square_coordinates[x]))
			
			# NORMAL CAPTURE
			if x != 0 and x != 7 :

				if board_piece_positions[y-piece][x+1] < 0 and piece == 1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x+1], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x+1]))
				if board_piece_positions[y-piece][x-1] < 0 and piece == 1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x-1], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x-1]))

				if board_piece_positions[y-piece][x+1] > 0 and piece == -1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x+1], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x+1]))
				if board_piece_positions[y-piece][x-1] > 0 and piece == -1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x-1]))

			else:

				if x == 0 and board_piece_positions[y-piece][x+1] < 0 and piece == 1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x+1]))
				if x == 7 and board_piece_positions[y-piece][x-1] < 0 and piece == 1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x-1]))

				if x == 0 and board_piece_positions[y-piece][x+1] > 0 and piece == -1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x+1]))
				if x == 7 and board_piece_positions[y-piece][x-1] > 0 and piece == -1:
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-piece, x], piece):
						available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x-1]))
			
			# ON PEASANT CAPTURE
			if on_peasant_square != []:
				if on_peasant_square[1] == turn:
					x = on_peasant_square[0][1]
					y = on_peasant_square[0][0]
					if turn == 1:
						#White
						if (0 <= y+turn <= 7) and (x+1 <= 7) and (x-1 >= 0):
							if board_piece_positions[y+turn][x+1] == turn:
								# Backup board is necesary because we have to manually delete the pawn that is captured on it for then make sure that the king is safe
								backup_board = copy.deepcopy(board_piece_positions)
								backup_board[y+turn][x] = 0
								if  not is_king_on_check_after_move(backup_board, turn, [y+turn, x+1], [y, x], piece):
									available_squares['coordinates'].append((square_coordinates[y],square_coordinates[x]))

							if board_piece_positions[y+turn][x-1] == turn:
								backup_board = copy.deepcopy(board_piece_positions)
								backup_board[y+turn][x] = 0
								if  not is_king_on_check_after_move(backup_board, turn, [y+turn, x-1], [y, x], piece):
									available_squares['coordinates'].append((square_coordinates[y],square_coordinates[x]))
					else:
						#Black
						if (0 <= y+turn <= 7) and (x+1 <= 7) and (x-1 >= 0):
							if board_piece_positions[y+turn][x+1] == turn:
								backup_board = copy.deepcopy(board_piece_positions)
								backup_board[y+turn][x] = 0
								if  not is_king_on_check_after_move(backup_board, turn, [y+turn, x+1], [y, x], piece):
									available_squares['coordinates'].append((square_coordinates[y],square_coordinates[x]))

							if board_piece_positions[y+turn][x-1] == turn:
								backup_board = copy.deepcopy(board_piece_positions)
								backup_board[y+turn][x] = 0
								if  not is_king_on_check_after_move(backup_board, turn, [y+turn, x-1], [y, x], piece):
									available_squares['coordinates'].append((square_coordinates[y],square_coordinates[x]))

			# PROMOTION


		# WHITE KNIGHT
		if piece == 2 :

			# JUMP
			if 0 <= x+2 <= 7 and 0 <= y+1 <= 7  and board_piece_positions[y+1][x+2] <= 0 :
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+1, x+2], piece): 
					available_squares['coordinates'].append((square_coordinates[y+1], square_coordinates[x+2]))
			if 0 <= x+2 <= 7 and 0 <= y-1 <= 7  and board_piece_positions[y-1][x+2] <= 0 :
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-1, x+2], piece): 
					available_squares['coordinates'].append((square_coordinates[y-1], square_coordinates[x+2]))
			if 0 <= x-2 <= 7 and 0 <= y+1 <= 7  and board_piece_positions[y+1][x-2] <= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+1, x-2], piece):
					available_squares['coordinates'].append((square_coordinates[y+1], square_coordinates[x-2]))
			if 0 <= x-2 <= 7 and 0 <= y-1 <= 7  and board_piece_positions[y-1][x-2] <= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-1, x-2], piece):
					available_squares['coordinates'].append((square_coordinates[y-1], square_coordinates[x-2]))
			if 0 <= x+1 <= 7 and 0 <= y+2 <= 7  and board_piece_positions[y+2][x+1] <= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+2, x+1], piece):
					available_squares['coordinates'].append((square_coordinates[y+2], square_coordinates[x+1]))
			if 0 <= x+1 <= 7 and 0 <= y-2 <= 7  and board_piece_positions[y-2][x+1] <= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-2, x+1], piece):
					available_squares['coordinates'].append((square_coordinates[y-2], square_coordinates[x+1]))
			if 0 <= x-1 <= 7 and 0 <= y+2 <= 7  and board_piece_positions[y+2][x-1] <= 0 :
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+2, x-1], piece):
					available_squares['coordinates'].append((square_coordinates[y+2], square_coordinates[x-1]))
			if 0 <= x-1 <= 7 and 0 <= y-2 <= 7  and board_piece_positions[y-2][x-1] <= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-2, x-1], piece):
					available_squares['coordinates'].append((square_coordinates[y-2], square_coordinates[x-1]))


		# BLACK KNIGHT
		if piece == -2 :

			# JUMP
			if 0 <= x+2 <= 7 and 0 <= y+1 <= 7  and board_piece_positions[y+1][x+2] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+1, x+2], piece):
					available_squares['coordinates'].append((square_coordinates[y+1], square_coordinates[x+2]))
			if 0 <= x+2 <= 7 and 0 <= y-1 <= 7  and board_piece_positions[y-1][x+2] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-1, x+2], piece):
					available_squares['coordinates'].append((square_coordinates[y-1], square_coordinates[x+2]))
			if 0 <= x-2 <= 7 and 0 <= y+1 <= 7  and board_piece_positions[y+1][x-2] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+1, x-2], piece):
					available_squares['coordinates'].append((square_coordinates[y+1], square_coordinates[x-2]))
			if 0 <= x-2 <= 7 and 0 <= y-1 <= 7  and board_piece_positions[y-1][x-2] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-1, x-2], piece):
					available_squares['coordinates'].append((square_coordinates[y-1], square_coordinates[x-2]))
			if 0 <= x+1 <= 7 and 0 <= y+2 <= 7  and board_piece_positions[y+2][x+1] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+2, x+1], piece):
					available_squares['coordinates'].append((square_coordinates[y+2], square_coordinates[x+1]))
			if 0 <= x+1 <= 7 and 0 <= y-2 <= 7  and board_piece_positions[y-2][x+1] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-2, x+1], piece):
					available_squares['coordinates'].append((square_coordinates[y-2], square_coordinates[x+1]))
			if 0 <= x-1 <= 7 and 0 <= y+2 <= 7  and board_piece_positions[y+2][x-1] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+2, x-1], piece):
					available_squares['coordinates'].append((square_coordinates[y+2], square_coordinates[x-1]))
			if 0 <= x-1 <= 7 and 0 <= y-2 <= 7  and board_piece_positions[y-2][x-1] >= 0 : 
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-2, x-1], piece):
					available_squares['coordinates'].append((square_coordinates[y-2], square_coordinates[x-1]))

		
		# WHITE BISHOP + WHITE QUEEN
		if piece in [3, 6]:
				
			for index in range(1,8):
				if (0 > y-index) or (x+index > 7) : break

				if board_piece_positions[y-index][x+index] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-index, x+index], piece):
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x+index]))
				if board_piece_positions[y-index][x+index] < 0 : break

			

			for index in range(1,8):
				if (y+index > 7) or (0 > x-index) : break

				if board_piece_positions[y+index][x-index] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+index, x-index], piece):
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x-index]))
				if board_piece_positions[y+index][x-index] < 0 : break
				
			

			for index in range(1,8):
				if (0 > y-index) or (0 > x-index) : break

				if board_piece_positions[y-index][x-index] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-index, x-index], piece):
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x-index]))
				if board_piece_positions[y-index][x-index] < 0 : break
				
			

			for index in range(1,8):
				if (y+index > 7) or (x+index > 7) : break
				
				if board_piece_positions[y+index][x+index] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+index, x+index], piece):
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x+index]))
				if board_piece_positions[y+index][x+index] < 0 : break


		# BLACK BISHOP + BLACK QUEEN
		if piece in [-3, -6]:
				
			for index in range(1,8):
				if (0 > y-index) or (x+index > 7) : break

				if board_piece_positions[y-index][x+index] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-index, x+index], piece):
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x+index]))
				if board_piece_positions[y-index][x+index] > 0 : break
				
			

			for index in range(1,8):
				if (y+index > 7) or (0 > x-index) : break

				if board_piece_positions[y+index][x-index] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+index, x-index], piece):
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x-index]))
				if board_piece_positions[y+index][x-index] > 0 : break
				
			

			for index in range(1,8):
				if (0 > y-index) or (0 > x-index) : break
				
				if board_piece_positions[y-index][x-index] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-index, x-index], piece):
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x-index]))
				if board_piece_positions[y-index][x-index] > 0 : break
				
			

			for index in range(1,8):
				if (y+index > 7) or (x+index > 7) : break

				if board_piece_positions[y+index][x+index] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+index, x+index], piece):
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x+index]))
				if board_piece_positions[y+index][x+index] > 0 : break
				
		

		# WHITE ROOK + WHITE QUEEN
		if piece in [4, 5, 6]:
			
			for index in range(1,8):
				if (0 > x+index) or (x+index > 7) : break
				
				if board_piece_positions[y][x+index] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y, x+index], piece):
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x+index]))
				if board_piece_positions[y][x+index] < 0 : break
				

			
			for index in range(1,8):
				if (0 > x-index) or (x-index > 7) : break
				
				if board_piece_positions[y][x-index] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y, x-index], piece):
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x-index]))
				if board_piece_positions[y][x-index] < 0 : break
				
			

			for index in range(1,8):
				if (0 > y+index) or (y+index > 7) : break
				
				if board_piece_positions[y+index][x] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+index, x], piece):
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x]))
				if board_piece_positions[y+index][x] < 0 : break
				
			

			for index in range(1,8):
				if (0 > y-index) or (y-index > 7) : break
				
				if board_piece_positions[y-index][x] > 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-index, x], piece):
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x]))
				if board_piece_positions[y-index][x] < 0 : break
				
		

		# BLACK ROOK + BLACK QUEEN
		if piece in [-4, -5, -6]:
			
			for index in range(1,8):
				if (x+index > 7) : break
				
				if board_piece_positions[y][x+index] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y, x+index], piece):
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x+index]))
				if board_piece_positions[y][x+index] > 0 : break
				

			
			for index in range(1,8):
				if (0 > x-index) : break
				
				if board_piece_positions[y][x-index] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y, x-index], piece):
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x-index]))
				if board_piece_positions[y][x-index] > 0 : break
				
			

			for index in range(1,8):
				if (y+index > 7) : break
				
				if board_piece_positions[y+index][x] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+index, x], piece):
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x]))
				if board_piece_positions[y+index][x] > 0 : break
				
			

			for index in range(1,8):
				if (0 > y-index) : break
				
				if board_piece_positions[y-index][x] < 0 : break
				if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y-index, x], piece):
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x]))
				if board_piece_positions[y-index][x] > 0 : break
			

	else:
		# Only shows attacked squares

		# PAWN
		if piece in [1, -1]:

			if x != 0 and x != 7 :
				available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x+1]))
				available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x-1]))
			else:
				if x == 0:
					available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x+1]))
				if x == 7:
					available_squares['coordinates'].append((square_coordinates[y-piece],square_coordinates[x-1]))
		
		# KNIGHT
		if piece in [2, -2]:

			if 0 <= x+2 <= 7 and 0 <= y+1 <= 7: 
				available_squares['coordinates'].append((square_coordinates[y+1], square_coordinates[x+2]))
			if 0 <= x+2 <= 7 and 0 <= y-1 <= 7: 
				available_squares['coordinates'].append((square_coordinates[y-1], square_coordinates[x+2]))
			if 0 <= x-2 <= 7 and 0 <= y+1 <= 7: 
				available_squares['coordinates'].append((square_coordinates[y+1], square_coordinates[x-2]))
			if 0 <= x-2 <= 7 and 0 <= y-1 <= 7: 
				available_squares['coordinates'].append((square_coordinates[y-1], square_coordinates[x-2]))
			if 0 <= x+1 <= 7 and 0 <= y+2 <= 7: 
				available_squares['coordinates'].append((square_coordinates[y+2], square_coordinates[x+1]))
			if 0 <= x+1 <= 7 and 0 <= y-2 <= 7: 
				available_squares['coordinates'].append((square_coordinates[y-2], square_coordinates[x+1]))
			if 0 <= x-1 <= 7 and 0 <= y+2 <= 7:
				available_squares['coordinates'].append((square_coordinates[y+2], square_coordinates[x-1]))
			if 0 <= x-1 <= 7 and 0 <= y-2 <= 7: 
				available_squares['coordinates'].append((square_coordinates[y-2], square_coordinates[x-1]))

		# BISHOP / QUEEN
		if piece in [3, -3, 6, -6]:

			for index in range(1,8):
				if (0 > y-index) or (x+index > 7) : break
				
				if board_piece_positions[y-index][x+index] != 0 :
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x+index]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x+index]))

			for index in range(1,8):
				if (y+index > 7) or (0 > x-index) : break
				
				if board_piece_positions[y+index][x-index] != 0 : 
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x-index]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x-index]))

			for index in range(1,8):
				if (0 > y-index) or (0 > x-index) : break
				
				if board_piece_positions[y-index][x-index] != 0 :
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x-index]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x-index]))

			for index in range(1,8):
				if (y+index > 7) or (x+index > 7) : break
				
				if board_piece_positions[y+index][x+index] != 0 :
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x+index]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x+index]))
		
		# ROOK / QUEEN
		if piece in [4, -4, 5, -5, 6, -6]:

			for index in range(1,8):
				if (x+index > 7) : break
				
				if board_piece_positions[y][x+index] != 0 :
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x+index]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x+index]))
			
			for index in range(1,8):
				if (y+index > 7) : break
				
				if board_piece_positions[y+index][x] != 0 :
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y+index], square_coordinates[x]))
			
			for index in range(1,8):
				if (0 > x-index) : break
				
				if board_piece_positions[y][x-index] != 0 :
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x-index]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y], square_coordinates[x-index]))
			
			for index in range(1,8):
				if (0 > y-index) : break
				
				if board_piece_positions[y-index][x] != 0 :
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x]))
					break
				else:
					available_squares['coordinates'].append((square_coordinates[y-index], square_coordinates[x]))
		
		# KING
		if piece in [7, -7]:

			for move in king_moves:
				if ((0 <= y+move[0] <= 7) and (0 <= x+move[1] <= 7)):
					available_squares['coordinates'].append((square_coordinates[y+move[0]], square_coordinates[x+move[1]]))
							


	# INDEX
	for coordinate in available_squares['coordinates']:
		available_squares['indexes'].append([square_coordinates.index(coordinate[1]), square_coordinates.index(coordinate[0])])

	return available_squares



# Function that shows what squares are being attacked by the opponent
def get_attacked_squares(board, turn):

	attacked_squares_list = {
		'coordinates' 	: [],
		'indexes'		: []
	}

	positions = [0, 1, 2, 3, 4, 5, 6, 7]

	for line in zip(board, positions):
		for square in zip(line[0], positions):

			if square[0] != 0:
				if (turn == 1 and square[0] < 0) or (turn == -1 and square[0] > 0):

					piece_square = [line[1], square[1]]

					attacked_squares = available_squares(square[0], piece_square, board, True, [])

					for attacked_square in zip(attacked_squares['indexes'], attacked_squares['coordinates']):
						attacked_squares_list['indexes'].append(attacked_square[0])
						attacked_squares_list['coordinates'].append(attacked_square[1])

	return attacked_squares_list

# Function that shows what squares are available in the current turn
def get_available_squares(board, turn, on_peasant_square):

	available_squares_list = {
		'coordinates' 	: [],
		'indexes'		: []
	}

	positions = [0, 1, 2, 3, 4, 5, 6, 7]

	for line in zip(board, positions):
		for square in zip(line[0], positions):

			if square[0] != 0:
				if (turn == 1 and square[0] > 0) or (turn == -1 and square[0] < 0):

					piece_square = [line[1], square[1]]

					piece_available_squares = available_squares(square[0], piece_square, board, False, on_peasant_square)

					for available_square in zip(piece_available_squares['indexes'], piece_available_squares['coordinates']):
						available_squares_list['indexes'].append(available_square[0])
						available_squares_list['coordinates'].append(available_square[1])
	
	return available_squares_list


def king_available_squares(piece, king_square, board_piece_positions, attacked_squares, castling):
	x = king_square[1]
	y = king_square[0]

	available_squares = {
		'coordinates' 	: [],
		'indexes'		: []
	}
	
	# White
	if piece > 0:
		turn = 1

		for move in king_moves:
			if ((0 <= y+move[0] <= 7) and (0 <= x+move[1] <= 7)):
				if board_piece_positions[y+move[0]][x+move[1]] <= 0 :
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+move[0], x+move[1]], piece):
						available_squares['coordinates'].append((square_coordinates[y+move[0]], square_coordinates[x+move[1]]))

		# We do not use the original king square because the coordinates are inverted, when we use the search_king_square function we invert those coordinates.
		new_king_square = search_king_square(board_piece_positions, turn)
		king_on_check = is_king_on_check(new_king_square, attacked_squares)
		#  CASTLE:
		if castling['white-king-moved'] != True and king_on_check != True:
			
			# SHORT CASTLE
			if castling['white-short-moved'] == False:
				if board_piece_positions[7][5] == 0 and board_piece_positions[7][6] == 0 and board_piece_positions[7][7] == 4 and [5, 7] not in attacked_squares['indexes'] :
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [7, 6], piece):
						available_squares['coordinates'].append((square_coordinates[7], square_coordinates[6]))
			
			# LONG CASTLE
			if castling['white-long-moved'] == False:
				if board_piece_positions[7][3] == 0 and board_piece_positions[7][2] == 0 and board_piece_positions[7][1] == 0 and board_piece_positions[7][0] == 5 and [3, 7] not in attacked_squares['indexes'] :
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [7, 2], piece):
						available_squares['coordinates'].append((square_coordinates[7], square_coordinates[2]))


	# Black
	else:
		turn = -1

		for move in king_moves:
			if ((0 <= y+move[0] <= 7) and (0 <= x+move[1] <= 7)):
				if board_piece_positions[y+move[0]][x+move[1]] >= 0 :
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [y+move[0], x+move[1]], piece):
						available_squares['coordinates'].append((square_coordinates[y+move[0]], square_coordinates[x+move[1]]))

		new_king_square = search_king_square(board_piece_positions, turn)
		king_on_check = is_king_on_check(new_king_square, attacked_squares)
		#  CASTLE:
		if castling['black-king-moved'] != True and king_on_check != True:
			
			# SHORT CASTLE
			if castling['black-short-moved'] == False:
				if board_piece_positions[0][5] == 0 and board_piece_positions[0][6] == 0 and board_piece_positions[0][7] == -4 and [5, 0] not in attacked_squares['indexes'] :
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [0, 6], piece):
						available_squares['coordinates'].append((square_coordinates[0], square_coordinates[6]))
			
			# LONG CASTLE
			if castling['black-long-moved'] == False:
				if board_piece_positions[0][3] == 0 and board_piece_positions[0][2] == 0 and board_piece_positions[0][1] == 0 and board_piece_positions[0][0] == -5 and [3, 0] not in attacked_squares['indexes'] :
					if  not is_king_on_check_after_move(board_piece_positions, turn, [y, x], [0, 2], piece):
						available_squares['coordinates'].append((square_coordinates[0], square_coordinates[2]))



	# INDEX
	for coordinate in available_squares['coordinates']:
		available_squares['indexes'].append([square_coordinates.index(coordinate[1]), square_coordinates.index(coordinate[0])])


	return available_squares

def search_king_square(board, turn):
	for line in board:
		for piece in line:
			if piece == 7*turn:
				king_square = [line.index(7*turn), board.index(line)]
				return king_square

def is_king_on_check(king_square, attacked_squares):
	if king_square in attacked_squares['indexes']:
		return True
	else:
		return False	
		
def is_king_on_check_after_move(board, turn, piece_square, piece_square_after_move, piece):
	# We have to make sure that after the move that we are about to make our king is not in check,
	# otherwise this would be an illegal move.
	# To make sure that this is not our case, we try the move on an backup board, if in the backup board the king is checked we
	# do not make the move. If after the move in the backup board the king is safe we make the move.

	# Make the move on the backup board:
	backup_board = copy.deepcopy(board)

	backup_board[piece_square_after_move[0]][piece_square_after_move[1]] = piece
	backup_board[piece_square[0]][piece_square[1]] = 0

	backup_king_square = search_king_square(backup_board, turn)
	backup_attacked_squares = get_attacked_squares(backup_board, turn)
	backup_king_on_check = is_king_on_check(backup_king_square, backup_attacked_squares)

	if backup_king_on_check:
		return True
	else:
		return False