import pygame, sys

class Menu:

	def __init__(self, window_position_x, window_position_y):
		print(window_position_x, window_position_y)
		pygame.init()

		# Create screen
		size = (1000,800)
		screen = pygame.display.set_mode(size)
		#screen.position(window_position_x, window_position_y)

		self.screen = screen

		# Create colors
		black = (0,0,0)
		grey = (90,90,90)
		white = (255,255,255)
		yellow = (255,255,0)
		green = (102,255,102)

		self.black = black
		self.grey = grey
		self.white = white
		self.yellow = yellow
		self.green = green

		# Create Strings
		title_string 		= 'ARCADE      MACHINE'
		tetris_string 		= '   TETRIS'
		snake_string 		= '    SNAKE'
		pong_string 		= '     PONG'
		connect4_string 	= 'CONNECT 4'
		reaction_string 	= ' REACTION'
		infection_string 	= 'INFECTION'

		self.title_string 		= title_string
		self.tetris_string 		= tetris_string
		self.snake_string 		= snake_string
		self.pong_string 		= pong_string
		self.connect4_string 	= connect4_string
		self.reaction_string 	= reaction_string
		self.infection_string 	= infection_string

		# Create fonts
		title_font = pygame.font.Font('fonts\\menu_fonts\\ARCADECLASSIC.TTF', 100)
		buttons_font = pygame.font.Font('fonts\\menu_fonts\\Ode to Idle Gaming.ttf', 30)

		self.title_font = title_font
		self.buttons_font = buttons_font

		self.menu()

	# Functions
	def draw_button(self, screen, x_axis, y_axis, text, active):
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

	def menu(self):
		## MENU LOOP ##
		# This loop will display a screen with the name 'Arcade Machine' and a scroll of the games we can play, the games will include :
		# 	- Tetris
		# 	- Snake	
		# 	- Pong 
		# 	- Connect 4
		# 	- Reaction
		#	- Infection

		#TODO
		# 	- Add animation : rainbow letters for the title
		# 	- Add music and sound to the buttons
		#	- When a button is pressed paint it green

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# SCREEN ELEMENTS :

			#	- Background:
			screen.fill(black)

			# 	- Mouse
			mouse = pygame.mouse.get_pos()

			#	- Buttons:

			# Tetris
			if (100 <= mouse[0] <= 350) and (250 <= mouse[1] <= 330) :
				Menu.draw_button(self, screen, 100, 250, tetris_string, True)

				if event.type == pygame.MOUSEBUTTONDOWN:
					pygame.quit()
					exec(open(tetris_path).read())
			else:
				Menu.draw_button(self, screen, 100, 250, tetris_string, False)

			# Snake
			if (100 <= mouse[0] <= 350) and (450 <= mouse[1] <= 530) :
				Menu.draw_button(self, screen, 100, 450, snake_string, True)
			else:
				Menu.draw_button(self, screen, 100, 450, snake_string, False)

			# Pong
			if (100 <= mouse[0] <= 350) and (650 <= mouse[1] <= 730) :
				Menu.draw_button(self, screen, 100, 650, pong_string, True)
			else:
				Menu.draw_button(self, screen, 100, 650, pong_string, False)

			# Connect 4
			if (650 <= mouse[0] <= 900) and (250 <= mouse[1] <= 330) :
				Menu.draw_button(self, screen, 650, 250, connect4_string, True)
			else:
				Menu.draw_button(self, screen, 650, 250, connect4_string, False)

			# Reaction
			if (650 <= mouse[0] <= 900) and (450 <= mouse[1] <= 530) :
				Menu.draw_button(self, screen, 650, 450, reaction_string, True)
			else:
				Menu.draw_button(self, screen, 650, 450, reaction_string, False)

			# Infection
			if (650 <= mouse[0] <= 900) and (650 <= mouse[1] <= 730) :
				Menu.draw_button(self, screen, 650, 650, infection_string, True)
			else:
				Menu.draw_button(self, screen, 650, 650, infection_string, False)


			#	- Title:
			title = title_font.render(title_string, True, white)
			screen.blit(title, (100,50))

			pygame.display.flip()