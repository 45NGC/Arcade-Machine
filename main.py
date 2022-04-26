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
def activate_button(x_axis, y_axis, text):

	pygame.draw.rect(screen, yellow, [x_axis, y_axis, 250,80])
	pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70])
	button = buttons_font.render(text, True, yellow)
	screen.blit(button, (x_axis+5,y_axis+15))

def button_up(i):
	if i < 3 :
		return i+4
	else:
		return i-2

def button_down(i):
	if i > 4 :
		return i-4
	else:
		return i+2

def button_rigt_left(i):
	if i == 1 or 3 or 5 :
		return i+1
	else:
		return i-1


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

x = 0
y = 0
i = 0

# By default the control is the mouse
keyboard = False
mouse = True

while True:

	for event in pygame.event.get():
		print(event)

		if event.type == pygame.QUIT :
			sys.exit()


	if event.type == pygame.KEYDOWN :
			mouse = False
			keyboard = True
			i = 1

	if event.type == pygame.MOUSEMOTION :
			mouse = True
			keyboard = False


	# SCREEN ELEMENTS :

	#	- Background:
	screen.fill(black)

	#	- Title:
	title = title_font.render(title_string, True, white)
	screen.blit(title, (75,50))

	#	- Buttons:

	# TETRIS
	if x!=100 or y!=250 :
		pygame.draw.rect(screen, white, [100, 250, 250,80])
		pygame.draw.rect(screen, black, [105, 255, 240,70])
		tetris_button = buttons_font.render(tetris_string, True, white)
		screen.blit(tetris_button, (105,260))
	else:
		activate_button(100, 250, tetris_string)

	# SNAKE
	if x!=100 or y!=450 :
		pygame.draw.rect(screen, white, [100, 450, 250,80])
		pygame.draw.rect(screen, black, [105, 455, 240,70])
		snake_button = buttons_font.render(snake_string, True, white)
		screen.blit(snake_button, (105,460))
	else:
		activate_button(100, 450, snake_string)

	# PONG
	if x!=100 or y!=650 :
		pygame.draw.rect(screen, white, [100, 650, 250,80])
		pygame.draw.rect(screen, black, [105, 655, 240,70])
		pong_button = buttons_font.render(pong_string, True, white)
		screen.blit(pong_button, (105,660))
	else:
		activate_button(100, 650, pong_string)

	# CONNECT 4
	if x!=550 or y!=250 :
		pygame.draw.rect(screen, white, [550, 250, 250,80])
		pygame.draw.rect(screen, black, [555, 255, 240,70])
		connect4_button = buttons_font.render(connect4_string, True, white)
		screen.blit(connect4_button, (555,260))
	else:
		activate_button(550, 250, connect4_string)

	# REACTION
	if x!=550 or y!=450 :
		pygame.draw.rect(screen, white, [550, 450, 250,80])
		pygame.draw.rect(screen, black, [555, 455, 240,70])
		reaction_button = buttons_font.render(reaction_string, True, white)
		screen.blit(reaction_button, (555,460))
	else:
		activate_button(550, 450, reaction_string)

	# INFECTION
	if x!=550 or y!=650 :
		pygame.draw.rect(screen, white, [550, 650, 250,80])
		pygame.draw.rect(screen, black, [555, 655, 240,70])
		infection_button = buttons_font.render(infection_string, True, white)
		screen.blit(infection_button, (555,660))
	else:
		activate_button(550, 650, infection_string)
	


	##  MOUSE CONTROL  ##
	if mouse:
		x = 0
		y = 0
		mouse_pos = pygame.mouse.get_pos()

		# Tetris
		if ((100 <= mouse_pos[0] <= 350) and (250 <= mouse_pos[1] <= 330)) :
			activate_button(100, 250, tetris_string)

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.quit()
				exec(open(tetris_path).read())

		# Snake
		if (100 <= mouse_pos[0] <= 350) and (450 <= mouse_pos[1] <= 530) :
			activate_button(100, 450, snake_string)

		# Pong
		if (100 <= mouse_pos[0] <= 350) and (650 <= mouse_pos[1] <= 730) :
			activate_button(100, 650, pong_string)

		# Connect 4
		if (550 <= mouse_pos[0] <= 800) and (250 <= mouse_pos[1] <= 330) :
			activate_button(550, 250, connect4_string)

		# Reaction
		if (550 <= mouse_pos[0] <= 800) and (450 <= mouse_pos[1] <= 530) :
			activate_button(550, 450, reaction_string)

		# Infection
		if (550 <= mouse_pos[0] <= 800) and (650 <= mouse_pos[1] <= 730) :
			activate_button(550, 650, infection_string)


	##  KEYBOARD CONTROL  ##
	if keyboard:
		# if pygame.key.name(event.key) == "up":
		# 	i = button_up(i)
		
		# if pygame.key.name(event.key) == "down":
		# 	i = button_down(i)
		
		# if pygame.key.name(event.key) == 'right' or 'left':
		# 	i = button_rigt_left(i)

		# 'i' has to be always between 1 and 6
		print(i)

		# Tetris
		if i == 1 :
			print('TETRIS')
			x = 100
			y = 250
		
		# Connect 4
		if i == 2 :
			print('CONNECT4')
			x = 550
			y = 250
		
		# Snake
		if i == 3 :
			print('SNAKE')
			x = 100
			y = 450
		
		# Reaction
		if i == 4 :
			print('REACTION')
			x = 550
			y = 450
		
		# Pong
		if i == 5 :
			print('PONG')
			x = 100
			y = 650

		# Infection
		if i == 6 :
			print('INFECTION')
			x = 550
			y = 650


		# Depending on the value of 'i' it paints a different scheme of buttons
		
		if pygame.key.get_pressed()[pygame.K_UP] :
			i = button_up(i)

		if pygame.key.get_pressed()[pygame.K_DOWN] :
			i = button_down(i)
		
		if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT] :
			i = button_rigt_left(i)

	pygame.display.flip()