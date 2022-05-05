import pygame
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TETRIS')

# Create colors
black = (0,0,0)
grey = (40,40,40)
light_grey = (90,90,90)
#grey_green = (194, 214, 214)
white = (255,255,255)
yellow = (255, 204, 0)
green = (51, 204, 51)
purple = (153, 0, 255)
pink = (255, 153, 255)
dark_pink = (255, 53, 155)#(255, 103, 205)
orange = (255, 153, 0)
red = (179, 0, 0)
blue = (0, 64, 255)
turquoise = (0, 255, 255)

# Create fonts


# Create strings
tetris_string = 'TETRIS'
play_string = 'PLAY'
highscores_string = 'HIGH SCORES'
hold_string = 'HOLD'
next_string = 'NEXT'
score_string = 'SCORE'
lines_string = 'LINES'

pause_string = 'PAUSE'
resume_string = 'RESUME'
controls_string = 'CONTROLS'
quit_string = 'QUIT'



# Panels
tetris_label_width = 300
tetris_label_height = 110
tetris_label_X = 300
tetris_label_Y = 75

highscores_panel_width = 340
highscores_panel_height = 300
highscores_panel_X = 280
highscores_panel_Y = 490

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

pause_menu_size = 350
pause_menu_X = 275
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
def draw_board() :
      pass

def draw_panels(menu, pause) :
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

      if menu :
            # TETRIS LABEL
            pygame.draw.rect(screen, dark_pink, [tetris_label_X-10, tetris_label_Y-10, tetris_label_width+20, tetris_label_height+20])
            pygame.draw.rect(screen, dark_pink, [tetris_label_X+99-10, tetris_label_Y-10, tetris_label_height+20, tetris_label_width-100+20])

            pygame.draw.rect(screen, pink, [tetris_label_X-8, tetris_label_Y-8, tetris_label_width+16, tetris_label_height+16])
            pygame.draw.rect(screen, pink, [tetris_label_X+99-8, tetris_label_Y-8, tetris_label_height+16, tetris_label_width-100+16])

            pygame.draw.rect(screen, dark_pink, [tetris_label_X-2, tetris_label_Y-2, tetris_label_width+4, tetris_label_height+4])
            pygame.draw.rect(screen, dark_pink, [tetris_label_X+99-2, tetris_label_Y-2, tetris_label_height+4, tetris_label_width-100+4])

            pygame.draw.rect(screen, black, [tetris_label_X, tetris_label_Y, tetris_label_width, tetris_label_height])
            pygame.draw.rect(screen, black, [tetris_label_X+99, tetris_label_Y, tetris_label_height, tetris_label_width-100])
            
            # HIGH SCORES TABLE
            pygame.draw.rect(screen, pink, [highscores_panel_X-2, highscores_panel_Y-2, highscores_panel_width+4, highscores_panel_height+4])
            pygame.draw.rect(screen, black, [highscores_panel_X, highscores_panel_Y, highscores_panel_width, highscores_panel_height])


      # 	- Pause panel
      if pause :
            pygame.draw.rect(screen, pink, [pause_menu_X-2, pause_menu_Y-2, pause_menu_size+4, pause_menu_size+4])
            pygame.draw.rect(screen, black, [pause_menu_X, pause_menu_Y, pause_menu_size, pause_menu_size])   

def draw_buttons() :
      pass

## TETRIS MAIN LOOP ##
def main() :
      print('GAME')
      run = True
      pause = False
      while run :
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        run = False

            # SCREEN ELEMENTS :

            #	- Background :
            screen.fill(black)

            #	- Panels :
            draw_panels(False, pause)


            pygame.display.flip()

## TETRIS MENU LOOP ##
def menu() :
      menu_clock = pygame.time.Clock()
      run = True
      pause = False
      while run :
            menu_clock.tick(30)
            
            for event in pygame.event.get():
                  #print(event)
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

            #	- Panels :
            draw_panels(True, pause)


            pygame.display.flip()


menu()
pygame.quit()
exec(open('main.py').read())