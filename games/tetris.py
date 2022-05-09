import pygame
import sys
pygame.init()

# Create screen
size = (900,850)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TETRIS')

# Create colors
black = (0,0,0)
dark_grey = (40,40,40)
grey = (60,60,60)
light_grey = (100,100,100)
white = (255,255,255)
yellow = (255,204,0)
green = (51,204,51)
dark_purple = (83,0,185)
purple = (153,0,255)
dark_pink = (255,53,155)
pink = (255,153,255)
orange = (255, 153, 0)
red = (255, 57, 57)
blue = (0, 64, 255)
turquoise = (0, 255, 255)

# Create fonts
tetris_font = pygame.font.Font('games\\fonts\\tetris_fonts\\UniformBold.ttf', 100)
font_h1 = pygame.font.Font('games\\fonts\\tetris_fonts\\Gameplay.ttf', 30)
font_h2 = pygame.font.Font('games\\fonts\\tetris_fonts\\Gameplay.ttf', 25)
font_h3 = pygame.font.Font('games\\fonts\\tetris_fonts\\Gameplay.ttf', 20)

# Create strings
tetris_string = 'TETRIS'

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

tetris_label_width = 300
tetris_label_height = 110
tetris_label_X = 300
tetris_label_Y = 75

button_width = 250
button_height = 80

play_button_X = 325
play_button_Y = 350

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

resume_button_X = 325
resume_button_Y = 300
controls_button_X = 325
controls_button_Y = 390
quit_button_X = 325
quit_button_Y = 480

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
def draw_button(x_axis, y_axis, text, active) :
      text = text.center(22)
      if active :
            pygame.draw.rect(screen, purple, [x_axis-3, y_axis-3, button_width+6, button_height+6], border_radius = 20)
            pygame.draw.rect(screen, black, [x_axis, y_axis, button_width, button_height], border_radius = 20)
            button = font_h2.render(text, True, white)
            screen.blit(button, (x_axis, y_axis+20))
      else:
            pygame.draw.rect(screen, pink, [x_axis-2, y_axis-2, button_width+4, button_height+4], border_radius = 20)
            pygame.draw.rect(screen, black, [x_axis, y_axis, button_width, button_height], border_radius = 20)
            button = font_h2.render(text, True, white)
            screen.blit(button, (x_axis, y_axis+20))


def draw_board() :
      pass


def draw_menu(play_button_active):
      # TETRIS LABEL
      pygame.draw.rect(screen, pink, [tetris_label_X-10, tetris_label_Y-10, tetris_label_width+20, tetris_label_height+20])
      pygame.draw.rect(screen, pink, [tetris_label_X+99-10, tetris_label_Y-10, tetris_label_height+20, tetris_label_width-100+20])

      pygame.draw.rect(screen, purple, [tetris_label_X-8, tetris_label_Y-8, tetris_label_width+16, tetris_label_height+16])
      pygame.draw.rect(screen, purple, [tetris_label_X+99-8, tetris_label_Y-8, tetris_label_height+16, tetris_label_width-100+16])

      pygame.draw.rect(screen, pink, [tetris_label_X-2, tetris_label_Y-2, tetris_label_width+4, tetris_label_height+4])
      pygame.draw.rect(screen, pink, [tetris_label_X+99-2, tetris_label_Y-2, tetris_label_height+4, tetris_label_width-100+4])

      pygame.draw.rect(screen, black, [tetris_label_X, tetris_label_Y, tetris_label_width, tetris_label_height])
      pygame.draw.rect(screen, black, [tetris_label_X+99, tetris_label_Y, tetris_label_height, tetris_label_width-100])

      tetris_text = tetris_font.render(tetris_string, True, white)
      screen.blit(tetris_text, (tetris_label_X+18, tetris_label_Y))

      # START BUTTON
      draw_button(play_button_X, play_button_Y, play_string, play_button_active)

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


def draw_panels(pause_button_active) :

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
      if pause_button_active :
            pygame.draw.rect(screen, purple, [pause_button_X-3, pause_button_Y-3, pause_button_size+6, pause_button_size+6], border_radius = 20)
            pygame.draw.rect(screen, black, [pause_button_X, pause_button_Y, pause_button_size, pause_button_size], border_radius = 20)
            pygame.draw.rect(screen, pink, [pause_button_X+30, pause_button_Y+15, 10, 70])
            pygame.draw.rect(screen, pink, [pause_button_X+60, pause_button_Y+15, 10, 70])
      else:
            pygame.draw.rect(screen, pink, [pause_button_X-2, pause_button_Y-2, pause_button_size+4, pause_button_size+4], border_radius = 20)
            pygame.draw.rect(screen, black, [pause_button_X, pause_button_Y, pause_button_size, pause_button_size], border_radius = 20)
            pygame.draw.rect(screen, white, [pause_button_X+30, pause_button_Y+15, 10, 70])
            pygame.draw.rect(screen, white, [pause_button_X+60, pause_button_Y+15, 10, 70])


def draw_pause(in_game):
      print('PAUSE')
      paused = True
      pause_clock = pygame.time.Clock()
      resume_button_active = False
      controls_button_active = False
      quit_button_active = False

      show_controls = False

      while paused:
            pause_clock.tick(30)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():

                  if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                  
                  #KEYCONTROLS
                  if event.type == pygame.KEYDOWN:
                        keys_pressed = pygame.key.get_pressed()
                        if keys_pressed[pygame.K_SPACE]:
                              paused = False

                        elif keys_pressed[pygame.K_ESCAPE] :
                              paused = False

                        elif show_controls :
                              if keys_pressed[pygame.K_ESCAPE]:
                                    show_controls = False
                  
                  #MOUSECONTROLS
                  if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
                              if event.type == pygame.MOUSEBUTTONDOWN : 
                                    paused = False
                  
                  if (resume_button_X <= mouse[0] <= resume_button_X+button_width) and (resume_button_Y <= mouse[1] <= resume_button_Y+button_height) :
                        resume_button_active = True
                        if event.type == pygame.MOUSEBUTTONDOWN : 
                              paused = False
                  else:
                        resume_button_active = False
                  
                  if (controls_button_X <= mouse[0] <= controls_button_X+button_width) and (controls_button_Y <= mouse[1] <= controls_button_Y+button_height) :
                        controls_button_active = True
                        if event.type == pygame.MOUSEBUTTONDOWN :
                              #show_controls = True 
                              pass
                  else:
                        controls_button_active = False

                  if (quit_button_X <= mouse[0] <= quit_button_X+button_width) and (quit_button_Y <= mouse[1] <= quit_button_Y+button_height) :
                        quit_button_active = True
                        if event.type == pygame.MOUSEBUTTONDOWN :
                              if in_game == True : menu()
                              if in_game == False :
                                    # return to main
                                    pygame.quit()
                  else:
                        quit_button_active = False

            # Cover background
            pygame.draw.rect(screen, light_grey, [tetris_panel_X, tetris_panel_Y, tetris_panel_width, tetris_panel_height])

            # Menu
            pygame.draw.rect(screen, pink, [pause_menu_X-2, pause_menu_Y-2, pause_menu_size+4, pause_menu_size+4])
            pygame.draw.rect(screen, black, [pause_menu_X, pause_menu_Y, pause_menu_size, pause_menu_size])
            pause_label = font_h1.render(pause_string, True, white)
            screen.blit(pause_label, (pause_menu_X+125, pause_menu_Y+20))

            # Buttons
            draw_button(resume_button_X, resume_button_Y, resume_string, resume_button_active)
            draw_button(controls_button_X, controls_button_Y, controls_string, controls_button_active)
            draw_button(quit_button_X, quit_button_Y, quit_string, quit_button_active)

            if show_controls :
                  #Show the user the game controls
                  pass

            pygame.display.flip()
      
      if in_game :
            tetris_game()
      else:
            tetris_menu()


## TETRIS MAIN LOOP ##
def tetris_game() :
      print('GAME')
      game_clock = pygame.time.Clock()
      run = True
      pause = False
      pause_button_active = False
      while run :
            game_clock.tick(30)
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        sys.exit()
                  
                  #KEYCONTROLS
                  if event.type == pygame.KEYDOWN:
                        keys_pressed = pygame.key.get_pressed()

                        if keys_pressed[pygame.K_ESCAPE] :
                              pause_button_active = True
                              pause = True

                  #MOUSECONTROLS
                  if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
                        pause_button_active = True
                        if event.type == pygame.MOUSEBUTTONDOWN : pause = True
                  elif pause == False:
                        pause_button_active = False

            # SCREEN ELEMENTS :

            #	- Background :
            screen.fill(black)

            #	- Panels :
            draw_panels(pause_button_active)
            draw_board()
            if pause : draw_pause(in_game=True)


            pygame.display.flip()

## TETRIS MENU LOOP ##
def tetris_menu() :
      menu_clock = pygame.time.Clock()
      run = True
      pause = False
      play = False
      play_button_active = False
      pause_button_active = False
      while run :
            menu_clock.tick(30)
            mouse = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        sys.exit()

                  #KEYCONTROLS
                  if event.type == pygame.KEYDOWN:
                        keys_pressed = pygame.key.get_pressed()

                        if keys_pressed[pygame.K_SPACE] : play = True
                        if keys_pressed[pygame.K_ESCAPE] : 
                              pause_button_active = True
                              pause = True

                  #MOUSECONTROLS
                  if (play_button_X <= mouse[0] <= play_button_X+button_width) and (play_button_Y <= mouse[1] <= play_button_Y+button_height) :
                        play_button_active = True
                        if event.type == pygame.MOUSEBUTTONDOWN : play = True
                  else:
                        play_button_active = False
                  

                  if (pause_button_X <= mouse[0] <= pause_button_X+pause_button_size) and (pause_button_Y <= mouse[1] <= pause_button_Y+pause_button_size) :
                        pause_button_active = True
                        if event.type == pygame.MOUSEBUTTONDOWN : pause = True
                  elif pause == False:
                        pause_button_active = False

            
            # SCREEN ELEMENTS

            # Background :
            screen.fill(black)

            # Panels :
            draw_panels(pause_button_active)
            draw_menu(play_button_active)
            if pause : draw_pause(in_game=False)
            if play : main()


            pygame.display.flip()

tetris_menu()