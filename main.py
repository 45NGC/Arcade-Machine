import pygame, sys
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)

# Create colors
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
red_pink = (255, 0, 102)

# Create fonts
title_font = pygame.font.Font('fonts\\main_fonts\\ARCADECLASSIC.TTF', 100)
buttons_font = pygame.font.Font('fonts\\main_fonts\\Ode to Idle Gaming.ttf', 30)

# Create Strings
title_string 		= 'ARCADE   MACHINE'
tetris_string 		= '   TETRIS'
snake_string 		= '    SNAKE'
pong_string 		= '     PONG'
connect4_string 	= 'CONNECT 4'
reaction_string 	= ' REACTION'
infection_string 	= 'INFECTION'

# Define game paths
tetris_path			= 'games\\tetris\\tetris.py'
snake_path			= 'games\\snake\\snake.py'
pong_path			= 'games\\'
connect4_path		= 'games\\'
reaction_path		= 'games\\'
infection_path		= 'games\\'

# Functions
def rainbow_letters() :
	pass

def draw_button(x_axis, y_axis, text, active) :
	text = text.center(12)

	if active == True:
		pygame.draw.rect(screen, pink, [x_axis, y_axis, 250,80])
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70])
		button = buttons_font.render(text, True, red_pink)
		screen.blit(button, (x_axis+5,y_axis+15))
	else:
		pygame.draw.rect(screen, white, [x_axis, y_axis, 250,80])
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70])
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

while True:

	for event in pygame.event.get() :
	
		if event.type == pygame.QUIT :
			sys.exit()
	
	# SCREEN ELEMENTS :

	#	- Background:
	screen.fill(black)

	#	- Title:
	title = title_font.render(title_string, True, white)
	screen.blit(title, (75,50))

	# 	- Mouse
	mouse = pygame.mouse.get_pos()

	#	- Buttons:

	# Tetris
	if (100 <= mouse[0] <= 350) and (250 <= mouse[1] <= 330) :
		draw_button(100, 250, tetris_string, True)

		if event.type == pygame.MOUSEBUTTONDOWN :
			pygame.quit()
			exec(open(tetris_path).read())
	else:
		draw_button(100, 250, tetris_string, False)

	# Snake
	if (100 <= mouse[0] <= 350) and (450 <= mouse[1] <= 530) :
		draw_button(100, 450, snake_string, True)

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(snake_path).read())
	else:
		draw_button(100, 450, snake_string, False)

	# Pong
	if (100 <= mouse[0] <= 350) and (650 <= mouse[1] <= 730) :
		draw_button(100, 650, pong_string, True)

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(pong_path).read())
	else:
		draw_button(100, 650, pong_string, False)

	# Connect 4
	if (550 <= mouse[0] <= 800) and (250 <= mouse[1] <= 330) :
		draw_button(550, 250, connect4_string, True)

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(connect4_path).read())
	else:
		draw_button(550, 250, connect4_string, False)

	# Reaction
	if (550 <= mouse[0] <= 800) and (450 <= mouse[1] <= 530) :
		draw_button(550, 450, reaction_string, True)

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(reaction_path).read())
	else:
		draw_button(550, 450, reaction_string, False)

	# Infection
	if (550 <= mouse[0] <= 800) and (650 <= mouse[1] <= 730) :
		draw_button(550, 650, infection_string, True)

		if event.type == pygame.MOUSEBUTTONDOWN :
			print('NOT AVAILABLE')
			# pygame.quit()
			# exec(open(infection_path).read())
	else:
		draw_button(550, 650, infection_string, False)

	pygame.display.flip()