import pygame

pygame.init()

width = 600
height = 600
mode = (width, height)

screen = pygame.display.set_mode(mode)
pygame.display.set_caption("Jogo Final")


while True:
    pygame.display.flip()
pygame.quit()
