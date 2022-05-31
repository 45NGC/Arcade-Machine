from game_scripts.utilities import draw_button1
from game_scripts.tetris import draw_next_pieces, draw_tetris_panels, draw_tetris_board, draw_tetris_menu, draw_tetris_pause
from game_scripts.tetris import PIECES, get_piece, get_empty_board, is_valid_position, add_piece_to_board, draw_board_blocks, draw_piece
from game_scripts.pong import draw_pong_menu, draw_pong_pause_button, draw_pong_pause_menu
import sys
import time
import random
import pygame
pygame.init()

# Create screen
screen_size = (900,850)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('ARCADE MACHINE')

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
	title_font = pygame.font.Font('resources\\fonts\\ARCADECLASSIC.TTF', 100)

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

		screen.fill((0,0,0))
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
			if event.type == pygame.MOUSEBUTTONDOWN : pong_menu()

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


############################################################## <TETRIS> ###############################################################


def tetris_menu() :
	menu_clock = pygame.time.Clock()
	pause = False
	play = False
	button_width = 250
	button_height = 80
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

					if keys_pressed[pygame.K_SPACE] : tetris_game0()
					if keys_pressed[pygame.K_ESCAPE] : tetris_pause(in_game=False)

				#MOUSECONTROLS
				if (play_button_X <= mouse[0] <= play_button_X+button_width) and (play_button_Y <= mouse[1] <= play_button_Y+button_height) :
					if event.type == pygame.MOUSEBUTTONDOWN : tetris_game0()

				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
					if event.type == pygame.MOUSEBUTTONDOWN : tetris_pause(in_game=False)

		
		# SCREEN ELEMENTS

		screen.fill((0,0,0))

		# Panels :
		draw_tetris_panels(screen)
		draw_tetris_menu(screen, mouse)

		pygame.display.flip()


def tetris_game0():
	game_clock = pygame.time.Clock()
	board = get_empty_board()
	fall_timer = time.time()
	moving_down = False
	moving_left = False
	moving_right = False
	score = 0
	fall = 0.27
	current_piece = get_piece()
	next_piece1 = None
	next_piece2 = get_piece()

	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650

	run = True
	end = False

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

			if not is_valid_position(board, current_piece):
				end = True
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			#MOUSECONTROLS
			if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
				if event.type == pygame.MOUSEBUTTONDOWN : tetris_pause(in_game=True)
			
			# KEYCONTROLS
			if event.type == pygame.KEYUP:
				if (event.key == pygame.K_LEFT) : 
					moving_left = False
				elif (event.key == pygame.K_RIGHT): 
					moving_right = False
				elif (event.key == pygame.K_DOWN): 
					moving_down = False

			elif event.type == pygame.KEYDOWN:
				# pause
				if event.key == pygame.K_ESCAPE :
					tetris_pause(in_game=True)
					fall_timer = time.time()

				# move the piece sideways
				if event.key == pygame.K_LEFT and is_valid_position(board, current_piece, ad_X=-1):
					current_piece['x'] -= 1
					moving_left = True
					moving_right = False
				elif event.key == pygame.K_RIGHT and is_valid_position(board, current_piece, ad_X=1):
					current_piece['x'] += 1
					moving_right = True
					moving_left = False

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
					moving_down = False
					moving_left = False
					moving_right = False
					for i in range(1, 20):
						if not is_valid_position(board, current_piece, ad_Y=i):
							break
					current_piece['y'] += i - 1
		
		if moving_left and is_valid_position(board, current_piece, ad_X=-1):
			current_piece['x'] -= 1
		elif moving_right and is_valid_position(board, current_piece, ad_X=1):
			current_piece['x'] += 1
		if moving_down and is_valid_position(board, current_piece, ad_Y=1):
			current_piece['y'] += 1
		
		if time.time() - fall_timer > fall:
            # check if the piece has avaiable space
			if not is_valid_position(board, current_piece, ad_Y=1):
				add_piece_to_board(board, current_piece)
				current_piece = None
			else:
				# if the piece has space it continues to fall down
				current_piece['y'] += 1
				fall_timer = time.time()
		
		

		# SCREEN ELEMENTS :

		screen.fill((0,0,0))

		# Panels :
		draw_tetris_panels(screen)

		# Game :
		draw_board_blocks(screen, board)
		draw_next_pieces(screen, next_piece1, next_piece2)

		# Draw current piece
		if current_piece != None: draw_piece(screen, current_piece)
		draw_tetris_board(screen)
		
		pygame.display.flip()




def tetris_game() :
	game_clock = pygame.time.Clock()
	fall = 0
	pause_button_size = 100
	pause_button_X = 725
	pause_button_Y = 650
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

					if keys_pressed[pygame.K_ESCAPE] : tetris_pause(in_game=True)

					if keys_pressed[pygame.K_UP] : piece_rotation += 1 
					if keys_pressed[pygame.K_DOWN] : fall += 1
					if keys_pressed[pygame.K_LEFT] : piece_x -= 1
					if keys_pressed[pygame.K_RIGHT] : piece_x += 1


				#MOUSECONTROLS
				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
					if event.type == pygame.MOUSEBUTTONDOWN : tetris_pause(in_game=True)

		# SCREEN ELEMENTS :

		screen.fill((0,0,0))

		# Panels :
		draw_tetris_panels(screen)

		# Game :
		#draw_piece(screen, 1, piece_x, piece_rotation, fall)

		draw_tetris_board(screen)
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
							if in_game == False : arcade_machine_menu()

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
					if in_game  == False : arcade_machine_menu()
			
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
	score_font = pygame.font.Font('resources\\fonts\\Gameplay.ttf', 25)

	# BALL
	ball_start = True
	ball = pygame.Rect(game_area_width/2-10, 150+game_area_height/2-10, 20, 20)
	ball_speed_x = 4
	ball_speed_y = 4

	# TIMER
	timer1 = pygame.time.get_ticks()
	timer2 = 0
	timer_font = pygame.font.Font('resources\\fonts\\Gameplay.ttf', 35)

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