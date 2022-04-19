import pygame, sys
pygame.init()

# Create screen
size = (800, 800)
screen = pygame.display.set_mode(size)

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