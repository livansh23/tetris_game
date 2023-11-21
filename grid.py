import pygame
from colors import Colors

class Grid:
    def __init__(self): 
        self.num_rows = 20 #Rows in tetris game 
        self.num_column = 10 # Column in tetris game 
        self.cell_size = 30 # Size of each individual cell in the tetris game 
        self.grid = [[0 for j in range (self.num_column)]for i in range(self.num_rows)] #2D array we will used to represent the grid pattern of tetris 
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows): #iterates through the rows
            for column in range(self.num_column): # iterates through the columns
                print(self.grid[row][column], end = " ") # Printing the 2D array in a grid format 
            print()

    def is_inside(self, row, column): #Checks whether the blocks are inside the screen or not 
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_column: #If you use row <= self.num_rows the block will fall down one cell below the screen
            return True
        return False

    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_column):
                cell_value = self.grid[row][column] 
                cell_rect = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)  
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # Drawing a rectangle as this fucntion will help with collision detection and drawing of tetriminos  

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_column):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_rows(self, row):
        for column in range(self.num_column):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for column in range(self.num_column):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0 
        for row in range(self.num_rows -1, 0, -1):
            if self.is_row_full(row):
                self.clear_rows(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_column):
                self.grid[row][column] = 0





    