import pygame
pygame.init()

# COLORS
black = (0,0,0)
white = (255,255,255)
pink = (255, 153, 255)
red_pink = (255, 0, 102)
purple = (153,0,255)

# FONTS
button1_font = pygame.font.Font('resources\\fonts\\main_fonts\\Ode to Idle Gaming.ttf', 30)
button2_font = pygame.font.Font('resources\\fonts\\tetris_fonts\\Gameplay.ttf', 25)

# BUTTONS
button1_width = 244
button1_height = 74

def draw_button1(screen, x_axis, y_axis, text, mouse, i_text_animation) :
	text = text.center(12)
	text_animation_array = [0,1,2,3,4,5,4,3,2,1]
	
	if(x_axis <= mouse[0] <= x_axis+button1_width) and (y_axis <= mouse[1] <= y_axis+button1_height) :
		pygame.draw.rect(screen, pink, [x_axis, y_axis, button1_width+6,button1_height+6], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis+5, y_axis+5, button1_width-4,button1_height-4], border_radius = 20)
		button = button1_font.render(text, True, red_pink)
		screen.blit(button, (x_axis+5 , y_axis+10 + text_animation_array[i_text_animation]))
	else:
		pygame.draw.rect(screen, white, [x_axis, y_axis, button1_width+6,button1_height+6], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis+3, y_axis+3, button1_width,button1_height], border_radius = 20)
		button = button1_font.render(text, True, white)
		screen.blit(button, (x_axis+5,y_axis+10))



def draw_button2(screen, x_axis, y_axis, button_width, button_height, text, active) :
	text = text.center(22)

	if active :
		pygame.draw.rect(screen, purple, [x_axis-3, y_axis-3, button_width+6, button_height+6], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis, y_axis, button_width, button_height], border_radius = 20)
		button = button2_font.render(text, True, white)
		screen.blit(button, (x_axis, y_axis+20))
	else:
		pygame.draw.rect(screen, pink, [x_axis-2, y_axis-2, button_width+4, button_height+4], border_radius = 20)
		pygame.draw.rect(screen, black, [x_axis, y_axis, button_width, button_height], border_radius = 20)
		button = button2_font.render(text, True, white)
		screen.blit(button, (x_axis, y_axis+20))