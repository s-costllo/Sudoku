import math,random

import pygame, sys

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0]*9 for i in range(9)]
        self.box_length = int(math.sqrt(row_length))

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for x in range(9):
            for y in range(9):
                print(self.board[x][y], end=" ")
            print("")

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for i in range(9):
            if self.board[row][i] == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for x in range(row_start,row_start+2):
            for y in range(col_start,col_start+2):
                if self.board[x][y] == num:
                    return False
        return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        row_start = int(row//3*3)
        col_start = int(col//3*3)
        if self.valid_in_box(row_start, col_start, num):
            if self.valid_in_row(row, num):
                if self.valid_in_col(col,num):
                    return True
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        x = row_start
        y = col_start
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while True:
            w = random.choice(list)
            self.board[x][y] = w
            list.remove(w)
            if not (list):
                break
            y += 1
            if y == col_start + 3:
                y = col_start
                x += 1

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        x = 0
        while True:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
            if self.board[r][c] == 0:
                continue
            else:
                self.board[r][c] = 0
                x += 1
            if x == self.removed_cells:
                break

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values() 
    board = sudoku.get_board()
    sudoku.remove_cells() #clears some cells to create the puzzle
    board = sudoku.get_board() #gets updated board
    return board #returns the updated puzzle board

#class that represents each cell in Sudoku grid
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = str(value)
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def draw(self):
        number_font = pygame.font.Font("LEMONMILK-Light.otf", 50)

        number_surface = number_font.render(self.value, 1, "black")
        #gets rectangle the number will be placed
	number_rectangle = number_surface.get_rect(
            center=(431 + self.col*67, 33 + self.row*67))
        self.screen.blit(number_surface, number_rectangle)

class SketchCell:
    def __init__(self, value, row, col, screen):
        self.value = str(value)
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def draw(self):

        number_sketch_font = pygame.font.Font("LEMONMILK-Light.otf", 25)

        number_sketch_surface = number_sketch_font.render(self.value, 1, (99, 101, 105))
        #gets rectangle where sketched number will be placed
	number_sketch_rectangle = number_sketch_surface.get_rect(
            center=(415 + self.col * 67, 16 + self.row * 67))
        self.screen.blit(number_sketch_surface, number_sketch_rectangle)

class FilledCell:
    def __init__(self, value, row, col, screen):
        self.value = str(value)
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def draw(self):
        number_font = pygame.font.Font("LEMONMILK-Light.otf", 50)

        number_surface = number_font.render(self.value, 1, (30,46,87))
	#gets rectangle where number will be placed
        number_rectangle = number_surface.get_rect(
            center=(431 + self.col*67, 33 + self.row*67))
        self.screen.blit(number_surface, number_rectangle)

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
	self.board = None
	self.original_board = None

    def draw(self, sudoku, sketch, filled_cell):
        #self.screen.blit(bg, (0, 0))
        #self.screen.fill("black")
        board = pygame.Surface((603, 603))
        board.fill("white")
        self.screen.blit(board, (397, 0))
        for row in range(0, 10, 1):
            pygame.draw.line(self.screen, (99, 101, 105), (397, row * 67), (1000, row * 67))
        for col in range(0, 10, 1):
            pygame.draw.line(self.screen, (99, 101, 105), (col * 67 + 397, 0), (col * 67 + 397, 603))
        for row in range(3, 7, 3):
            pygame.draw.line(self.screen, (99, 101, 105), (397, row * 67), (1000, row * 67), 4)
        for col in range(3, 7, 3):
            pygame.draw.line(self.screen, (99, 101, 105), (col * 67 + 397, 0), (col * 67 + 397, 603), 4)

	#draws numbers in each cell 
        for y in range(9):
            for x in range(9):
                if sudoku[x][y] == 0:
                    continue #skips empty cells
                else:
                    board = Cell(sudoku[x][y],x,y,self.screen)
                    board.draw()
	#draws sketch numbers
        for y in range(9):
            for x in range(9):
                if sketch[x][y] == 0:
                    continue #skips empty cells
                else:
                    board = SketchCell(sketch[x][y],x,y,self.screen)
                    board.draw()
	#draws filled cells
        for y in range(9):
            for x in range(9):
                if filled_cell[x][y] == 0:
                    continue #skips empty cells
                else:
                    board = FilledCell(filled_cell[x][y],x,y,self.screen)
                    board.draw()


    def select(self, row, col):
        #top
        pygame.draw.line(self.screen, (30,46,87), (398+row*67,col*67), (398+row*67+67,col*67),4)
        #left
        pygame.draw.line(self.screen, (30,46,87), (398 + row * 67,  col * 67), (398 + row * 67, col * 67+67), 4)
        #bottom
        pygame.draw.line(self.screen, (30,46,87), (398 + row * 67,  col * 67+67), (398 + row * 67 + 67, col * 67+67), 4)
        #right
        pygame.draw.line(self.screen, (30,46,87), (397 + row * 67+67,  col * 67), (397 + row * 67+67, col * 67+67), 4)

    def click(self, row, col):
	#pixel coordinates to grid coordinates 
        row = (row - 397)//67 #calculates row number
        col = col//67 #calculates column number
        coor = (row, col) #returns selected cell as (row, col)
        return coor

    def clear(self):
	#clears value of selected cell if there
        if self.value is not None:
	    self.value = None
	#clears sketch value if there
	if hasattr(self, "sketch_value") and self.sketch_value is not None:
	    self.sketch_value = None

    def sketch(self, value):
        if not hasattr(self, "sketch_grid"):
	    self.sketch_grid = {} #initializes sketch grid if it doesn't exist yet
	if hasattr(self, "selected_cell") and self.selected_cell is not None:
	    row, col = self.selected_cell
	    self.sketch_grid[(row, col)] = value #sets sketch value for selected cell

    def place_number(self, value):
	#sets value of current selected cell equal to the user entered value 
        row, col = self.selected_cell
	if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
	    self.board[row][col] = value
        else:
            raise IndexError("Selected cell is out of bounds.")

    def set_board(self, board):
	#sets current board state
	self.board = board
	#stores copy of original board to reset later
	self.original_board = []  #initialize an empty list to store  copy of the board
            for row in board:  
            	new_row = row[:]  
            	self.original_board.append(new_row)
		    
    def reset_to_original(self):
	#checks to prevent resetting the board
        if self.original_board is None:
            raise ValueError("Original board is not defined. Please set the board first.")
	#resets board to original state
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col] = self.original_board[row][col]

    def is_full(self, sudoku):
	#checks if board is full 
        for y in range(9):
            for x in range(9):
                if sudoku[x][y] == 0:
                    return False
        return True

    def update_board(self):
	#updates underlying 2D board with values in all cells 
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
		if self.board[row][col] is None:
                self.board[row][col] = 0

    def find_empty(self):
	#finds empty cell and returns row and col as tuple(x,y)
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
		     return (row, col)
	return None 

    def check_board(self, sudoku, sodokuSol):
	#checks if board is solved correctly
        for y in range(9):
            for x in range(9):
                if sudoku[x][y] != sodokuSol[x][y]:
                    return False
        return True
