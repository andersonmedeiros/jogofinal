import pygame


# fonte de texto
def text(msg, cor):
    font = pygame.font.SysFont(None, 40)
    text = font.render(msg, True, cor)
    return text


def show_menu(screen, width, height):
    # centro da tela
    center_x = width/3
    center_y = height/2

    # centro entre o centro da tela e o topo da tela
    center_top_x = center_x
    center_top_y = center_y/2

    # centro entre o centro da tela e o fim da tela
    center_bottom_x = center_x
    center_bottom_y = center_y + (center_y/2)

    close = True
    while close:
        screen.fill((255, 255, 255))
        screen.blit(text("JOGO FINAL", (0, 0, 0)),
                    [center_top_x + 10, center_top_y-40])
        screen.blit(text("PLAY", (0, 0, 0)), [center_x + 60, center_y])
        screen.blit(text("CREDITS", (0, 0, 0)),
                    [center_bottom_x + 30, center_bottom_y+40])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                if pos[0] >= center_x + 60 and \
                        pos[0] <= 2 * (center_x + 60) and \
                        pos[1] >= center_y and pos[1] <= center_y + 30:
                    screen.blit(text("PLAY", (150, 95, 45)),
                                [center_x+60, center_y])
                elif pos[0] >= center_bottom_x + 30 and \
                        pos[0] <= 2 * (center_bottom_x + 30) and \
                        pos[1] >= center_bottom_y + 40 and \
                        pos[1] <= center_bottom_y + 40 + 30:
                    screen.blit(text("CREDITS", (150, 95, 45)),
                                [center_bottom_x+30, center_bottom_y+40])

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if pos[0] >= center_x + 60 and \
                        pos[0] <= 2 * (center_x + 60) and \
                        pos[1] >= center_y and pos[1] <= center_y + 30:
                    return 1
                elif pos[0] >= center_bottom_x + 30 and \
                        pos[0] <= 2 * (center_bottom_x + 30) and \
                        pos[1] >= center_bottom_y + 40 and \
                        pos[1] <= center_bottom_y + 40 + 30:
                    return 2

            pygame.display.update()
