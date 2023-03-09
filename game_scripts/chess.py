import pygame
from game_scripts.utilities import draw_button2
from pygame import image
pygame.init()

# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
purple = (153,0,255)

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
	mode1_string  = '1 vs 1'
	draw_button2(screen, 330, 330, mode1_string, mouse)

def draw_chess_pieces(screen, mouse):
	piece_coordinates = [65, 140, 215, 290, 365, 440, 515, 590]
	square_center_coordinates = []
	# PAWN
	w_pawn1 = image.load('resources/chess-images/pieces/white/Wpawn.png')
	w_pawn2 = image.load('resources/chess-images/pieces/white/Wpawn.png')
	w_pawn3 = image.load('resources/chess-images/pieces/white/Wpawn.png')
	w_pawn4 = image.load('resources/chess-images/pieces/white/Wpawn.png')
	w_pawn5 = image.load('resources/chess-images/pieces/white/Wpawn.png')
	w_pawn6 = image.load('resources/chess-images/pieces/white/Wpawn.png')
	w_pawn7 = image.load('resources/chess-images/pieces/white/Wpawn.png')
	w_pawn8 = image.load('resources/chess-images/pieces/white/Wpawn.png')

	w_knight1 = image.load('resources/chess-images/pieces/white/Wknight.png')
	w_knight2 = image.load('resources/chess-images/pieces/white/Wknight.png')

	w_bishop1 = image.load('resources/chess-images/pieces/white/Wbishop.png')
	w_bishop2 = image.load('resources/chess-images/pieces/white/Wbishop.png')

	w_rook1 = image.load('resources/chess-images/pieces/white/Wrook.png')
	w_rook2 = image.load('resources/chess-images/pieces/white/Wrook.png')

	w_queen = image.load('resources/chess-images/pieces/white/Wqueen.png')
	w_king = image.load('resources/chess-images/pieces/white/Wking.png')


	b_pawn1 = image.load('resources/chess-images/pieces/black/Bpawn.png')
	b_pawn2 = image.load('resources/chess-images/pieces/black/Bpawn.png')
	b_pawn3 = image.load('resources/chess-images/pieces/black/Bpawn.png')
	b_pawn4 = image.load('resources/chess-images/pieces/black/Bpawn.png')
	b_pawn5 = image.load('resources/chess-images/pieces/black/Bpawn.png')
	b_pawn6 = image.load('resources/chess-images/pieces/black/Bpawn.png')
	b_pawn7 = image.load('resources/chess-images/pieces/black/Bpawn.png')
	b_pawn8 = image.load('resources/chess-images/pieces/black/Bpawn.png')

	b_knight1 = image.load('resources/chess-images/pieces/black/Bknight.png')
	b_knight2 = image.load('resources/chess-images/pieces/black/Bknight.png')

	b_bishop1 = image.load('resources/chess-images/pieces/black/Bbishop.png')
	b_bishop2 = image.load('resources/chess-images/pieces/black/Bbishop.png')

	b_rook1 = image.load('resources/chess-images/pieces/black/Brook.png')
	b_rook2 = image.load('resources/chess-images/pieces/black/Brook.png')

	b_queen = image.load('resources/chess-images/pieces/black/Bqueen.png')
	b_king = image.load('resources/chess-images/pieces/black/Bking.png')


	screen.blit(w_pawn1, (piece_coordinates[0], piece_coordinates[6]))
	screen.blit(w_pawn2, (piece_coordinates[1], piece_coordinates[6]))
	screen.blit(w_pawn3, (piece_coordinates[2], piece_coordinates[6]))
	screen.blit(w_pawn4, (piece_coordinates[3], piece_coordinates[6]))
	screen.blit(w_pawn5, (piece_coordinates[4], piece_coordinates[6]))
	screen.blit(w_pawn6, (piece_coordinates[5], piece_coordinates[6]))
	screen.blit(w_pawn7, (piece_coordinates[6], piece_coordinates[6]))
	screen.blit(w_pawn8, (piece_coordinates[7], piece_coordinates[6]))

	screen.blit(w_rook1, 	(piece_coordinates[0], piece_coordinates[7]))
	screen.blit(w_knight1, 	(piece_coordinates[1], piece_coordinates[7]))
	screen.blit(w_bishop1, 	(piece_coordinates[2], piece_coordinates[7]))
	screen.blit(w_queen, 	(piece_coordinates[3], piece_coordinates[7]))
	screen.blit(w_king, 	(piece_coordinates[4], piece_coordinates[7]))
	screen.blit(w_bishop2, 	(piece_coordinates[5], piece_coordinates[7]))
	screen.blit(w_knight2, 	(piece_coordinates[6], piece_coordinates[7]))
	screen.blit(w_rook2, 	(piece_coordinates[7], piece_coordinates[7]))

	screen.blit(b_pawn1, (piece_coordinates[0], piece_coordinates[1]))
	screen.blit(b_pawn2, (piece_coordinates[1], piece_coordinates[1]))
	screen.blit(b_pawn3, (piece_coordinates[2], piece_coordinates[1]))
	screen.blit(b_pawn4, (piece_coordinates[3], piece_coordinates[1]))
	screen.blit(b_pawn5, (piece_coordinates[4], piece_coordinates[1]))
	screen.blit(b_pawn6, (piece_coordinates[5], piece_coordinates[1]))
	screen.blit(b_pawn7, (piece_coordinates[6], piece_coordinates[1]))
	screen.blit(b_pawn8, (piece_coordinates[7], piece_coordinates[1]))

	screen.blit(b_rook1, 	(piece_coordinates[0], piece_coordinates[0]))
	screen.blit(b_knight1, 	(piece_coordinates[1], piece_coordinates[0]))
	screen.blit(b_bishop1, 	(piece_coordinates[2], piece_coordinates[0]))
	screen.blit(b_queen, 	(piece_coordinates[3], piece_coordinates[0]))
	screen.blit(b_king, 	(piece_coordinates[4], piece_coordinates[0]))
	screen.blit(b_bishop2, 	(piece_coordinates[5], piece_coordinates[0]))
	screen.blit(b_knight2, 	(piece_coordinates[6], piece_coordinates[0]))
	screen.blit(b_rook2, 	(piece_coordinates[7], piece_coordinates[0]))
