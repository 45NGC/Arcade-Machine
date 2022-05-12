from game_scripts.utilities import draw_button
from game_scripts.tetris import draw_tetris_panels, draw_tetris_menu, draw_tetris_pause
import sys
import pygame
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ARCADE MACHINE')

# COLORS 
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
red_pink = (255, 0, 102)
dark_grey = (40,40,40)
grey = (60,60,60)
light_grey = (100,100,100)
yellow = (255,204,0)
green = (51,204,51)
dark_purple = (83,0,185)
purple = (153,0,255)
dark_pink = (255,53,155)
orange = (255, 153, 0)
red = (255, 57, 57)
blue = (0, 64, 255)
turquoise = (0, 255, 255)

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
	(191, 255, 0),(255, 255, 0),(255, 191, 0),(255, 64, 0)
]

# FONTS
title_font = pygame.font.Font('resources\\fonts\\main_fonts\\ARCADECLASSIC.TTF', 100)
text_animation_array = [0,1,2,3,4,5,4,3,2,1]

# STRINGS

# Main strings
title_string 		= 'ARCADE   MACHINE'
tetris_string 		= '   TETRIS'
snake_string 		= '    SNAKE'
pong_string 		= '     PONG'
connect4_string 	= 'CONNECT 4'
reaction_string 	= ' REACTION'
infection_string 	= 'INFECTION'

# Buttons
button_width = 250
button_height = 80

play_button_X = 325
play_button_Y = 350

pause_button_size = 100
pause_button_X = 725
pause_button_Y = 650

pause_menu_size = 350
pause_menu_X = 275
pause_menu_Y = 220

resume_button_X = 325
resume_button_Y = 300
controls_button_X = 325
controls_button_Y = 390
quit_button_X = 325
quit_button_Y = 480

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
#	- Create variables for the buttons xy
def arcade_machine_menu() :
	main_clock = pygame.time.Clock()
	run = True
	rainbow_title = 0
	i_text_animation = 0

	while run:
		main_clock.tick(15)

		for event in pygame.event.get() :
		
			if event.type == pygame.QUIT :
				sys.exit()
		
		# SCREEN ELEMENTS :

		screen.fill(black)
		mouse = pygame.mouse.get_pos()

		# Title:
		rainbow_title += 1
		if rainbow_title > 42 : rainbow_title = 0
		title = title_font.render(title_string, True, rainbow_array[rainbow_title])
		screen.blit(title, (75,50))

		# Buttons:
		if i_text_animation < 9 : i_text_animation += 1
		if i_text_animation == 9 : i_text_animation = 0

		#tetris
		if (100 <= mouse[0] <= 350) and (250 <= mouse[1] <= 330) :
			draw_button(screen, 100, 250, tetris_string, True, text_animation_array[i_text_animation])

			if event.type == pygame.MOUSEBUTTONDOWN :
				tetris_menu()
		else:
			draw_button(screen, 100, 250, tetris_string, False, 0)

		#snake
		if (100 <= mouse[0] <= 350) and (450 <= mouse[1] <= 530) :
			draw_button(screen, 100, 450, snake_string, True, text_animation_array[i_text_animation])

			if event.type == pygame.MOUSEBUTTONDOWN :
				print('NOT AVAILABLE')
				# pygame.quit()
				# exec(open(snake_path).read())
		else:
			draw_button(screen, 100, 450, snake_string, False, 0)

		#pong
		if (100 <= mouse[0] <= 350) and (650 <= mouse[1] <= 730) :
			draw_button(screen, 100, 650, pong_string, True, text_animation_array[i_text_animation])

			if event.type == pygame.MOUSEBUTTONDOWN :
				print('NOT AVAILABLE')
				# pygame.quit()
				# exec(open(pong_path).read())
		else:
			draw_button(screen, 100, 650, pong_string, False, 0)

		#connect4
		if (550 <= mouse[0] <= 800) and (250 <= mouse[1] <= 330) :
			draw_button(screen, 550, 250, connect4_string, True, text_animation_array[i_text_animation])

			if event.type == pygame.MOUSEBUTTONDOWN :
				print('NOT AVAILABLE')
				# pygame.quit()
				# exec(open(connect4_path).read())
		else:
			draw_button(screen, 550, 250, connect4_string, False, 0)

		#reaction
		if (550 <= mouse[0] <= 800) and (450 <= mouse[1] <= 530) :
			draw_button(screen, 550, 450, reaction_string, True, text_animation_array[i_text_animation])

			if event.type == pygame.MOUSEBUTTONDOWN :
				print('NOT AVAILABLE')
				# pygame.quit()
				# exec(open(reaction_path).read())
		else:
			draw_button(screen, 550, 450, reaction_string, False, 0)

		#infection
		if (550 <= mouse[0] <= 800) and (650 <= mouse[1] <= 730) :
			draw_button(screen, 550, 650, infection_string, True, text_animation_array[i_text_animation])

			if event.type == pygame.MOUSEBUTTONDOWN :
				print('NOT AVAILABLE')
				# pygame.quit()
				# exec(open(infection_path).read())
		else:
			draw_button(screen, 550, 650, infection_string, False, 0)

		pygame.display.flip()


############################################################## <TETRIS> ##############################################################

## TETRIS MENU LOOP ##
def tetris_menu() :
	menu_clock = pygame.time.Clock()
	run = True
	pause = False
	play = False
	play_button_active = False
	pause_button_active = False
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
							pause_button_active = True
							pause = True

				#MOUSECONTROLS
				if (play_button_X <= mouse[0] <= play_button_X+button_width) and (play_button_Y <= mouse[1] <= play_button_Y+button_height) :
					play_button_active = True
					if event.type == pygame.MOUSEBUTTONDOWN : play = True
				else:
					play_button_active = False
				

				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
					pause_button_active = True
					if event.type == pygame.MOUSEBUTTONDOWN : pause = True
				elif pause == False:
					pause_button_active = False

		
		# SCREEN ELEMENTS

		# Background :
		screen.fill(black)

		# Panels :
		draw_tetris_panels(screen, pause_button_active)
		draw_tetris_menu(screen, play_button_active)
		if pause : tetris_pause(in_game=False)
		if play : tetris_game()

		pygame.display.flip()


## TETRIS MAIN LOOP ##
def tetris_game() :
	game_clock = pygame.time.Clock()
	run = True
	pause = False
	pause_button_active = False
	while run :
		game_clock.tick(30)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				
				#KEYCONTROLS
				if event.type == pygame.KEYDOWN:
					keys_pressed = pygame.key.get_pressed()

					if keys_pressed[pygame.K_ESCAPE] :
							pause_button_active = True
							pause = True

				#MOUSECONTROLS
				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
					pause_button_active = True
					if event.type == pygame.MOUSEBUTTONDOWN : pause = True
				elif pause == False:
					pause_button_active = False

		# SCREEN ELEMENTS :

		#	- Background :
		screen.fill(black)

		#	- Panels :
		draw_tetris_panels(screen, pause_button_active)
		#draw_board()
		if pause : tetris_pause(in_game=True)


		pygame.display.flip()


def tetris_pause(in_game):
	paused = True
	pause_clock = pygame.time.Clock()
	resume_button_active = False
	controls_button_active = False
	quit_button_active = False

	show_controls = False

	while paused:
		pause_clock.tick(30)
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():

				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				
				#KEYCONTROLS
				if event.type == pygame.KEYDOWN:
					keys_pressed = pygame.key.get_pressed()
					if keys_pressed[pygame.K_SPACE]:
							paused = False

					elif keys_pressed[pygame.K_ESCAPE] :
							paused = False

					elif show_controls :
							if keys_pressed[pygame.K_ESCAPE]:
								show_controls = False
				
				#MOUSECONTROLS
				if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
							if event.type == pygame.MOUSEBUTTONDOWN : 
								paused = False
				
				if (resume_button_X <= mouse[0] <= resume_button_X+button_width) and (resume_button_Y <= mouse[1] <= resume_button_Y+button_height) :
					resume_button_active = True
					if event.type == pygame.MOUSEBUTTONDOWN : 
							paused = False
				else:
					resume_button_active = False
				
				if (controls_button_X <= mouse[0] <= controls_button_X+button_width) and (controls_button_Y <= mouse[1] <= controls_button_Y+button_height) :
					controls_button_active = True
					if event.type == pygame.MOUSEBUTTONDOWN :
							#show_controls = True 
							pass
				else:
					controls_button_active = False

				if (quit_button_X <= mouse[0] <= quit_button_X+button_width) and (quit_button_Y <= mouse[1] <= quit_button_Y+button_height) :
					quit_button_active = True
					if event.type == pygame.MOUSEBUTTONDOWN :
							if in_game == True : tetris_menu()
							if in_game == False : arcade_machine_menu()
				else:
					quit_button_active = False

		draw_tetris_pause(screen, resume_button_active, controls_button_active, quit_button_active)

		if show_controls :
				#Show the user the game controls
				pass

		pygame.display.flip()
	
	if in_game :
		tetris_game()
	else:
		tetris_menu()

############################################################## </TETRIS> ##############################################################