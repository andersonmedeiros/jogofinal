import pygame

def text(screen, msg, cor, tam, pos_x, pos_y):
    font = pygame.font.SysFont(None, tam)
    text = font.render(msg, True, cor)
    screen.blit(text, [pos_x, pos_y])