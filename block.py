import pygame
from colors import Colors
from position import Position
class Block:
    # required variables 
    """
    id 
    rotation_state
    cells
    """
    # required methods 
    """
    draw()
    rotate()
    move()
    get_cell_positions()
    undo_rotate()
    """
    def __init__(self, id): 
        self.id = id
        self.rotation_state = 0
        self.cells = {}
        self.cell_size = 30
        self.colors = Colors.get_cell_colors()
        self.row_offset, self.column_offset = 0, 0
    
    def draw(self, screen, offset_x, offset_y): #This function will draw small pixels where tetriminos will fall (20 by 10)
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) # Leaving 1 pixel offset
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) #USing the draw function from the library to draw the blocks
            
    def move(self, rows, columns): #The tetriminos move by one row and column when this function is called. If move(0, 1) is called it will move the pixels 1 column left move(1,0) moves tetriminos 1 block down and if minus is used it will go to the alternate direction 
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []

        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self): #USing the rotation state via dictionary in blocks.py
        self.rotation_state += 1

        if self.rotation_state == len(self.cells): #So it does not increment after 4th rotation state 
            self.rotation_state = 0

    def undo_rotation(self): #IF the block rotates and the tetriminos go ouside the screen this function should be called 
        self.rotation_state -= 1

        if self.rotation_state == 0:  #The length of rotation state is used so the 4th state in the dict is used
            self.rotation_state = len(self.cells) - 1 

 
 