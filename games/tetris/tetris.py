import pygame
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TETRIS')

# Create colors
black = (0,0,0)
grey = (90,90,90)
grey_green = (194, 214, 214)
white = (255,255,255)
yellow = (255, 204, 0)
green = (51, 204, 51)
purple = (153, 0, 255)
pink = (255, 153, 255)
orange = (255, 153, 0)
red = (179, 0, 0)
blue = (0, 64, 255)
turquoise = (0, 255, 255)

# Panels
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

pause_button_size = 100
pause_button_X = 725
pause_button_Y = 650

pause_menu_size = 300
pause_menu_x = 300
pause_menu_Y = 200

# Buttons

# Block
block_size = 40

# Pieces
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


# Functions
def hide_buttons_panels() :
	pass

def show_buttons_panels(pause) :
      #	- Background:
      screen.fill(black)

      # 	- Tetris panel
      pygame.draw.rect(screen, pink, [tetris_panel_X-2, tetris_panel_Y-2, tetris_panel_width+4, tetris_panel_height+4])
      pygame.draw.rect(screen, grey, [tetris_panel_X, tetris_panel_Y, tetris_panel_width, tetris_panel_height])

      # 	- Hold panel
      pygame.draw.rect(screen, pink, [hold_panel_X-2, hold_panel_Y-2, hold_panel_width+4, hold_panel_height+4])
      pygame.draw.rect(screen, grey, [hold_panel_X, hold_panel_Y, hold_panel_width, hold_panel_height])

      # 	- Score panel
      pygame.draw.rect(screen, pink, [score_panel_X-2, score_panel_Y-2, score_panel_width+4, score_panel_height+4])
      pygame.draw.rect(screen, grey, [score_panel_X, score_panel_Y, score_panel_width, score_panel_height])

      # 	- Next panel
      pygame.draw.rect(screen, pink, [next_panel_X-2, next_panel_Y-2, next_panel_width+4, next_panel_height+4])
      pygame.draw.rect(screen, grey, [next_panel_X, next_panel_Y, next_panel_width, next_panel_height])

      # 	- Pause panel
      pygame.draw.rect(screen, pink, [pause_button_X-2,pause_button_Y-2, pause_button_size+4, pause_button_size+4])
      pygame.draw.rect(screen, grey, [pause_button_X, pause_button_Y, pause_button_size, pause_button_size])

      if pause :
            pygame.draw.rect(screen, pink, [pause_button_X+30, pause_button_Y+15, 10, 70])
            pygame.draw.rect(screen, pink, [pause_button_X+60, pause_button_Y+15, 10, 70])
      else :
            pygame.draw.rect(screen, white, [pause_button_X+30, pause_button_Y+15, 10, 70])
            pygame.draw.rect(screen, white, [pause_button_X+60, pause_button_Y+15, 10, 70])

## TETRIS MAIN LOOP ##
def main() :
      print('GAME')

## TETRIS MENU LOOP ##
def menu() :
      menu_clock = pygame.time.Clock()
      run = True
      pause = False
      while run :
            menu_clock.tick(60)
            
            for event in pygame.event.get():
                  #print(event)
                  print('\nPause -> '+str(pause)+'\n')
                  if event.type == pygame.QUIT:
                        run = False

                  if event.type == pygame.KEYDOWN:
                        keys_pressed = pygame.key.get_pressed()
                        if keys_pressed[pygame.K_SPACE]:
                              main()

                        if keys_pressed[pygame.K_ESCAPE] :
                              if pause == False : 
                                    pause = True
                              else :
                                    pause = False

            
            # SCREEN ELEMENTS :

            #	- Background:
            screen.fill(black)

            #	- Buttons:
            show_buttons_panels(pause)

            pygame.display.flip()


menu()
pygame.quit()
exec(open('main.py').read())