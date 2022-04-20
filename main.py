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
		print(event)
	
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
		pygame.draw.rect(screen,white,[100,350,250,80])
	else:
		pygame.draw.rect(screen,grey,[100,350,250,80])

	# Snake
	if (100 <= mouse[0] <= 350) and (550 <= mouse[1] <= 630) :
		pygame.draw.rect(screen,white,[100,550,250,80])
	else:
		pygame.draw.rect(screen,grey,[100,550,250,80])

	# Pong
	if (100 <= mouse[0] <= 350) and (750 <= mouse[1] <= 830) :
		pygame.draw.rect(screen,white,[100,750,250,80])
	else:
		pygame.draw.rect(screen,grey,[100,750,250,80])

	# Connect 4
	if (650 <= mouse[0] <= 900) and (350 <= mouse[1] <= 430) :
		pygame.draw.rect(screen,white,[650,350,250,80])
	else:
		pygame.draw.rect(screen,grey,[650,350,250,80])

	# Fast Reflexes
	if (650 <= mouse[0] <= 900) and (550 <= mouse[1] <= 630) :
		pygame.draw.rect(screen,white,[650,550,250,80])
	else:
		pygame.draw.rect(screen,grey,[650,550,250,80])

	# Infection
	if (650 <= mouse[0] <= 900) and (750 <= mouse[1] <= 830) :
		pygame.draw.rect(screen,white,[650,750,250,80])
	else:
		pygame.draw.rect(screen,grey,[650,750,250,80])


	#	- Title:
	title = title_font.render(title_string, True, white)
	screen.blit(title, (100,50))

	pygame.display.flip()