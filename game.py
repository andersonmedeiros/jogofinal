import pygame
import aux
from gameover import show_gameover
from random import randint
# paddle = pygame.Rect(285, pos_y_result, 80, 30)
pos_x = 285
pos_y = 505
paddle = pygame.Rect(285, 505, 80, 30)

def gerar_pergunta(qtde):
    lists = []
    for i in range(0, qtde):
        a = randint(0, 100)
        b = randint(0, 100)
        result = a + b
        lists.append([a, b, result])
    return lists


def resposta():
    respostas = []
    for i in range(0, 4):
        respostas.append(randint(0, 200))

    return respostas

def gameplay(screen, width, height):
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    close = True
    pygame.mixer.__init__
    correct = pygame.mixer.Sound('correct.wav')

    wrong = pygame.mixer.Sound('wrong.wav')

    background = pygame.mixer.Sound('background.wav')

    background.play()

    backimage = pygame.image.load('backfolder.jpeg')

    spriteimage = pygame.image.load('meteor.png')

    resposta1 = pygame.Rect(65, 60, 40, 30)
    resposta2 = pygame.Rect(215, 60, 40, 30)
    resposta3 = pygame.Rect(365, 60, 40, 30)
    resposta4 = pygame.Rect(515, 60, 40, 30)

    respostas = []
    respostas = resposta()
    pos = randint(0, 3)
    i = score = 0
    lives = 5
    lists = gerar_pergunta(1)
    velocidade = 60

    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
        screen.fill((255, 255, 255))
        screen.blit(backimage, (0, 0))

        # placar --score
        pos_y_score = height - 50
        pygame.draw.rect(screen, (0, 0, 0), [0, pos_y_score, width, 50])


        pygame.draw.rect(screen, (0, 0, 0), [0, 0, width, 50])
        aux.text(screen, "PERGUNTA: {} + {}".format(lists[0][0], lists[0][1]), (255, 255, 255), 25, 25, 15)


        respostas[pos] = lists[0][2]

        pygame.draw.rect(screen, (0, 0, 0), resposta1)
        x_resposta1 = resposta1[0]
        y_resposta1 = resposta1[1]
        aux.text(screen, "{}".format(respostas[0]), (150, 150, 150), 25, 70, 68)
        resposta1.move_ip(0, 1)

        pygame.draw.rect(screen, (0, 0, 0), resposta2)
        x_resposta2 = resposta2[0]
        y_resposta2 = resposta2[1]
        aux.text(screen, "{}".format(respostas[1]), (150, 150, 150), 25, 220, 68)
        resposta2.move_ip(0, 1)

        pygame.draw.rect(screen, (0, 0, 0), resposta3)
        x_resposta3 = resposta3[0]
        y_resposta3 = resposta3[1]
        aux.text(screen, "{}".format(respostas[2]), (150, 150, 150), 25, 370, 68)
        resposta3.move_ip(0, 1)

        pygame.draw.rect(screen, (0, 0, 0), resposta4)
        x_resposta4 = resposta4[0]
        y_resposta4 = resposta4[1]
        aux.text(screen, "{}".format(respostas[3]), (150, 150, 150), 25, 520, 68)
        resposta4.move_ip(0, 1)

        # raquete --result
        pos_x_result = 285
        pos_y_result = pos_y_score - 45

        pygame.draw.rect(screen, (0, 0, 0), paddle)
        x_paddle = paddle[0]
        y_paddle = paddle[1]
        aux.text(screen, "RESULT", (255, 255, 255), 25, pos_x_result + 7, pos_y_result + 6)

        if y_resposta1 + 30 == y_paddle and x_resposta1 >= x_paddle and x_resposta1 + 40 <= x_paddle + 80:
            if respostas[0] == lists[0][2]:
                correct.play()
                score += 1
                i += 1
                resposta1.move_ip(0, -440)
                resposta2.move_ip(0, -440)
                resposta3.move_ip(0, -440)
                resposta4.move_ip(0, -440)
                lists = gerar_pergunta(1)
                pos = randint(0, 3)
                respostas = resposta()
                if velocidade < 180:
                    velocidade += 5
            else:
                wrong.play()
                op = show_gameover(screen, 600, 600, score)
                if op == 1:
                    gameplay(screen, width, height)

        if y_resposta2 + 30 == y_paddle and x_resposta2 >= x_paddle and x_resposta2 + 40 <= x_paddle + 80:
            if respostas[1] == lists[0][2]:
                correct.play()
                score += 1
                i += 1
                resposta1.move_ip(0, -440)
                resposta2.move_ip(0, -440)
                resposta3.move_ip(0, -440)
                resposta4.move_ip(0, -440)
                lists = gerar_pergunta(1)
                pos = randint(0, 3)
                respostas = resposta()
                if velocidade < 180:
                    velocidade += 5
            else:
                wrong.play()
                op = show_gameover(screen, 600, 600, score)
                if op == 1:
                    gameplay(screen, width, height)

        if y_resposta3 + 30 == y_paddle and x_resposta3 >= x_paddle and x_resposta3 + 40 <= x_paddle + 80:
            if respostas[2] == lists[0][2]:
                correct.play()
                score += 1
                i += 1
                resposta1.move_ip(0, -440)
                resposta2.move_ip(0, -440)
                resposta3.move_ip(0, -440)
                resposta4.move_ip(0, -440)
                lists = gerar_pergunta(1)
                pos = randint(0, 3)
                respostas = resposta()
                if velocidade < 180:
                    velocidade += 5
            else:
                wrong.play()
                op = show_gameover(screen, 600, 600, score)
                if op == 1:
                    gameplay(screen, width, height)

        if y_resposta4 + 30 == y_paddle and x_resposta4 >= x_paddle and x_resposta4 + 40 <= x_paddle + 80:
            if respostas[3] == lists[0][2]:
                correct.play()
                score += 1
                i += 1
                resposta1.move_ip(0, -440)
                resposta2.move_ip(0, -440)
                resposta3.move_ip(0, -440)
                resposta4.move_ip(0, -440)
                lists = gerar_pergunta(1)
                pos = randint(0, 3)
                respostas = resposta()
                if velocidade < 180:
                    velocidade += 5
            else:
                wrong.play()
                op = show_gameover(screen, 600, 600, score)
                if op == 1:
                    gameplay(screen, width, height)

        aux.text(screen, "SCORE: {}".format(score), (255, 255, 255), 25, 25, pos_y_score + 15)
        clock.tick(velocidade)
        pygame.display.update()

        x_paddle, y_paddle = pygame.mouse.get_pos()
        paddle[0] = x_paddle


        if y_resposta1 == 480:            
            resposta1.move_ip(0, -440)
            resposta2.move_ip(0, -440)
            resposta3.move_ip(0, -440)
            resposta4.move_ip(0, -440)
            pos = randint(0, 3)
            respostas = resposta()
            lives -= 1

        if lives == 0:
            close = False

        if close == False:
            #background.stop()
            pygame.mouse.set_visible(True)
