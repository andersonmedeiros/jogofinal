import pygame
import aux


def show_gameover(screen, width, height, acertos):
    pygame.mouse.set_visible(True)
    close = True
    while close:
        

        screen.fill((255, 255, 255))
        aux.text(screen, "GAME OVER!", (255,0,0), 40, 240, 90)
        if acertos == 1:
            aux.text(screen, "VOCÊ ACERTOU: {} PERGUNTA".format(acertos), (0,0,0), 40, 70, 200)
        elif acertos > 1:
            aux.text(screen, "VOCÊ ACERTOU: {} PERGUNTAS".format(acertos), (0,0,0), 40, 70, 200)
        elif acertos == 0:
            aux.text(screen, "{} ACERTOS, TENTE NOVAMENTE!".format(acertos), (0,0,0), 40, 70, 200)
        


        aux.text(screen, "REINICIAR", (255,0,0), 40, 240, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

                if pos[0] >= 240 and \
                        pos[0] <= 480 and \
                        pos[1] >= 550 and pos[1] <= 590:
                    aux.text(screen, "REINICIAR", (255,255,0), 40, 240, 550)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 240 and \
                        pos[0] <= 480 and \
                        pos[1] >= 550 and pos[1] <= 590:
                    return 1

            pygame.display.update()
