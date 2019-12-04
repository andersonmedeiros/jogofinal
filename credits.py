import pygame


# fonte de texto
def text(msg, cor):
    font = pygame.font.SysFont(None, 25)
    text = font.render(msg, True, cor)
    return text


def show_credits(screen, width, height):
    txt_credits = open("credits.txt", "r")
    list_credits = []
    for credit in txt_credits:
        list_credits.append(credit.strip("\n"))

    close = True
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill((255, 255, 255))
        screen.blit(text("JOGO FINAL", (0, 0, 0)),
                    [240, 25])
        linha = 70
        for i in range(0, len(list_credits)):
            screen.blit(text(list_credits[i], (0, 0, 0)), [15, linha])
            linha += 30

        pygame.display.update()
