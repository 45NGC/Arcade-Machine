from cmath import rect
from game_scripts.utilities import draw_button2
import random
import pygame
pygame.init()


# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
dark_grey = (40,40,40)
grey = (60,60,60)
light_grey = (100,100,100)
yellow = (255,204,0)
green = (51,204,51)
purple = (153,0,255)
orange = (255, 153, 0)
red = (255, 57, 57)
blue = (0, 64, 255)
turquoise = (0, 255, 255)

# FONTS
tetris_font = pygame.font.Font('resources\\fonts\\tetris_fonts\\UniformBold.ttf', 100)
font_h1 = pygame.font.Font('resources\\fonts\\tetris_fonts\\Gameplay.ttf', 30)
font_h2 = pygame.font.Font('resources\\fonts\\tetris_fonts\\Gameplay.ttf', 25)
font_h3 = pygame.font.Font('resources\\fonts\\tetris_fonts\\Gameplay.ttf', 20)

# STRINGS
tetris_title_string = 'TETRIS'
play_string = '    PLAY'
highscores_string = 'HIGH SCORES'
hold_string = 'HOLD'
next_string = 'NEXT'
score_string = 'SCORE'
lines_string = 'LINES'
pause_string = 'PAUSE'
resume_string = '  RESUME'
controls_string = 'CONTROLS'
quit_string = '     QUIT'

# PANELS
tetris_panel_width = 400  
tetris_panel_height = 800
tetris_panel_X = 250
tetris_panel_Y = 25

hold_panel_width = 150
hold_panel_height = 200
hold_panel_X = 50
hold_panel_Y = 50

score_panel_width = 150
score_panel_height = 300
score_panel_X = 50
score_panel_Y = 500

next_panel_width = 150
next_panel_height = 400
next_panel_X = 700
next_panel_Y = 50

tetris_label_width = 300
tetris_label_height = 110
tetris_label_X = 300
tetris_label_Y = 75

highscores_panel_width = 340
highscores_panel_height = 320
highscores_panel_X = 280
highscores_panel_Y = 470

pause_button_size = 100
pause_button_X = 725
pause_button_Y = 650

pause_menu_size = 350
pause_menu_X = 275
pause_menu_Y = 220

play_button_X = 325
play_button_Y = 350
resume_button_X = 325
resume_button_Y = 300
controls_button_X = 325
controls_button_Y = 390
quit_button_X = 325
quit_button_Y = 480

block_size = 40
rows = 20
columns = 10 


# TETRIS FUNCTIONS
def draw_tetris_panels(screen) :

	# 	- TETRIS
	# Panel
	pygame.draw.rect(screen, pink, [tetris_panel_X-2, tetris_panel_Y-2, tetris_panel_width+4, tetris_panel_height+4])
	pygame.draw.rect(screen, dark_grey, [tetris_panel_X, tetris_panel_Y, tetris_panel_width, tetris_panel_height])


	# 	- HOLD
	# Panel
	pygame.draw.rect(screen, pink, [hold_panel_X-2, hold_panel_Y-2, hold_panel_width+4, hold_panel_height+4])
	pygame.draw.rect(screen, dark_grey, [hold_panel_X, hold_panel_Y, hold_panel_width, hold_panel_height])
	pygame.draw.rect(screen, black, [hold_panel_X+10, hold_panel_Y+60, hold_panel_width-20, hold_panel_height-70], border_radius = 10)

	# Text
	hold_text = font_h2.render(hold_string, True, white)
	screen.blit(hold_text, (hold_panel_X+40, hold_panel_Y+15))


	# 	- SCORE / LINES
	# Panel
	pygame.draw.rect(screen, pink, [score_panel_X-2, score_panel_Y-2, score_panel_width+4, score_panel_height+4])
	pygame.draw.rect(screen, dark_grey, [score_panel_X, score_panel_Y, score_panel_width, score_panel_height])
	pygame.draw.rect(screen, black, [score_panel_X+10, score_panel_Y+60, score_panel_width-20, 50], border_radius = 10)
	pygame.draw.rect(screen, black, [score_panel_X+10, score_panel_Y+220, score_panel_width-20, 50], border_radius = 10)

	# Text
	score_text = font_h2.render(score_string, True, white)
	lines_text = font_h2.render(lines_string, True, white)
	screen.blit(score_text, (score_panel_X+30, score_panel_Y+15))
	screen.blit(lines_text, (score_panel_X+35, score_panel_Y+175))

	#score = font_h3.render(str(score).center(7), True, white)
	#lines = font_h3.render(str(lines).center(7), True, white)
	#screen.blit(score, (score_panel_X+30, score_panel_Y+70))
	#screen.blit(lines, (score_panel_X+30, score_panel_Y+230))


	# 	- NEXT
	# Panel
	pygame.draw.rect(screen, pink, [next_panel_X-2, next_panel_Y-2, next_panel_width+4, next_panel_height+4])
	pygame.draw.rect(screen, dark_grey, [next_panel_X, next_panel_Y, next_panel_width, next_panel_height])
	pygame.draw.rect(screen, black, [next_panel_X+10, next_panel_Y+60, next_panel_width-20, next_panel_height-70], border_radius = 10)

	# Text
	next_text = font_h2.render(next_string, True, white)
	screen.blit(next_text, (next_panel_X+40, next_panel_Y+15))


	# 	- PAUSE
		# Button
	pygame.draw.rect(screen, pink, [pause_button_X-2, pause_button_Y-2, pause_button_size+4, pause_button_size+4], border_radius = 20)
	pygame.draw.rect(screen, black, [pause_button_X, pause_button_Y, pause_button_size, pause_button_size], border_radius = 20)
	pygame.draw.rect(screen, white, [pause_button_X+30, pause_button_Y+15, 10, 70])
	pygame.draw.rect(screen, white, [pause_button_X+60, pause_button_Y+15, 10, 70])

def draw_tetris_board(screen) :

      for i in range(rows):
            pygame.draw.line(screen, light_grey, (tetris_panel_X, tetris_panel_Y+ i*block_size), (tetris_panel_X + tetris_panel_width, tetris_panel_Y + i * block_size))
            for j in range(columns):
                  pygame.draw.line(screen, light_grey, (tetris_panel_X + j * block_size, tetris_panel_Y), (tetris_panel_X + j * block_size, tetris_panel_Y + tetris_panel_height))

def draw_tetris_menu(screen, mouse) :
	# TETRIS LABEL
	pygame.draw.rect(screen, pink, [tetris_label_X-10, tetris_label_Y-10, tetris_label_width+20, tetris_label_height+20])
	pygame.draw.rect(screen, pink, [tetris_label_X+99-10, tetris_label_Y-10, tetris_label_height+20, tetris_label_width-100+20])

	pygame.draw.rect(screen, purple, [tetris_label_X-8, tetris_label_Y-8, tetris_label_width+16, tetris_label_height+16])
	pygame.draw.rect(screen, purple, [tetris_label_X+99-8, tetris_label_Y-8, tetris_label_height+16, tetris_label_width-100+16])

	pygame.draw.rect(screen, pink, [tetris_label_X-2, tetris_label_Y-2, tetris_label_width+4, tetris_label_height+4])
	pygame.draw.rect(screen, pink, [tetris_label_X+99-2, tetris_label_Y-2, tetris_label_height+4, tetris_label_width-100+4])

	pygame.draw.rect(screen, black, [tetris_label_X, tetris_label_Y, tetris_label_width, tetris_label_height])
	pygame.draw.rect(screen, black, [tetris_label_X+99, tetris_label_Y, tetris_label_height, tetris_label_width-100])

	tetris_text = tetris_font.render(tetris_title_string, True, white)
	screen.blit(tetris_text, (tetris_label_X+18, tetris_label_Y))

	# START BUTTON
	draw_button2(screen, play_button_X, play_button_Y, play_string, mouse)

	# HIGH SCORES TABLE
	pygame.draw.rect(screen, pink, [highscores_panel_X-2, highscores_panel_Y-2, highscores_panel_width+4, highscores_panel_height+4])
	pygame.draw.rect(screen, black, [highscores_panel_X, highscores_panel_Y, highscores_panel_width, highscores_panel_height])

	pygame.draw.rect(screen, grey, [highscores_panel_X+15, highscores_panel_Y+60, highscores_panel_width-30, 47])
	pygame.draw.rect(screen, light_grey, [highscores_panel_X+15, highscores_panel_Y+109, highscores_panel_width-30, 47])
	pygame.draw.rect(screen, grey, [highscores_panel_X+15, highscores_panel_Y+158, highscores_panel_width-30, 47])
	pygame.draw.rect(screen, light_grey, [highscores_panel_X+15, highscores_panel_Y+207, highscores_panel_width-30, 47])
	pygame.draw.rect(screen, grey, [highscores_panel_X+15, highscores_panel_Y+256, highscores_panel_width-30, 47])

	highscores_text = font_h1.render(highscores_string, True, white)
	screen.blit(highscores_text, (highscores_panel_X+60, highscores_panel_Y+10))

def draw_tetris_pause(screen, mouse) :
	# Cover background
	pygame.draw.rect(screen, light_grey, [tetris_panel_X, tetris_panel_Y, tetris_panel_width, tetris_panel_height])

	# Menu
	pygame.draw.rect(screen, pink, [pause_menu_X-2, pause_menu_Y-2, pause_menu_size+4, pause_menu_size+4])
	pygame.draw.rect(screen, black, [pause_menu_X, pause_menu_Y, pause_menu_size, pause_menu_size])
	pause_label = font_h1.render(pause_string, True, white)
	screen.blit(pause_label, (pause_menu_X+125, pause_menu_Y+20))

	# Buttons
	draw_button2(screen, resume_button_X, resume_button_Y, resume_string, mouse)
	draw_button2(screen, controls_button_X, controls_button_Y, controls_string, mouse)
	draw_button2(screen, quit_button_X, quit_button_Y, quit_string, mouse)

	# Pause button
	pygame.draw.rect(screen, purple, [pause_button_X-2, pause_button_Y-2, pause_button_size+4, pause_button_size+4], border_radius = 20)
	pygame.draw.rect(screen, black, [pause_button_X, pause_button_Y, pause_button_size, pause_button_size], border_radius = 20)
	pygame.draw.rect(screen, pink, [pause_button_X+30, pause_button_Y+15, 10, 70])
	pygame.draw.rect(screen, pink, [pause_button_X+60, pause_button_Y+15, 10, 70])

def update_tetris_score(screen, score, lines) :
	#score = font_h3.render(str(score).center(7), True, white)
	#lines = font_h3.render(str(lines).center(7), True, white)
	#screen.blit(score, (score_panel_X+30, score_panel_Y+70))
	#screen.blit(lines, (score_panel_X+30, score_panel_Y+230))
	pass


# make an array to indicate that when the piece falls its coordinates are not available for other pieces that may collide with it
space_avaiable = [
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],]

def reset_space_avaiable(space_avaiable) :
	space_avaiable = [
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],]

def draw_piece(screen, piece, coordenades_x, rotation, fall) :
	rotation += 1 

	# []
	if piece == 1 :
		pygame.draw.rect(screen, yellow, [tetris_panel_X+tetris_panel_width//2+block_size*coordenades_x, tetris_panel_Y+block_size*fall, block_size*2, block_size*2])
	
	# L
	if piece == 2 :
		pygame.draw.rect(screen, blue, [(tetris_panel_X+tetris_panel_width//2)+block_size*coordenades_x, tetris_panel_Y+block_size*fall, block_size, block_size*3])
		pygame.draw.rect(screen, blue, [(tetris_panel_X+tetris_panel_width//2)+block_size*(coordenades_x+1), tetris_panel_Y+block_size*(fall+2), block_size, block_size])

	# J
	if piece == 3 :
		pygame.draw.rect(screen, orange, [(tetris_panel_X+tetris_panel_width//2)+block_size*coordenades_x, tetris_panel_Y+block_size*fall, block_size, block_size*3])
		pygame.draw.rect(screen, orange, [(tetris_panel_X+tetris_panel_width//2)+block_size*(coordenades_x-1), tetris_panel_Y+block_size*(fall+2), block_size, block_size])

	# S
	if piece == 4 :
		pygame.draw.rect(screen, green, [(tetris_panel_X+tetris_panel_width//2)+block_size*coordenades_x, tetris_panel_Y+block_size*fall, block_size, block_size*2])
		pygame.draw.rect(screen, green, [(tetris_panel_X+tetris_panel_width//2)+block_size*(coordenades_x+1), tetris_panel_Y+block_size*(fall+1), block_size, block_size*2])

	# Z
	if piece == 5 :
		pygame.draw.rect(screen, red, [(tetris_panel_X+tetris_panel_width//2)+block_size*coordenades_x, tetris_panel_Y+block_size*fall, block_size, block_size*2])
		pygame.draw.rect(screen, red, [(tetris_panel_X+tetris_panel_width//2)+block_size*(coordenades_x-1), tetris_panel_Y+block_size*(fall+1), block_size, block_size*2])

	# T
	if piece == 6 :
		pygame.draw.rect(screen, purple, [(tetris_panel_X+tetris_panel_width//2)+block_size*coordenades_x, tetris_panel_Y+block_size*fall, block_size, block_size*3])
		pygame.draw.rect(screen, purple, [(tetris_panel_X+tetris_panel_width//2)+block_size*(coordenades_x+1), tetris_panel_Y+block_size*(fall+1), block_size, block_size])