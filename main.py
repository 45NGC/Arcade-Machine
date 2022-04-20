import pygame, sys
pygame.init()

# Create screen
size = (1000,1000)
screen = pygame.display.set_mode(size)

width = screen.get_width()
height = screen.get_height()

# Create colors
black = (0,0,0)
white = (255,255,255)
grey  = (100,100,100)

# Create fonts
title_font = pygame.font.Font('ARCADECLASSIC.TTF', 100)

# Create Strings
title_string = 'ARCADE      MACHINE'

# Functions


# Main loop
# This loop will display a screen with the name 'Arcade Machine' and a scroll of the games we can play, the games will include :
# 	- Tetris
# 	- Snake	
# 	- Pong 
# 	- Connect 4
# 	- Fast Reflexes
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

	mouse = pygame.mouse.get_pos()

	#	- Buttons:
	#		- Tetris
	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
		pygame.draw.rect(screen,white,[width/2,height/2,140,40])
	else:
		pygame.draw.rect(screen,grey,[width/2,height/2,140,40])

	#	- Title:
	title = title_font.render(title_string, True, white)
	screen.blit(title, (100,50))

	pygame.display.flip()