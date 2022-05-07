import sys
import pygame
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ARCADE MACHINE')

# Create colors
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
red_pink = (255, 0, 102)

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

# Create fonts
title_font = pygame.font.Font('games\\fonts\\main_fonts\\ARCADECLASSIC.TTF', 100)
buttons_font = pygame.font.Font('games\\fonts\\main_fonts\\Ode to Idle Gaming.ttf', 30)
text_animation_array = [0,1,2,3,4,5,4,3,2,1]

# Create Strings
title_string 		= 'ARCADE   MACHINE'
tetris_string 		= '   TETRIS'
snake_string 		= '    SNAKE'
pong_string 		= '     PONG'
connect4_string 	= 'CONNECT 4'
reaction_string 	= ' REACTION'
infection_string 	= 'INFECTION'

# Define game paths
tetris_path			= 'games\\tetris.py'
snake_path			= 'games\\snake.py'
pong_path			= 'games\\'
connect4_path		= 'games\\'
reaction_path		= 'games\\'
infection_path		= 'games\\'

# Functions
def draw_button(x_axis, y_axis, text, active, text_animation) :
	text = text.center(12)

	if active == True:
		pygame.draw.rect(screen, pink, [x_axis, y_axis, 250,80], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70], border_radius = 20)
		button = buttons_font.render(text, True, red_pink)
		screen.blit(button, (x_axis+5 , y_axis+10 + text_animation))
	else:
		pygame.draw.rect(screen, white, [x_axis, y_axis, 250,80], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70], border_radius = 20)
		button = buttons_font.render(text, True, white)
		screen.blit(button, (x_axis+5,y_axis+10))

## MAIN LOOP ##
# This loop will display a screen with the name 'Arcade Machine' and a scroll of the games we can play, the games will include :
# 	- Tetris
# 	- Snake	
# 	- Pong 
# 	- Connect 4
# 	- Reaction
#	- Infection

# TODO
# 	- Add animation : rainbow letters for the title
# 	- Add music and sound to the buttons

clock = pygame.time.Clock()
run = True
rainbow_title = 0
i_text_animation = 0

while run:
	clock.tick(15)

	for event in pygame.event.get() :
	
		if event.type == pygame.QUIT :
			sys.exit()
	
	# SCREEN ELEMENTS :

	#	- Background:
	screen.fill(black)

	#	- Title:
	rainbow_title += 1
	if rainbow_title > 42 : rainbow_title = 0

	title = title_font.render(title_string, True, rainbow_array[rainbow_title])
	screen.blit(title, (75,50))


	# 	- Mouse
	mouse = pygame.mouse.get_pos()

	#	- Buttons:
	if i_text_animation < 9 : i_text_animation += 1
	if i_text_animation == 9 : i_text_animation = 0
	
	# Tetris
	if (100 <= mouse[0] <= 350) and (250 <= mouse[1] <= 330) :
		draw_button(100, 250, tetris_string, True, text_animation_array[i_text_animation])

		if event.type == pygame.MOUSEBUTTONDOWN :
			pygame.quit()
			exec(open(tetris_path).read())
	else:
		draw_button(100, 250, tetris_string, False, 0)

	# Snake
	if (100 <= mouse[0] <= 350) and (450 <= mouse[1] <= 530) :
		draw_button(100, 450, snake_string, True, text_animation_array[i_text_animation])

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(snake_path).read())
	else:
		draw_button(100, 450, snake_string, False, 0)

	# Pong
	if (100 <= mouse[0] <= 350) and (650 <= mouse[1] <= 730) :
		draw_button(100, 650, pong_string, True, text_animation_array[i_text_animation])

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(pong_path).read())
	else:
		draw_button(100, 650, pong_string, False, 0)

	# Connect 4
	if (550 <= mouse[0] <= 800) and (250 <= mouse[1] <= 330) :
		draw_button(550, 250, connect4_string, True, text_animation_array[i_text_animation])

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(connect4_path).read())
	else:
		draw_button(550, 250, connect4_string, False, 0)

	# Reaction
	if (550 <= mouse[0] <= 800) and (450 <= mouse[1] <= 530) :
		draw_button(550, 450, reaction_string, True, text_animation_array[i_text_animation])

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(reaction_path).read())
	else:
		draw_button(550, 450, reaction_string, False, 0)

	# Infection
	if (550 <= mouse[0] <= 800) and (650 <= mouse[1] <= 730) :
		draw_button(550, 650, infection_string, True, text_animation_array[i_text_animation])

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(infection_path).read())
	else:
		draw_button(550, 650, infection_string, False, 0)

	pygame.display.flip()