import pygame


# fonte de texto
def text(msg, cor):
    font = pygame.font.SysFont(None, 30)
    text = font.render(msg, True, cor)
    return text



def show_credits(screen, width, height):
    txt_credits = open("credits.txt", "r")
    list_credits = []
    for credit in txt_credits:
        list_credits.append(credit.strip("\n"))

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill((255, 245, 195))
        screen.blit(text("JOGO FINAL", (0, 0, 0)),
                    [240, 25])
        linha = 70
        for i in range(0, len(list_credits)):
            screen.blit(text(list_credits[i], (0, 0, 0)), [15, linha])
            linha += 30

        pygame.display.update()
