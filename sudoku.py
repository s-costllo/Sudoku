import pygame, sys
from sudoku_generator import *
import copy

def draw_game_start(screen):
    start_title_font = pygame.font.Font("LEMONMILK-Medium.otf", 70)
    button_font = pygame.font.Font("LEMONMILK-Medium.otf", 50)

    screen.blit(bg, (0, 0))
    #screen.fill("black")

    title_surface = start_title_font.render("Sudoku", 1, "white")
    title_rectangle = title_surface.get_rect(
        center =(1000//2, 603//2 - 150))
    screen.blit(title_surface, title_rectangle)

    diff_surface = button_font.render("Select difficulty:", 1, "white")
    diff_rectangle = diff_surface.get_rect(
        center=(1000 // 2, 603 // 2+30 ))
    screen.blit(diff_surface, diff_rectangle)

    easy_text = button_font.render("Easy", 1, (255,255,255))
    medium_text = button_font.render("Medium", 1, (255,255,255))
    hard_text = button_font.render("Hard", 1, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill((30,46,87))
    easy_surface.blit(easy_text, (10,10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill((30,46,87))
    medium_surface.blit(medium_text, (10,10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill((30, 46, 87))
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(
        center=(1000//2-250, 603//2+150))
    medium_rectangle = medium_surface.get_rect(
        center=(1000//2, 603//2+150))
    hard_rectangle = easy_surface.get_rect(
        center=(1000 // 2 + 250, 603 // 2 + 150))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()

def game(screen):
    screen.blit(bg, (0, 0))
    #screen.fill("black")

    button_font = pygame.font.Font("LEMONMILK-Medium.otf", 50)
    number_font = pygame.font.Font("LEMONMILK-Light.otf", 50)

    #reset, restart, exit buttons
    reset_text = button_font.render("reset", 1, (255, 255, 255))
    restart_text = button_font.render("restart", 1, (255, 255, 255))
    exit_text = button_font.render("exit", 1, (255, 255, 255))

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill((30, 46, 87))
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((30, 46, 87))
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((30, 46, 87))
    exit_surface.blit(exit_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(
        center=(397 // 2 , 603 // 2 - 175))
    screen.blit(reset_surface, reset_rectangle)
    restart_rectangle = restart_surface.get_rect(
        center=(397 // 2, 603 // 2 + 5))
    screen.blit(restart_surface, restart_rectangle)
    exit_rectangle = exit_surface.get_rect(
        center=(397 // 2, 603 // 2 + 175))
    screen.blit(exit_surface, exit_rectangle)

    board.draw(sudoku)

    #running
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rectangle.collidepoint(event.pos):
                    return 1
                elif restart_rectangle.collidepoint(event.pos):
                    return 2
                elif exit_rectangle.collidepoint(event.pos):
                    return 3
                else:
                    x = event.pos[0]
                    y = event.pos[1]
                    #print(x,y)
                    coor = board.click(x, y)
                    print(coor)
                    board.draw(sudoku)
                    board.select(coor[0],coor[1]+1)
        pygame.display.update()


def draw_game_over(screen):
    #screen.fill("black")
    screen.blit(bg, (0, 0))
    start_title_font = pygame.font.Font("LEMONMILK-Medium.otf", 70)
    button_font = pygame.font.Font("LEMONMILK-Medium.otf", 50)

    title_surface = start_title_font.render("Game Lost :((((", 1, "white")
    title_rectangle = title_surface.get_rect(
        center=(1000 // 2, 603 // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    exit_text = button_font.render("exit", 1, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((30, 46, 87))
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(1000 // 2, 603 // 2 + 175))
    screen.blit(exit_surface, exit_rectangle)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


def draw_game_won(screen):
    #screen.fill("black")
    screen.blit(bg, (0, 0))
    start_title_font = pygame.font.Font("LEMONMILK-Medium.otf", 70)
    button_font = pygame.font.Font("LEMONMILK-Medium.otf", 50)

    title_surface = start_title_font.render("Game Won!!!", 1, "white")
    title_rectangle = title_surface.get_rect(
        center=(1000 // 2, 603 // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    restart_text = button_font.render("restart", 1, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((30, 46, 87))
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(1000 // 2, 603 // 2 + 175))
    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    return 2
        pygame.display.update()

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((1000,603))
    bg = pygame.image.load("TL.png")
    # bg and dimensions subject to change, just using it for reference right now

    while True:

        diff = draw_game_start(screen)
        board = Board(9, 9, screen, diff)
        #sudoku = generate_sudoku(9, diff)
        sudoku = SudokuGenerator(9, diff)
        sudoku.fill_values()
        sudokuR = copy.deepcopy(sudoku)
        sudokuSol = sudoku.get_board()
        sudokuR.remove_cells()
        sudoku = sudokuR.get_board()
        sudokuO = copy.deepcopy(sudoku)

        '''
        for x in range(9):
            for y in range(9):
                print(sudokuSol[x][y], end=" ")
            print("")
        print("")
        '''

        for x in range(9):
            for y in range(9):
                print(sudoku[x][y], end=" ")
            print("")
        print("")

        boardOption = game(screen)

        if boardOption == 1:
            #just testing game won and game lost screens
            draw_game_won(screen)
        elif boardOption == 2:
            draw_game_over(screen)
        elif boardOption == 3:
            sys.exit()

        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_rectangle.collidepoint(event.pos):
                        x = 1
                    elif restart_rectangle.collidepoint(event.pos):
                        x = 2
                    elif exit_rectangle.collidepoint(event.pos):
                        sys.exit()
            pygame.display.update()
        '''
        '''
        diff = draw_game_start(screen)
        if diff == 1:
            boardOption = draw_game(screen)
        if diff == 2:
            boardOption = draw_game(screen)
        if diff == 3:
            boardOption = draw_game(screen)
        '''
    




