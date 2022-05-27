import pygame
from game_scripts.utilities import draw_button2
pygame.init()

# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
purple = (153,0,255)

def draw_pong_menu(screen, mouse) :
	# Title
	pong_title_string = 'PONG'
	pong_label_background1 = pygame.Rect(300, 30, 300, 250)
	pong_label_background2 = pygame.Rect(310, 40, 280, 230)
	pygame.draw.ellipse(screen, white, pong_label_background1)
	pygame.draw.ellipse(screen, black, pong_label_background2)

	pong_title_font = pygame.font.Font('resources\\fonts\\ARCADECLASSIC.TTF', 100)
	pong_title = pong_title_font.render(pong_title_string, True, white)
	screen.blit(pong_title, (345,105))

	# Game modes buttons
	mode1_string  = '1 vs IA'
	mode2_string  = '1 vs 1'
	mode3_string  = 'PRACTISE'
	draw_button2(screen, 70, 330, mode1_string, mouse)
	draw_button2(screen, 580, 330, mode2_string, mouse)
	draw_button2(screen, 325, 570, mode3_string, mouse)

def draw_pong_pause_button(screen) :
	x_axis, y_axis = 425, 770
	button_border = pygame.Rect(x_axis-2, y_axis-2, 54, 54)
	pause_button = pygame.Rect(x_axis, y_axis, 50, 50)
	stick_1 = pygame.Rect(x_axis+10, y_axis+5, 5, 40)
	stick_2 = pygame.Rect(x_axis+35, y_axis+5, 5, 40)

	pygame.draw.rect(screen, pink, button_border, border_radius = 10)
	pygame.draw.rect(screen, black, pause_button, border_radius = 10)
	pygame.draw.rect(screen, white, stick_1)
	pygame.draw.rect(screen, white, stick_2)

def draw_pong_pause_menu(screen, mouse):
	x_axis , y_axis = 425, 770
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
	pause_font = pygame.font.Font('resources\\fonts\\Gameplay.ttf', 30)
	pause_title = pause_font.render(pause_string, True, white)
	screen.blit(pause_title, (400,240))
	
	# Buttons
	resume_string = '  RESUME'
	controls_string = 'CONTROLS'
	quit_string = '     QUIT'
	draw_button2(screen, 325, 300, resume_string, mouse)
	draw_button2(screen, 325, 390, controls_string, mouse)
	draw_button2(screen, 325, 480, quit_string, mouse)

def draw_pong_circumstancial_menus():
	# IA difficulty selector
	# easy_mode_string = 'EASY'
	# normal_mode_string = 'NORMAL'
	# hard_mode_string = 'HARD'
	# legend_mode_string = 'LEGEND'
	# easy_mode_switch_background = pygame.Rect(500, 330, 40, 40)
	# easy_mode_switch = pygame.Rect(505, 335, 30, 30)
	# normal_mode_switch_background = pygame.Rect(560, 330, 40, 40)
	# normal_mode_switch = pygame.Rect(565, 335, 30, 30)
	# hard_mode_switch_background = pygame.Rect(620, 330, 40, 40)
	# hard_mode_switch = pygame.Rect(625, 335, 30, 30)
	# legend_mode_switch_background = pygame.Rect(680, 330, 40, 40)
	# legend_mode_switch = pygame.Rect(685, 335, 30, 30)
	# pygame.draw.ellipse(screen, white, easy_mode_switch_background)
	# pygame.draw.ellipse(screen, white, normal_mode_switch_background)
	# pygame.draw.ellipse(screen, white, hard_mode_switch_background)
	# pygame.draw.ellipse(screen, white, legend_mode_switch_background)

	# if selected_difficulty == 1 : pygame.draw.ellipse(screen, black, easy_mode_switch)
	# if selected_difficulty == 2 : pygame.draw.ellipse(screen, black, normal_mode_switch)
	# if selected_difficulty == 3 : pygame.draw.ellipse(screen, black, hard_mode_switch)
	# if selected_difficulty == 4 : pygame.draw.ellipse(screen, black, legend_mode_switch)
	pass
