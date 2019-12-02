import pygame
from menu import show_menu
from credits import show_credits

pygame.init()

width = 600
height = 600
mode = (width, height)

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

tela = screen = pygame.display.set_mode(mode)
pygame.display.set_caption("Jogo Final")

close = True
while close:
    op = show_menu(screen, width, height)
    if op == False:
        close = False
    elif op == 1:
        print("PLAY")
    elif op == 2:
        show_credits(screen, width, height)

pygame.quit()
