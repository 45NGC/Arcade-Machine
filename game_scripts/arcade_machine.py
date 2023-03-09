from game_scripts.utilities import draw_button1, draw_button2, draw_text_input
from game_scripts.tetris import draw_ui_pieces, draw_tetris_panels, draw_tetris_board, draw_tetris_menu, draw_tetris_pause, draw_tetris_game_over
from game_scripts.tetris import PIECES, get_piece, get_empty_board, is_valid_position, add_piece_to_board, draw_board_blocks, draw_piece, remove_complete_lines
from game_scripts.pong import draw_pong_menu, draw_pong_pause_button, draw_pong_pause_menu
from game_scripts.chess import draw_chess_menu, draw_chess_pieces
from game_scripts.data import *
import sys
import time
import random
import nums_from_string
import pygame
from pygame import image
pygame.init()

# Create screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 850
screen_size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('ARCADE MACHINE')
USER = None



# User register/login
def arcade_machine_register_login():
	clock = pygame.time.Clock()
	global USER_NAME
	register_string = 'REGISTER'
	login_string = 'LOGIN'
	user_name_string = 'NICKNAME'
	password_string = 'PASSWORD'
	font = pygame.font.Font('resources/fonts/Gameplay.ttf', 20)

	user_name_label = font.render(user_name_string, True, (255,255,255))
	password_label = font.render(password_string, True, (255,255,255))

	input_user_name_active = False
	input_password_active = False
	input_user_name = ''
	input_password = ''

	run = True

	while run :
		clock.tick(60)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			# KEYCONTROLS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					if input_user_name_active : input_user_name = input_user_name[:-1]
					if input_password_active : input_password = input_password[:-1]
				else:
					if input_user_name_active and len(input_user_name) < 25 : input_user_name += event.unicode
					if input_password_active and len(input_password) < 25 : input_password += event.unicode
			
			# MOUSECONTROLS
			if (350 <= mouse[0] <= 750) and (300 <= mouse[1] <= 370) : # input_user_name
				if event.type == pygame.MOUSEBUTTONDOWN :
					input_user_name_active = True
					input_password_active = False

			elif (150 <= mouse[0] <= 550) and (450 <= mouse[1] <= 520) : # input_password
				if event.type == pygame.MOUSEBUTTONDOWN :
					input_user_name_active = False
					input_password_active = True

			elif (150 <= mouse[0] <= 400) and (650 <= mouse[1] <= 730) : # register_button
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(get_user_name(input_user_name)) != 0 :
						print('USER ALREADY EXISTS')
					else : 
						add_user(input_user_name, input_password)
						arcade_machine_menu(input_user_name)

			elif (500 <= mouse[0] <= 650) and (650 <= mouse[1] <= 730) : # login_button
				if event.type == pygame.MOUSEBUTTONDOWN:
					if len(get_user_name(input_user_name)) == 0 :
						print('USER DOES NOT EXIST')
					else : 
						user_password = str((get_user_password(input_user_name)))
						formated_input = "[('"+str(input_password)+"',)]"

						if user_password == formated_input:
							arcade_machine_menu(input_user_name)
						else :
							print('INCORRECT PASSWORD')

			elif event.type ==  pygame.MOUSEBUTTONDOWN :
				input_password_active = False
				input_user_name_active = False


		# SCREEN ELEMENTS
		screen.fill((0,0,0))

		screen.blit(user_name_label, (150,325))
		screen.blit(password_label, (150,475))

		draw_text_input(screen, 350, 300, input_user_name_active)
		draw_text_input(screen, 350, 450, input_password_active)

		user_name = font.render(input_user_name, True, (255,255,255))
		password = font.render(input_password, True, (255,255,255))
		screen.blit(user_name, (360,325))
		screen.blit(password, (360,475))

		draw_button2(screen, 150, 650, register_string, mouse)
		draw_button2(screen, 500, 650, login_string, mouse)
		
		pygame.display.flip()

## MAIN LOOP ##
# This loop will display a screen with the name 'Arcade Machine' and 6 buttons of the avaiable games :
# 	- Tetris
# 	- Snake	
# 	- Pong 
# 	- Connect 4
# 	- Reaction
#	- Infection

# TODO
# 	- Add music and sound effects to the buttons
def arcade_machine_menu(user_name) :
	global USER
	USER = user_name

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
	title_font = pygame.font.Font('resources/fonts/ARCADECLASSIC.TTF', 100)

	i_text_animation = 0

	button_width = 244
	button_height = 74

	l_column = 105
	r_column = 555
	row_1 = 255
	row_2 = 455
	row_3 = 655

	title_string 		= 'ARCADE   MACHINE'
	tetris_string 		= '   TETRIS'
	chess_string 		= '    CHESS'
	pong_string 		= '     PONG'
	connect4_string 	= 'CONNECT 4'
	reaction_string 	= ' REACTION'
	infection_string 	= 'INFECTION'

	run = True

	while run:
		main_clock.tick(15)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get() :
		
			if event.type == pygame.QUIT :
				sys.exit()

			if (l_column <= mouse[0] <= l_column+button_width) and (row_1 <= mouse[1] <= row_1+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : tetris_menu()
			
			if (l_column <= mouse[0] <= l_column+button_width) and (row_2 <= mouse[1] <= row_2+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : chess_menu()
		
			if (l_column <= mouse[0] <= l_column+button_width) and (row_3 <= mouse[1] <= row_3+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : pong_menu()

			if (r_column <= mouse[0] <= r_column+button_width) and (row_1 <= mouse[1] <= row_1+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : print('NOT AVAILABLE')

			if (r_column <= mouse[0] <= r_column+button_width) and (row_2 <= mouse[1] <= row_2+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : print('NOT AVAILABLE')

			if (r_column <= mouse[0] <= r_column+button_width) and (row_3 <= mouse[1] <= row_3+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : print('NOT AVAILABLE')

		# SCREEN ELEMENTS :

		screen.fill((0,0,0))

		# Title:
		rainbow_i += 1
		if rainbow_i > 42 : rainbow_i = 0
		title = title_font.render(title_string, True, rainbow_array[rainbow_i])
		screen.blit(title, (75,50))

		# Buttons:
		if i_text_animation < 9 : i_text_animation += 1
		if i_text_animation == 9 : i_text_animation = 0

		
		draw_button1(screen, l_column, row_1, tetris_string, mouse, i_text_animation) #tetris
		draw_button1(screen, l_column, row_2, chess_string, mouse, i_text_animation) #snake
		draw_button1(screen, l_column, row_3, pong_string, mouse, i_text_animation) #pong
		draw_button1(screen, r_column, row_1, connect4_string, mouse, i_text_animation) #connect4
		draw_button1(screen, r_column, row_2, reaction_string, mouse, i_text_animation) #reaction
		draw_button1(screen, r_column, row_3, infection_string, mouse, i_text_animation) #infection

		pygame.display.flip()


############################################################## <TETRIS> ###############################################################


def tetris_menu() :
	menu_clock = pygame.time.Clock()
	button_width = 250
	button_height = 80
	play_button_X = 325
	play_button_Y = 350
	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650
	run = True

	record_1_string = str(nums_from_string.get_nums(str(get_tetris_record1(USER)))[0])
	record_2_string = str(nums_from_string.get_nums(str(get_tetris_record2(USER)))[0])
	record_3_string = str(nums_from_string.get_nums(str(get_tetris_record3(USER)))[0])
	record_4_string = str(nums_from_string.get_nums(str(get_tetris_record4(USER)))[0])
	record_5_string = str(nums_from_string.get_nums(str(get_tetris_record5(USER)))[0])
	
	while run :
		menu_clock.tick(30)
		mouse = pygame.mouse.get_pos()
		
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				#KEYCONTROLS
				if event.type == pygame.KEYDOWN:
					keys_pressed = pygame.key.get_pressed()

					if keys_pressed[pygame.K_SPACE] : tetris_game()
					if keys_pressed[pygame.K_ESCAPE] : tetris_pause(in_game=False)

				#MOUSECONTROLS
				if (play_button_X <= mouse[0] <= play_button_X+button_width) and (play_button_Y <= mouse[1] <= play_button_Y+button_height) :
					if event.type == pygame.MOUSEBUTTONDOWN : tetris_game()

				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
					if event.type == pygame.MOUSEBUTTONDOWN : tetris_pause(in_game=False)

		
		# SCREEN ELEMENTS

		screen.fill((0,0,0))

		# Panels :
		draw_tetris_panels(screen)
		draw_tetris_menu(screen, mouse, record_1_string, record_2_string, record_3_string, record_4_string, record_5_string)

		pygame.display.flip()

def tetris_game():
	game_clock = pygame.time.Clock()
	board = get_empty_board()
	fall_timer = time.time()
	moving_down = False
	score = 0
	lines = 0
	fall = 0.35

	current_piece = get_piece()
	next_piece1 = None
	next_piece2 = get_piece()
	hold_piece = None

	hold_chance = True
	hold_aux = None

	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650

	run = True

	while run :
		game_clock.tick(25)
		mouse = pygame.mouse.get_pos()

		if next_piece1 == None : 
			next_piece1 = next_piece2
			next_piece2 = None
		
		if next_piece2 == None : next_piece2 = get_piece()

		if current_piece == None :
			current_piece = next_piece1
			next_piece1 = None
			fall_timer = time.time()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			#MOUSECONTROLS
			if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
				if event.type == pygame.MOUSEBUTTONDOWN : tetris_pause(in_game=True)
			
			# KEYCONTROLS
			if event.type == pygame.KEYUP:
				if (event.key == pygame.K_DOWN) : 
					moving_down = False

			elif event.type == pygame.KEYDOWN:
				# pause
				if event.key == pygame.K_ESCAPE :
					tetris_pause(in_game=True)
					fall_timer = time.time()

				# move the piece sideways
				if event.key == pygame.K_LEFT and is_valid_position(board, current_piece, ad_X=-1):
					current_piece['x'] -= 1
				elif event.key == pygame.K_RIGHT and is_valid_position(board, current_piece, ad_X=1):
					current_piece['x'] += 1

				# rotate piece
				elif event.key == pygame.K_UP:
					current_piece['rotation'] = (current_piece['rotation'] + 1) % len(PIECES[current_piece['shape']])
					if not is_valid_position(board, current_piece):
						current_piece['rotation'] = (current_piece['rotation'] - 1) % len(PIECES[current_piece['shape']])

				# move piece down
				elif event.key == pygame.K_DOWN:
					moving_down = True
					if is_valid_position(board, current_piece, ad_Y=1):
						current_piece['y'] += 1

				# move the current piece all the way down
				elif event.key == pygame.K_SPACE:
					for i in range(1, 20):
						if not is_valid_position(board, current_piece, ad_Y=i):
							break
					current_piece['y'] += i - 1

				elif event.key == pygame.K_c:
					if hold_chance == True:
						if hold_piece == None  :
							hold_piece = current_piece
							current_piece = None
							hold_chance = False
						else:
							hold_aux = hold_piece
							hold_piece = current_piece
							current_piece = hold_aux
							current_piece['y'] = -4
							current_piece['x'] = 3
							hold_chance = False


		
		if moving_down and is_valid_position(board, current_piece, ad_Y=1):
			current_piece['y'] += 1
		
		if time.time() - fall_timer > fall:
            # check if the piece has avaiable space
			if not is_valid_position(board, current_piece, ad_Y=1):
				if current_piece['y'] < -1: 
					tetris_game_over(score)
				else:
					add_piece_to_board(board, current_piece)
					update_score_lines = remove_complete_lines(board)
					score += update_score_lines[0]
					lines += update_score_lines[1]
					hold_chance = True
					current_piece = None
			else:
				# if the piece has space it continues to fall down
				current_piece['y'] += 1
				#print('piece x  ->'+str(current_piece['x']))
				#print('piece y  ->'+str(current_piece['y']))
				fall_timer = time.time()
		
		# The fall speed will depend on how many lines the player has completed
		#print(str(lines))
		#print(str(fall))
		if 10 <= lines < 20:
			fall = 0.3
		elif 20 <= lines < 30:
			fall = 0.25
		elif 30 <= lines < 40:
			fall = 0.2
		elif 40 <= lines < 50:
			fall = 0.15
		elif 50 <= lines < 60:
			fall = 0.1
		elif 60 <= lines < 70:
			fall = 0.05
		elif 70 <= lines < 80:
			fall = 0.03
		elif 80 <= lines < 90:
			fall = 0.02
		elif lines >= 90:
			fall = 0.01

		# SCREEN ELEMENTS :

		screen.fill((0,0,0))

		# Panels :
		draw_tetris_panels(screen, score, lines)

		# Game :
		draw_board_blocks(screen, board)
		draw_ui_pieces(screen, next_piece1, next_piece2, hold_piece)

		# Draw current piece
		if current_piece != None: draw_piece(screen, current_piece)
		draw_tetris_board(screen)
		
		pygame.display.flip()

def tetris_game_over(score):
	game_over_clock = pygame.time.Clock()
	game_score = score

	button_width = 250
	button_height = 80

	restart_button_X = 180
	restart_button_Y = 470
	quit_button_X = 470
	quit_button_Y = 470

	record_1_string = str(nums_from_string.get_nums(str(get_tetris_record1(USER)))[0])
	record_2_string = str(nums_from_string.get_nums(str(get_tetris_record2(USER)))[0])
	record_3_string = str(nums_from_string.get_nums(str(get_tetris_record3(USER)))[0])
	record_4_string = str(nums_from_string.get_nums(str(get_tetris_record4(USER)))[0])
	record_5_string = str(nums_from_string.get_nums(str(get_tetris_record5(USER)))[0])

	if score > int(record_1_string) : 
		update_tetris_records(score, 1)
		score = int(record_1_string)

	if score > int(record_2_string) : 
		update_tetris_records(score, 2)
		score = int(record_2_string)

	if score > int(record_3_string) : 
		update_tetris_records(score, 3)
		score = int(record_3_string)

	if score > int(record_4_string) : 
		update_tetris_records(score, 4)
		score = int(record_4_string)

	if score > int(record_5_string) : 
		update_tetris_records(score, 5)

	game_over = True

	while game_over:
		game_over_clock.tick(30)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()

			# KEYCONTROLS
			if event.type == pygame.KEYDOWN:
				keys_pressed = pygame.key.get_pressed()

				if keys_pressed[pygame.K_SPACE] : tetris_game()
				if keys_pressed[pygame.K_ESCAPE] : tetris_menu()

			#MOUSECONTROLS
			if (restart_button_X <= mouse[0] <= restart_button_X+button_width) and (restart_button_Y <= mouse[1] <= restart_button_Y+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : tetris_game()

			if (quit_button_X <= mouse[0] <= quit_button_X+button_width) and (quit_button_Y <= mouse[1] <= quit_button_Y+button_height) :
				if event.type == pygame.MOUSEBUTTONDOWN : tetris_menu()
		
		draw_tetris_game_over(screen, mouse, game_score)
		pygame.display.flip()

def tetris_pause(in_game) :
	pause_clock = pygame.time.Clock()

	button_width = 250
	button_height = 80

	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650

	resume_button_X = 325
	resume_button_Y = 300

	controls_button_X = 325
	controls_button_Y = 390

	quit_button_X = 325
	quit_button_Y = 480

	paused = True

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
							if in_game == False : arcade_machine_menu(USER)

		draw_tetris_pause(screen, mouse)

		pygame.display.flip()


############################################################## </TETRIS> ##############################################################

############################################################## <PONG> #################################################################


def pong_menu() :
	# 3 GAME MODES :
	# - 1 vs 1
	# - 1 vs IA 
	# - Practise (1 vs wall)
	menu_clock = pygame.time.Clock()
	vsIA_button_X = 70
	vsIA_button_Y = 330
	vs1_button_X = 580
	vs1_button_Y = 330
	practise_button_X = 325
	practise_button_Y = 570
	pause_button_X = 425
	pause_button_Y = 770
	run = True

	while run :
		menu_clock.tick(30)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			
			#MOUSECONTROLS
			if (pause_button_X <= mouse[0] <= pause_button_X+50) and (pause_button_Y <= mouse[1] <= pause_button_Y+50) :
				if event.type == pygame.MOUSEBUTTONDOWN : pong_pause(in_game=False)

			if (vsIA_button_X <= mouse[0] <= vsIA_button_X+250) and (vsIA_button_Y <= mouse[1] <= vsIA_button_Y+80) :
				if event.type == pygame.MOUSEBUTTONDOWN : pong_game(game_mode = 1)
			
			if (vs1_button_X <= mouse[0] <= vs1_button_X+250) and (vs1_button_Y <= mouse[1] <= vs1_button_Y+80) :
				if event.type == pygame.MOUSEBUTTONDOWN : pong_game(game_mode = 2)
			
			if (practise_button_X <= mouse[0] <= practise_button_X+250) and (practise_button_Y <= mouse[1] <= practise_button_Y+80) :
				if event.type == pygame.MOUSEBUTTONDOWN : pong_game(game_mode = 3)
			
			#KEYCONTROLS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE : pong_pause(in_game=False)

		
		# SCREEN ELEMENTS
		screen.fill((0,0,0))
		draw_pong_menu(screen, mouse)
		draw_pong_pause_button(screen)

		pygame.display.flip()

def pong_circumstantial_menus(menu) :
	pass

def pong_pause(in_game) :
	pause_clock = pygame.time.Clock()
	pause_button_X = 425
	pause_button_Y = 770

	resume_button_X = 325
	resume_button_Y = 300
	controls_button_X = 325
	controls_button_Y = 390
	quit_button_X = 325
	quit_button_Y = 480

	paused = True

	while paused :
		pause_clock.tick(30)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			
			#MOUSECONTROLS
			if (pause_button_X <= mouse[0] <= pause_button_X+50) and (pause_button_Y <= mouse[1] <= pause_button_Y+50) :
				if event.type == pygame.MOUSEBUTTONDOWN : paused = False
			if (resume_button_X <= mouse[0] <= resume_button_X+250) and (resume_button_Y <= mouse[1] <= resume_button_Y+80) :
				if event.type == pygame.MOUSEBUTTONDOWN : paused = False
			if (controls_button_X <= mouse[0] <= controls_button_X+250) and (pause_button_Y <= mouse[1] <= controls_button_Y+80) :
				if event.type == pygame.MOUSEBUTTONDOWN : pass #show controls
			if (quit_button_X <= mouse[0] <= pause_button_X+250) and (quit_button_Y <= mouse[1] <= quit_button_Y+80) :
				if event.type == pygame.MOUSEBUTTONDOWN :
					if in_game  == True : pong_menu()
					if in_game  == False : arcade_machine_menu(USER)
			
			#KEYCONTROLS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE : paused = False
				if event.key == pygame.K_SPACE : paused = False

		draw_pong_pause_menu(screen, mouse)
		pygame.display.flip()

def pong_game(game_mode) :
	pong_clock = pygame.time.Clock()
	game_area_width = 900
	game_area_height = 580

	# COLORS
	white = (255,255,255)
	light_grey = (100,100,100)
	pink = (255, 153, 255)

	# LINES
	line_up = pygame.Rect(0, 149, game_area_width, 1)
	line_down = pygame.Rect(0, 150+game_area_height, game_area_width, 1)
	line_right = pygame.Rect(899, 150, 1, game_area_height)

	# PLAYERS
	player1 = pygame.Rect(5, 150+game_area_height/2-35, 5, 70)
	player2 = pygame.Rect(game_area_width-10, 150+game_area_height/2-35, 5, 70)
	player1_speed = 0
	player2_speed = 0
	ia_speed = 6

	player1_score = 0
	player2_score = 0
	score_font = pygame.font.Font('resources/fonts/Gameplay.ttf', 25)

	# BALL
	ball_start = True
	ball = pygame.Rect(game_area_width/2-10, 150+game_area_height/2-10, 20, 20)
	ball_speed_x = 4
	ball_speed_y = 4

	# TIMER
	timer1 = pygame.time.get_ticks()
	timer2 = 0
	timer_font = pygame.font.Font('resources/fonts/Gameplay.ttf', 35)

	# PAUSE BUTTON
	pause_button_X = 425
	pause_button_Y = 770

	run = True

	while run :
		pong_clock.tick(60)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			#MOUSECONTROLS
			if (pause_button_X <= mouse[0] <= pause_button_X+50) and (pause_button_Y <= mouse[1] <= pause_button_Y+50) :
				if event.type == pygame.MOUSEBUTTONDOWN :
					pause = True
					pong_pause(in_game=True)
			
			#KEYCONTROLS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE : pong_pause(in_game=True)

				if event.key == pygame.K_LSHIFT : player1_speed -= 3
				if event.key == pygame.K_LCTRL : player1_speed += 3

				if game_mode == 2 :
					if event.key == pygame.K_UP : player2_speed -= 3
					if event.key == pygame.K_DOWN : player2_speed += 3

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LSHIFT : player1_speed += 3
				if event.key == pygame.K_LCTRL : player1_speed -= 3

				if game_mode == 2 :
					if event.key == pygame.K_UP : player2_speed += 3
					if event.key == pygame.K_DOWN : player2_speed -= 3

		
		# SCREEN ELEMENTS :
		screen.fill((0,0,0))

		# Game area
		pygame.draw.rect(screen, white, line_up)
		pygame.draw.rect(screen, white, line_down)
		pygame.draw.aaline(screen, light_grey, (game_area_width/2,150), (game_area_width/2,150+game_area_height))
		if game_mode != 3 : pygame.draw.aaline(screen, white, (game_area_width/2-10, 100), (game_area_width/2+10, 100))
		if game_mode == 3 : pygame.draw.rect(screen, white, line_right)


		# Players
		pygame.draw.rect(screen, white, player1)
		if game_mode != 3 : pygame.draw.rect(screen, white, player2)

		# players speed
		player1.y += player1_speed
		if game_mode == 2 : player2.y += player2_speed

		# ia
		if game_mode == 1 :
			if player2.top < ball.y :
				player2.top += ia_speed
			if player2.top > ball.y :
				player2.top -= ia_speed
		
		# player movement limitation
		if player1.y < 150 : player1.y = 150
		if player1.y > 150+game_area_height-70 : player1.y = 150+game_area_height-70
		if player2.y < 150 : player2.y = 150
		if player2.y > 150+game_area_height-70 : player2.y = 150+game_area_height-70

		# score text
		player1_score_text = score_font.render(str(player1_score), True, white)
		player2_score_text = score_font.render(str(player2_score), True, white)

		if game_mode == 3 :
			player1_score_text = score_font.render(str(player1_score), True, white)
			screen.blit(player1_score_text, (50, 85))
		else:
			if player1_score > 9 :
				screen.blit(player1_score_text, (game_area_width/2-70, 85))
			else:
				screen.blit(player1_score_text, (game_area_width/2-60, 85))
			screen.blit(player2_score_text, (game_area_width/2+40, 85))

		# Ball
		pygame.draw.ellipse(screen, pink, ball)

		ball.x += ball_speed_x
		ball.y += ball_speed_y

		# Collisions

		# top limit collision
		if ball.top <= 150 and ball_speed_y < 0 : 
			ball_speed_y *= -1
		
		# bottom limit collision
		if ball.bottom >= 150+game_area_height and ball_speed_y > 0 :
			ball_speed_y *= -1 

		# player1 collision
		if ball.colliderect(player1) and ball_speed_x < 0 :
			print('1 ball speed x -> '+str(ball_speed_x))
			print('1 ball speed y -> '+str(ball_speed_y))

			if abs(ball.left - player1.right) < 5 :
				ball_speed_x *= -1
			elif abs(ball.bottom - player1.top) < 10 and ball_speed_y > 0 :
				ball_speed_y *= -1
			elif abs(ball.top - player1.bottom) < 10 and ball_speed_y < 0 :
				ball_speed_y *= -1

			if ball_speed_y < 0 : ball_speed_y -= 0.5
			if ball_speed_y > 0 : ball_speed_y += 0.5
			if ball_speed_y > 8 : ball_speed_y = 8
			if ball_speed_y < -8 : ball_speed_y = -8

		if game_mode == 3 :
			# right limit collision
			if ball.colliderect(line_right) : ball_speed_x *= -1
			if ball.colliderect(player1) : player1_score += 1
		else:
			# player2 collision
			if ball.colliderect(player2) and ball_speed_x > 0 :
				print('2 ball speed x -> '+str(ball_speed_x))
				print('2 ball speed y -> '+str(ball_speed_y))

				if abs(ball.right - player2.left) < 5 :
					ball_speed_x *= -1
				elif abs(ball.bottom - player2.top) < 10 and ball_speed_y > 0 :
					ball_speed_y *= -1
				elif abs(ball.top - player2.bottom) < 10 and ball_speed_y < 0 :
					ball_speed_y *= -1
				
				if ball_speed_y < 0 : ball_speed_y -= 0.5
				if ball_speed_y > 0 : ball_speed_y += 0.5
				if ball_speed_y > 8 : ball_speed_y = 8
				if ball_speed_y < -8 : ball_speed_y = -8


		# Score
		if ball.left > game_area_width : 
			player1_score += 1
			timer1 = pygame.time.get_ticks()
			ball_start = True
			
		if ball.right < 0 : 
			player2_score += 1
			timer1 = pygame.time.get_ticks()
			ball_start = True

		# Restart ball
		if ball_start :
			timer2 = pygame.time.get_ticks()
			ball.center = (game_area_width/2, 150+game_area_height/2)

			if timer2 - timer1 < 4000 :
				ball_speed_x = 0
				ball_speed_y = 0
			else :
				ball_speed_x = 4 * random.choice((1,-1))
				ball_speed_y = 4 * random.choice((1,-1))
				ball_start = False

			if timer2 - timer1 < 1000 :
				three = timer_font.render('3', True, white)
				screen.blit(three,(game_area_width/2-10, 30))
			if 1000 < timer2 - timer1 < 2000 :
				two = timer_font.render('2', True, white)
				screen.blit(two,(game_area_width/2-10, 30))
			if 2000 < timer2 - timer1 < 3000 :
				one = timer_font.render('1', True, white)
				screen.blit(one,(game_area_width/2-10, 30))
		
		# Pause button
		draw_pong_pause_button(screen)

		pygame.display.flip()

############################################################## </PONG> ################################################################

############################################################## <CHESS> #################################################################


def chess_menu():
	menu_clock = pygame.time.Clock()
	play_button_X = 330
	play_button_Y = 330
	run = True

	while run :
		menu_clock.tick(30)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			
			#MOUSECONTROLS
			if (play_button_X <= mouse[0] <= play_button_X+250) and (play_button_Y <= mouse[1] <= play_button_Y+80) :
				if event.type == pygame.MOUSEBUTTONDOWN : chess_game()
		

		screen.fill((0,0,0))
		draw_chess_menu(screen, mouse)
		pygame.display.flip()


def chess_game():
	game_clock = pygame.time.Clock()
	play_button_X = 50
	play_button_Y = 50
	board = image.load('resources/chess-images/medium-board.png')
	run = True

	while run :
		game_clock.tick(30)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			
			#MOUSECONTROLS
			# if (play_button_X <= mouse[0] <= play_button_X+50) and (play_button_X <= mouse[1] <= play_button_X+50) :
			# 	if event.type == pygame.MOUSEBUTTONDOWN : chess_game()

		screen.fill((40,40,40))
		screen.blit(board, (50,50))
		draw_chess_pieces(screen, mouse)
		pygame.display.flip()



############################################################## </CHESS> ################################################################
