from ast import keyword
import pygame, sys
pygame.init()

# Create screen
size = (900,800)
screen = pygame.display.set_mode(size)

# Create colors
black = (0,0,0)
grey = (90,90,90)
white = (255,255,255)
yellow = (255,255,0)
green = (102,255,102)

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


tetris_string		= tetris_string.center(12)		
snake_string 		= snake_string.center(12)	
pong_string 		= pong_string.center(12)	
connect4_string		= connect4_string.center(12)	
reaction_string 	= reaction_string.center(12)	
infection_string 	= infection_string.center(12)	

# Define game paths
tetris_path			= 'games\\tetris\\tetris.py'
snake_path			= 'games\\snake\\snake.py'
pong_path			= 'games\\'
connect4_path		= 'games\\'
reaction_path		= 'games\\'
infection_path		= 'games\\'

# Functions
def draw_buttons(x, y):

	if x!=100 or y!=250 :
		# TETRIS
		pygame.draw.rect(screen, white, [100, 250, 250,80])
		pygame.draw.rect(screen, black, [105, 255, 240,70])
		tetris_button = buttons_font.render(tetris_string, True, white)
		screen.blit(tetris_button, (105,260))
	else:
		activate_button(100, 250, tetris_string)

	if x!=100 or y!=450 :
		# SNAKE
		pygame.draw.rect(screen, white, [100, 450, 250,80])
		pygame.draw.rect(screen, black, [105, 455, 240,70])
		snake_button = buttons_font.render(snake_string, True, white)
		screen.blit(snake_button, (105,460))
	else:
		activate_button(100, 460, snake_string)

	if x!=100 or y!=650 :
		# PONG
		pygame.draw.rect(screen, white, [100, 650, 250,80])
		pygame.draw.rect(screen, black, [105, 655, 240,70])
		pong_button = buttons_font.render(pong_string, True, white)
		screen.blit(pong_button, (105,660))
	else:
		activate_button(100, 660, pong_string)

	if x!=550 or y!=250 :
		# CONNECT 4
		pygame.draw.rect(screen, white, [550, 250, 250,80])
		pygame.draw.rect(screen, black, [555, 255, 240,70])
		connect4_button = buttons_font.render(connect4_string, True, white)
		screen.blit(connect4_button, (555,260))

	if x!=550 or y!=450 :
		# REACTION
		pygame.draw.rect(screen, white, [550, 450, 250,80])
		pygame.draw.rect(screen, black, [555, 455, 240,70])
		reaction_button = buttons_font.render(reaction_string, True, white)
		screen.blit(reaction_button, (555,460))

	if x!=550 or y!=650 :
		# INFECTION
		pygame.draw.rect(screen, white, [550, 650, 250,80])
		pygame.draw.rect(screen, black, [555, 655, 240,70])
		infection_button = buttons_font.render(infection_string, True, white)
		screen.blit(infection_button, (555,660))


def activate_button(x_axis, y_axis, text):

	pygame.draw.rect(screen, yellow, [x_axis, y_axis, 250,80])
	pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70])
	button = buttons_font.render(text, True, yellow)
	screen.blit(button, (x_axis+5,y_axis+15))


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

# The default control device is the mouse but if the user presses a key it is possible to use the keyboard as the control device
keyboard = False

while True:

	for event in pygame.event.get():
		print(event)

		if event.type == pygame.QUIT :
			sys.exit()
	
	# SCREEN ELEMENTS :

	#	- Background:
	screen.fill(black)

	#	- Title:
	title = title_font.render(title_string, True, white)
	screen.blit(title, (75,50))

	#	- Buttons:

	if event.type == pygame.KEYDOWN :
		#KEYBOARD
		print('Keyboard activated')
		keyboard = True

		tetris_button = False
		snake_button = False
		pong_button = False
		connect4_button = False
		reaction_button = False
		infection_button = False

	else:
		if keyboard == False:
			draw_buttons(0,0)

		#MOUSE
		mouse = pygame.mouse.get_pos()

		# Tetris
		if ((100 <= mouse[0] <= 350) and (250 <= mouse[1] <= 330)) :
			activate_button(100, 250, tetris_string)

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.quit()
				exec(open(tetris_path).read())

		# Snake
		if (100 <= mouse[0] <= 350) and (450 <= mouse[1] <= 530) :
			activate_button(100, 450, snake_string)

		# Pong
		if (100 <= mouse[0] <= 350) and (650 <= mouse[1] <= 730) :
			activate_button(100, 650, pong_string)

		# Connect 4
		if (550 <= mouse[0] <= 800) and (250 <= mouse[1] <= 330) :
			activate_button(550, 250, connect4_string)

		# Reaction
		if (550 <= mouse[0] <= 800) and (450 <= mouse[1] <= 530) :
			activate_button(550, 450, reaction_string)

		# Infection
		if (550 <= mouse[0] <= 800) and (650 <= mouse[1] <= 730) :
			activate_button(550, 650, infection_string)
		
		if keyboard == False:
			pygame.display.flip()