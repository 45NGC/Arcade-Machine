import pygame
pygame.init()

# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
red_pink = (255, 0, 102)
purple = (153,0,255)

# FONTS
buttons_font = pygame.font.Font('resources\\fonts\\main_fonts\\Ode to Idle Gaming.ttf', 30)
buttons2_font = pygame.font.Font('resources\\fonts\\tetris_fonts\\Gameplay.ttf', 25)

# BUTTONS

def draw_button(screen, x_axis, y_axis, text, active, text_animation) :
	text = text.center(12)

	if active :
		pygame.draw.rect(screen, pink, [x_axis, y_axis, 250,80], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, 240,70], border_radius = 20)
		button = buttons_font.render(text, True, red_pink)
		screen.blit(button, (x_axis+5 , y_axis+10 + text_animation))
	else :
		pygame.draw.rect(screen, white, [x_axis, y_axis, 250,80], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis+3, y_axis+3, 244,74], border_radius = 20)
		button = buttons_font.render(text, True, white)
		screen.blit(button, (x_axis+5,y_axis+10))



def draw_button2(screen, x_axis, y_axis, button_width, button_height, text, active) :
	text = text.center(22)

	if active :
		pygame.draw.rect(screen, purple, [x_axis-3, y_axis-3, button_width+6, button_height+6], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis, y_axis, button_width, button_height], border_radius = 20)
		button = buttons2_font.render(text, True, white)
		screen.blit(button, (x_axis, y_axis+20))
	else:
		pygame.draw.rect(screen, pink, [x_axis-2, y_axis-2, button_width+4, button_height+4], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis, y_axis, button_width, button_height], border_radius = 20)
		button = buttons2_font.render(text, True, white)
		screen.blit(button, (x_axis, y_axis+20))