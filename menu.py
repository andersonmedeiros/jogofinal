import pygame


def menu(screen, width, height):
    # centro da tela
    center_x = width/2
    center_y = height/2
    center = (center_x, center_y)

    # centro entre o centro da tela e o topo da tela
    center_top_x = center_x
    center_top_y = center_y/2
    center_top = (center_top_x, center_top_y)

    # centro entre o centro da tela e o fim da tela
    center_bottom_x = center_x
    center_bottom_y = center_y + (center_y/2)
    center_bottom = (center_bottom_x, center_bottom_y)

    close = True
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
            print(event)
