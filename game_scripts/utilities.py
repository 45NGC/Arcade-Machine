import pygame
pygame.init()

# COLORS
black = (0,0,0)
grey = (60,60,60)
white = (255,255,255)
pink = (255, 153, 255)
red_pink = (255, 0, 102)
purple = (153,0,255)

# FONTS
button1_font = pygame.font.Font('resources/fonts/Ode to Idle Gaming.ttf', 30)
button2_font = pygame.font.Font('resources/fonts/Gameplay.ttf', 25)

# BUTTONS
button1_width = 244
button1_height = 74

button2_width = 250
button2_height = 80

# TEXT INPUTS
TEXT_INPUT_WIDTH = 400
TEXT_INPUT_HEIGHT = 70

def draw_button1(screen, x_axis, y_axis, text, mouse, i_text_animation) :
	text = text.center(12)
	text_animation_array = [0,1,2,3,4,5,4,3,2,1]
	
	if(x_axis <= mouse[0] <= x_axis+button1_width) and (y_axis <= mouse[1] <= y_axis+button1_height) :
		pygame.draw.rect(screen, pink, [x_axis-3, y_axis-3, button1_width+6,button1_height+6], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis+3, y_axis+3, button1_width-6,button1_height-6], border_radius = 20)
		button = button1_font.render(text, True, red_pink)
		screen.blit(button, (x_axis+5 , y_axis+10 + text_animation_array[i_text_animation]))
	else:
		pygame.draw.rect(screen, white, [x_axis-3, y_axis-3, button1_width+6,button1_height+6], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis, y_axis, button1_width,button1_height], border_radius = 20)
		button = button1_font.render(text, True, white)
		screen.blit(button, (x_axis+5,y_axis+10))



def draw_button2(screen, x_axis, y_axis, text, mouse) :
	text = text.center(22)

	if (x_axis <= mouse[0] <= x_axis+button2_width) and (y_axis <= mouse[1] <= y_axis+button2_height) :
		pygame.draw.rect(screen, purple, [x_axis-3, y_axis-3, button2_width+6, button2_height+6], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis, y_axis, button2_width, button2_height], border_radius = 20)
		button = button2_font.render(text, True, white)
		screen.blit(button, (x_axis, y_axis+20))
	else:
		pygame.draw.rect(screen, pink, [x_axis-2, y_axis-2, button2_width+4, button2_height+4], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis, y_axis, button2_width, button2_height], border_radius = 20)
		button = button2_font.render(text, True, white)
		screen.blit(button, (x_axis, y_axis+20))



def draw_text_input(screen, x_axis, y_axis, active):

	if active :
		pygame.draw.rect(screen, pink, [x_axis-2, y_axis-2, TEXT_INPUT_WIDTH+4, TEXT_INPUT_HEIGHT+4], border_radius = 5)
		pygame.draw.rect(screen, black, [x_axis, y_axis, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT], border_radius = 5)
	else:
		pygame.draw.rect(screen, grey, [x_axis-5, y_axis-5, TEXT_INPUT_WIDTH+10, TEXT_INPUT_HEIGHT+10], border_radius = 5)
		pygame.draw.rect(screen, black, [x_axis, y_axis, TEXT_INPUT_WIDTH, TEXT_INPUT_HEIGHT], border_radius = 5)

def draw_pause_button(screen, x_axis, y_axis) :
	button_border = pygame.Rect(x_axis-2, y_axis-2, 54, 54)
	pause_button = pygame.Rect(x_axis, y_axis, 50, 50)
	stick_1 = pygame.Rect(x_axis+10, y_axis+5, 5, 40)
	stick_2 = pygame.Rect(x_axis+35, y_axis+5, 5, 40)

	pygame.draw.rect(screen, pink, button_border, border_radius = 10)
	pygame.draw.rect(screen, black, pause_button, border_radius = 10)
	pygame.draw.rect(screen, white, stick_1)
	pygame.draw.rect(screen, white, stick_2)

def draw_pause_menu(screen, x_axis, y_axis, mouse):
	button_border = pygame.Rect(x_axis-2, y_axis-2, 54, 54)
	pause_button = pygame.Rect(x_axis, y_axis, 50, 50)
	stick_1 = pygame.Rect(x_axis+10, y_axis+5, 5, 40)
	stick_2 = pygame.Rect(x_axis+35, y_axis+5, 5, 40)

	# Change pause button color
	pygame.draw.rect(screen, purple, button_border, border_radius = 10)
	pygame.draw.rect(screen, black, pause_button, border_radius = 10)
	pygame.draw.rect(screen, pink, stick_1)
	pygame.draw.rect(screen, pink, stick_2)

	# Pause menu
	pause_menu_background = pygame.Rect(273, 218, 354, 354)
	pause_menu = pygame.Rect(275, 220, 350, 350)
	pygame.draw.rect(screen, pink, pause_menu_background)
	pygame.draw.rect(screen, black, pause_menu)

	pause_string = 'PAUSE'
	pause_font = pygame.font.Font('resources/fonts/Gameplay.ttf', 30)
	pause_title = pause_font.render(pause_string, True, white)
	screen.blit(pause_title, (400,240))
	
	# Buttons
	resume_string = '  RESUME'
	controls_string = 'CONTROLS'
	quit_string = '     QUIT'
	draw_button2(screen, 325, 300, resume_string, mouse)
	draw_button2(screen, 325, 390, controls_string, mouse)
	draw_button2(screen, 325, 480, quit_string, mouse)
