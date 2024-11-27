import pygame, sys

def draw_game_start(screen):
    start_title_font = pygame.font.Font("LEMONMILK-Medium.otf", 70)
    button_font = pygame.font.Font("LEMONMILK-Medium.otf", 50)


    screen.blit(bg, (0, 0))

    title_surface = start_title_font.render("Sudoku", 0, "white")
    title_rectangle = title_surface.get_rect(
        center =(1000//2, 603//2 - 150))
    screen.blit(title_surface, title_rectangle)

    easy_text = button_font.render("Easy", 0, (255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

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
                    return
                elif medium_rectangle.collidepoint(event.pos):
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((1000,603))
    bg = pygame.image.load("TL.png")
    # bg and dimensions subject to change, just using it for reference right now
    draw_game_start(screen)
