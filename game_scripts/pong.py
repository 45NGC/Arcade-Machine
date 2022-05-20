import pygame
from game_scripts.utilities import draw_button2
pygame.init()

# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)

def draw_pong_menu(screen, mouse) :
	# Title
	pong_title_string = 'PONG'
	pong_label_background1 = pygame.Rect(100, 100, 300, 300)
	pong_label_background2 = pygame.Rect(110, 110, 280, 280)

	# Dynamic mode switch
	dynamic_mode_string = 'DYNAMIC MODE'
	dynamic_mode_panel_background1 = pygame.Rect(745, 45, 190, 90)
	dynamic_mode_panel_background2 = pygame.Rect(750, 50, 200, 100)

	# Game modes buttons
	mode1_string  = '1 vs 1'
	mode2_string  = '1 vs IA'
	mode3_string  = 'WALL MODE'
	mode4_string  = 'TRAINING'
	draw_button2(screen, 75, 200, mode1_string, mouse)
	draw_button2(screen, 75, 350, mode2_string, mouse)
	draw_button2(screen, 75, 500, mode3_string, mouse)
	draw_button2(screen, 75, 650, mode4_string, mouse)

	# Highscores
	# IA difficulty selector
	easy_mode_string = 'EASY'
	normal_mode_string = 'NORMAL'
	hard_mode_string = 'HARD'
	legend_mode_string = 'LEGEND'
	easy_mode_switch_background = pygame.Rect(500, 390, 40, 40)
	easy_mode_switch = pygame.Rect(505, 395, 30, 30)
	normal_mode_switch_background = pygame.Rect(560, 390, 40, 40)
	normal_mode_switch = pygame.Rect(565, 395, 30, 30)
	hard_mode_switch_background = pygame.Rect(620, 390, 40, 40)
	hard_mode_switch = pygame.Rect(625, 395, 30, 30)
	legend_mode_switch_background = pygame.Rect(680, 390, 40, 40)
	legend_mode_switch = pygame.Rect(685, 395, 30, 30)

	# Pause button
