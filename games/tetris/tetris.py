import pygame, sys
pygame.init()

# Create screen
size = (1000,800)
screen = pygame.display.set_mode(size)

## TETRIS MAIN LOOP ##
while True:

	for event in pygame.event.get():
		print(event)
	
		if event.type == pygame.QUIT:
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			print('Mouse button pressed')