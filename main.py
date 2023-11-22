import pygame, sys
from game import Game
from colors import Colors
import requests
from io import BytesIO


pygame.init() # Initialization 

img_url = "https://as1.ftcdn.net/v2/jpg/02/44/66/64/1000_F_244666489_NV7K6OK24CZsNLxCgWUHpGdPuukN3YIH.jpg"
response = requests.get(img_url)
img_data = BytesIO(response.content)


title_font = pygame.font.Font(None, 41)
second_font = pygame.font.Font(None, 15)

score_surface = title_font.render("Score", True, (255, 255, 255))
next_surface = title_font.render("Next", True, (255, 255, 255))
game_over = title_font.render("Game Over", True, Colors.white)
game_over_text = second_font.render("Press Any Key to Restart", True, Colors.white)


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

blue = (44,44, 127) 
black = (0, 0, 0)


# Setting up the game loop so it runs until X(exit) is pressed
# width, height = 300, 600 # The width and height of the game; Declared here because it needs to be used in other places too
screen = pygame.display.set_mode((500, 620)) # This line sets the main window of the game and is not responsive
pygame.display.set_caption("Tetris") # This sets the title of the game; In tetris case only "Tetris" will be used

# Adding icon of the game 
icon = pygame.image.load(img_data)
pygame.display.set_icon(icon)


clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT + 1   #This line sets up custom event so the Tetris block falls automatically every 200 ms rather than when the down arrow key is pressed 

if game.score < 500:
    pygame.time.set_timer(GAME_UPDATE, 200) #Creating a timer that will create the GAME_UPDATE function every 200 ms 
elif game.score > 500 and game.score < 999:
    pygame.time.set_timer(GAME_UPDATE, 700)
elif game.score > 1000 and game.score < 1999:
    pygame.time.set_timer(GAME_UPDATE, 1000)
elif game.score > 2000 and game.score < 4999:
    pygame.time.set_timer(GAME_UPDATE, 1300)
else:
    pygame.time.set_timer(GAME_UPDATE, 1600)
  
game_over_update = pygame.USEREVENT + 2
pygame.time.set_timer(game_over_update, 1000)

# Setting up the game loop so game continues to run until X is pressed 
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pygame.Quit means the user pressed X to close window 
            pygame.quit()
            sys.exit()

        #keyboard event
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()

            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()

            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
            
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
            #game.lock_block()
    
    
    
    # Drawing grids and background 
    
    score_value_surface = title_font.render(str(game.score), True, Colors.black)

    screen.fill(Colors.grey) # This is the background color of the tetris game 
    pygame.draw.rect(screen, Colors.light_grey, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_grey, next_rect, 0, 10)
    
    
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

#Conditional to display the game over text only when game is actually over
    if game.game_over == True:
        screen.blit(game_over, (320, 450, 50, 50))
        screen.blit(game_over_text, (320, 480, 50, 50))  # Display the text

        
    pygame.draw.rect(screen, Colors.light_grey, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)
    #if event.type == game_over_update:
        #screen.fill((0, 0, 0))  # Clear the screen
        #pygame.display.flip()  # Update the display

    game.draw(screen)
    #game.move_down()
    
    pygame.display.update()

    clock.tick(120) # This is the max FPS of the game 

pygame.quit()

    


    


