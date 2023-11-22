from grid import Grid
from blocks import *
import random 
import pygame



    
class Game:
    def __init__(self) -> None: # When the game function is called in the main.py file; This constructor initializes the blocks made 
        self.grid = Grid()
        self.blocks = [Iblock(), Jblock(), Lblock(), Oblock(), Sblock(), Tblock(), Zblock()]
        self.current_block, self.next_block = self.get_random_block(), self.get_random_block() #Randomly choosing blocks using random lib
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("/home/livvv/Desktop/coding playground/tetris-game/Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("/home/livvv/Desktop/coding playground/tetris-game/Sounds/clear.ogg")

        pygame.mixer.music.load("/home/livvv/Desktop/coding playground/tetris-game/Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared >= 3:
            self.score += 500
        self.score += move_down_points

    
    def get_random_block(self): # In order to cycle through all the blocks to reduce biasedness; this function removes the block from the list when it is called
        if len(self.blocks) == 0: #Re-appending all the blocks to its initial stage 
            self.blocks = [Iblock(), Jblock(), Lblock(), Oblock(), Sblock(), Tblock(), Zblock()]
        block = random.choice(self.blocks) #Randomly choosing block 
        self.blocks.remove(block) #Removing block 
        return block # Returining the block to display 

    def draw(self, screen): # Drawing on the screen 
        self.grid.draw(screen) #Using the draw function in the grid.py file 
        self.current_block.draw(screen, 1, 1)
        

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
    
    def move_left(self): #Moves the block 1 cell left 
        self.current_block.move(0, -1)
        if self.block_inside() == False or not self.block_fits():
            self.current_block.move(0,1)

    def move_right(self): #Moves the block 1 cell right 
        self.current_block.move(0, 1)
        if self.block_inside() == False or not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self): #Moves the block one cell down 
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()
            
    def lock_block(self): 
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True
    
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True
    
    def block_inside(self): #Checks whether the block is inside the main screen or not (300 by 600 screen) 
        tiles = self.current_block.get_cell_positions()

        for tile in tiles: 
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self): #Rotates the block 
        self.current_block.rotate()
        # If the rotation excludes the screen it undos the rotation 
        if self.block_inside() == False or not self.block_fits():
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()


    
    def reset(self):
        self.grid.reset()
        self.blocks = [Iblock(), Jblock(), Lblock(), Oblock(), Sblock(), Tblock(), Zblock()]
        self.current_block, self.next_block = self.get_random_block(), self.get_random_block() #Randomly choosing blocks using random lib
        self.score = 0


    



    

