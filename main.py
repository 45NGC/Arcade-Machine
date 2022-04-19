import pygame, sys
pygame.init()

# Create screen
size = (1000, 1000)
screen = pygame.display.set_mode(size)

# Create colors
black = (0,0,0)
white = (255,255,255)

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
	
	# SCREEN ELEMENTS :

	#	- Background:
	screen.fill(black)

	#	- Title:
	title = title_font.render(title_string, True, white)
	screen.blit(title, (100,50))

	pygame.display.flip()