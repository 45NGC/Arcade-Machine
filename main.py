import pygame, sys
pygame.init()

# Create screen
size = (1000,1000)
screen = pygame.display.set_mode(size)

width = screen.get_width()
height = screen.get_height()

# Create colors
black = (0,0,0)
grey = (90,90,90)
white = (255,255,255)
yellow = (255,255,0)
green = (102,255,102)

# Create fonts
title_font = pygame.font.Font('fonts\\ARCADECLASSIC.TTF', 100)
buttons_font = pygame.font.Font('fonts\\Ode to Idle Gaming.ttf', 30)

# Create Strings
title_string 		= 'ARCADE      MACHINE'
tetris_string 		= '   TETRIS'
snake_string 		= '    SNAKE'
pong_string 		= '     PONG'
connect4_string 	= 'CONNECT 4'
reaction_string 	= ' REACTION'
infection_string 	= 'INFECTION'

# Functions
def draw_button(x_axis, y_axis, text, active):
	text = text.center(12)

	if active == True:
		pygame.draw.rect(screen, yellow, [x_axis, y_axis, 250,80])
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70])
		button = buttons_font.render(text, True, yellow)
		screen.blit(button, (x_axis+5,y_axis+15))
	else:
		pygame.draw.rect(screen, white, [x_axis, y_axis, 250,80])
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70])
		button = buttons_font.render(text, True, white)
		screen.blit(button, (x_axis+5,y_axis+10))





# Main loop
# This loop will display a screen with the name 'Arcade Machine' and a scroll of the games we can play, the games will include :
# 	- Tetris
# 	- Snake	
# 	- Pong 
# 	- Connect 4
# 	- Reaction
#	- Infection
#
# TODO
# 	- Add animation 
# 	- Add music

while True:

	for event in pygame.event.get():
		#print(event)
	
		if event.type == pygame.QUIT:
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			print('Mouse button pressed')
	
	# SCREEN ELEMENTS :

	#	- Background:
	screen.fill(black)

	# 	- Mouse
	mouse = pygame.mouse.get_pos()

	#	- Buttons:

	# Tetris
	if (100 <= mouse[0] <= 350) and (350 <= mouse[1] <= 430) :
		draw_button(100, 350, tetris_string, True)
	else:
		draw_button(100, 350, tetris_string, False)

	# Snake
	if (100 <= mouse[0] <= 350) and (550 <= mouse[1] <= 630) :
		draw_button(100, 550, snake_string, True)
	else:
		draw_button(100, 550, snake_string, False)

	# Pong
	if (100 <= mouse[0] <= 350) and (750 <= mouse[1] <= 830) :
		draw_button(100, 750, pong_string, True)
	else:
		draw_button(100, 750, pong_string, False)

	# Connect 4
	if (650 <= mouse[0] <= 900) and (350 <= mouse[1] <= 430) :
		draw_button(650, 350, connect4_string, True)
	else:
		draw_button(650, 350, connect4_string, False)

	# Reaction
	if (650 <= mouse[0] <= 900) and (550 <= mouse[1] <= 630) :
		draw_button(650, 550, reaction_string, True)
	else:
		draw_button(650, 550, reaction_string, False)

	# Infection
	if (650 <= mouse[0] <= 900) and (750 <= mouse[1] <= 830) :
		draw_button(650, 750, infection_string, True)
	else:
		draw_button(650, 750, infection_string, False)


	#	- Title:
	title = title_font.render(title_string, True, white)
	screen.blit(title, (100,100))

	pygame.display.flip()