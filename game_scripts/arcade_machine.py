from game_scripts.utilities import draw_button1
from game_scripts.tetris import draw_tetris_panels, draw_tetris_board, draw_tetris_menu, draw_tetris_pause, draw_piece
import sys
import time
import pygame
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ARCADE MACHINE')

# Colors
black = (0,0,0)

## MAIN LOOP ##
# This loop will display a screen with the name 'Arcade Machine' and a scroll of the games we can play, the games will include :
# 	- Tetris
# 	- Snake	
# 	- Pong 
# 	- Connect 4
# 	- Reaction
#	- Infection

# TODO
# 	- Add music and sound effects to the buttons
def arcade_machine_menu() :
	main_clock = pygame.time.Clock()

	rainbow_i = 0
	rainbow_array = [
	(255, 0, 0),(255, 64, 0),(255, 191, 0),(255, 255, 0),
	(191, 255, 0),(128, 255, 0),(64, 255, 0),(0, 255, 0),
	(0, 255, 64),(0, 255, 128),(0, 255, 191),(0, 255, 255),
	(0, 191, 255),(0, 128, 255),(0, 64, 255),(0, 0, 255),
	(64, 0, 255),(128, 0, 255),(191, 0, 255),(255, 0, 255),
	(255, 0, 191),(255, 0, 128),(255, 0, 64),(255, 0, 128),
	(255, 0, 191),(255, 0, 255),(191, 0, 255),(128, 0, 255),
	(64, 0, 255),(0, 0, 255),(0, 64, 255),(0, 128, 255),
	(0, 191, 255),(0, 255, 255),(0, 255, 191),(0, 255, 128),
	(0, 255, 64),(0, 255, 0),(64, 255, 0),(128, 255, 0),
	(191, 255, 0),(255, 255, 0),(255, 191, 0),(255, 64, 0)]
	title_font = pygame.font.Font('resources\\fonts\\main_fonts\\ARCADECLASSIC.TTF', 100)

	i_text_animation = 0

	button_width = 250
	button_height = 80

	l_column = 100
	r_column = 550
	row_1 = 250
	row_2 = 450
	row_3 = 650

	title_string 		= 'ARCADE   MACHINE'
	tetris_string 		= '   TETRIS'
	snake_string 		= '    SNAKE'
	pong_string 		= '     PONG'
	connect4_string 	= 'CONNECT 4'
	reaction_string 	= ' REACTION'
	infection_string 	= 'INFECTION'

	run = True

	while run:
		main_clock.tick(15)

		for event in pygame.event.get() :
		
			if event.type == pygame.QUIT :
				sys.exit()
		
		# SCREEN ELEMENTS :

		screen.fill(black)
		mouse = pygame.mouse.get_pos()

		# Title:
		rainbow_i += 1
		if rainbow_i > 42 : rainbow_i = 0
		title = title_font.render(title_string, True, rainbow_array[rainbow_i])
		screen.blit(title, (75,50))

		# Buttons:
		if i_text_animation < 9 : i_text_animation += 1
		if i_text_animation == 9 : i_text_animation = 0

		#tetris
		draw_button1(screen, l_column, row_1, tetris_string, mouse, i_text_animation)
		if (l_column <= mouse[0] <= l_column+button_width) and (row_1 <= mouse[1] <= row_1+button_height) :
			if event.type == pygame.MOUSEBUTTONDOWN : tetris_menu()
		
		#snake
		draw_button1(screen, l_column, row_2, snake_string, mouse, i_text_animation)
		if (l_column <= mouse[0] <= l_column+button_width) and (row_2 <= mouse[1] <= row_2+button_height) :
			if event.type == pygame.MOUSEBUTTONDOWN : print('NOT AVAILABLE')

		#pong
		draw_button1(screen, l_column, row_3, pong_string, mouse, i_text_animation)
		if (l_column <= mouse[0] <= l_column+button_width) and (row_3 <= mouse[1] <= row_3+button_height) :
			if event.type == pygame.MOUSEBUTTONDOWN : pong_game()

		#connect4
		draw_button1(screen, r_column, row_1, connect4_string, mouse, i_text_animation)
		if (r_column <= mouse[0] <= r_column+button_width) and (row_1 <= mouse[1] <= row_1+button_height) :
			if event.type == pygame.MOUSEBUTTONDOWN : print('NOT AVAILABLE')

		#reaction
		draw_button1(screen, r_column, row_2, reaction_string, mouse, i_text_animation)
		if (r_column <= mouse[0] <= r_column+button_width) and (row_2 <= mouse[1] <= row_2+button_height) :
			if event.type == pygame.MOUSEBUTTONDOWN : print('NOT AVAILABLE')

		#infection
		draw_button1(screen, r_column, row_3, infection_string, mouse, i_text_animation)
		if (r_column <= mouse[0] <= r_column+button_width) and (row_3 <= mouse[1] <= row_3+button_height) :
			if event.type == pygame.MOUSEBUTTONDOWN : print('NOT AVAILABLE')

		pygame.display.flip()

def pause_loop(game, in_game) :
	pause_clock = pygame.time.Clock()

	pause_menu_size = 350
	pause_menu_X = 275
	pause_menu_Y = 220

	resume_button_X = 325
	resume_button_Y = 300

	controls_button_X = 325
	controls_button_Y = 390

	quit_button_X = 325
	quit_button_Y = 480

	paused = True

	if game is 'TETRIS' :

		while paused:
			pause_clock.tick(30)
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():

					if event.type == pygame.QUIT:
						sys.exit()
					
					#KEYCONTROLS
					if event.type == pygame.KEYDOWN:
						keys_pressed = pygame.key.get_pressed()

						if keys_pressed[pygame.K_SPACE] : paused = False

						if keys_pressed[pygame.K_ESCAPE] : paused = False

					#MOUSECONTROLS
					if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
								if event.type == pygame.MOUSEBUTTONDOWN : paused = False
					
					if (resume_button_X <= mouse[0] <= resume_button_X+button_width) and (resume_button_Y <= mouse[1] <= resume_button_Y+button_height) :
						if event.type == pygame.MOUSEBUTTONDOWN : paused = False
					
					if (controls_button_X <= mouse[0] <= controls_button_X+button_width) and (controls_button_Y <= mouse[1] <= controls_button_Y+button_height) :
						if event.type == pygame.MOUSEBUTTONDOWN : pass #show_controls() 

					if (quit_button_X <= mouse[0] <= quit_button_X+button_width) and (quit_button_Y <= mouse[1] <= quit_button_Y+button_height) :
						if event.type == pygame.MOUSEBUTTONDOWN :
								if in_game == True : tetris_menu()
								if in_game == False : arcade_machine_menu()

			draw_tetris_pause(screen, mouse)

			pygame.display.flip()
		
		if game is 'PONG' :
			pass

############################################################## <TETRIS> ###############################################################


def tetris_menu() :
	menu_clock = pygame.time.Clock()
	pause = False
	play = False
	play_button_X = 325
	play_button_Y = 350
	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650
	run = True
	
	while run :
		menu_clock.tick(30)
		mouse = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				#KEYCONTROLS
				if event.type == pygame.KEYDOWN:
					keys_pressed = pygame.key.get_pressed()

					if keys_pressed[pygame.K_SPACE] : play = True
					if keys_pressed[pygame.K_ESCAPE] : 
							pause = True

				#MOUSECONTROLS
				if (play_button_X <= mouse[0] <= play_button_X+button_width) and (play_button_Y <= mouse[1] <= play_button_Y+button_height) :
					if event.type == pygame.MOUSEBUTTONDOWN : play = True

				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
					if event.type == pygame.MOUSEBUTTONDOWN : pause = True

		
		# SCREEN ELEMENTS

		# Background :
		screen.fill(black)

		# Panels :
		draw_tetris_panels(screen)
		draw_tetris_menu(screen, mouse)
		if pause : pause_loop(game='TETRIS', in_game=False)
		pause = False
		if play : tetris_game()

		pygame.display.flip()

def tetris_game() :
	game_clock = pygame.time.Clock()
	fall = 0
	pause = False
	fall_timer = 1  #1 second
	elapsed_time = 0
	start_time = time.time()
	piece_rotation = 0
	piece_x = 0
	run = True

	while run :
		game_clock.tick(30)
		mouse = pygame.mouse.get_pos()

		# TIMER for the pieces falling
		elapsed_time = time.time() - start_time
		if elapsed_time > fall_timer : 
			fall += 1
			elapsed_time = 0
			start_time = time.time()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				
				#KEYCONTROLS
				if event.type == pygame.KEYDOWN:
					keys_pressed = pygame.key.get_pressed()

					if keys_pressed[pygame.K_ESCAPE] : pause = True

					if keys_pressed[pygame.K_UP] : piece_rotation += 1 
					if keys_pressed[pygame.K_DOWN] : fall += 1
					if keys_pressed[pygame.K_LEFT] : piece_x -= 1
					if keys_pressed[pygame.K_RIGHT] : piece_x += 1


				#MOUSECONTROLS
				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
					if event.type == pygame.MOUSEBUTTONDOWN : pause = True

		# SCREEN ELEMENTS :

		#	- Background :
		screen.fill(black)

		#	- Panels :
		draw_tetris_panels(screen)

		#	- Game :
		if pause : pause_loop(game='TETRIS', in_game=True)
		pause = False
		draw_piece(screen, 1, piece_x, piece_rotation, fall)

		draw_tetris_board(screen)
		pygame.display.flip()


############################################################## </TETRIS> ##############################################################

############################################################## <PONG> #################################################################


def pong_menu() :
	pass

def pong_game() :
	pong_clock = pygame.time.Clock()
	game_area_height = 580
	game_area_width = 900
	ball = pygame.Rect(game_area_width/2-10, game_area_height/2-10, 20, 20)
	player1 = pygame.Rect(5, game_area_height/2-35, 5, 70)
	player2 = pygame.Rect(game_area_width-5, game_area_height/2-35, 5, 70)
	run = True

	while run :
		pong_clock.tick(60)

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

def pong_pause(in_game) :
	pass


############################################################## </PONG> ################################################################