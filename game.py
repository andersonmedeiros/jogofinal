import pygame
import aux
from random import randint
# paddle = pygame.Rect(285, pos_y_result, 80, 30)
pos_x = 285
pos_y = 505
paddle = pygame.Rect(285, 505, 80, 30)
0
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
        print(i)
        respostas.append(randint(0, 200))

    return respostas

def gameplay(screen, width, height):
    clock = pygame.time.Clock()
    close = True
    lists = gerar_pergunta(randint(1, 20))

    resposta1 = pygame.Rect(65, 60, 40, 30)
    resposta2 = pygame.Rect(215, 60, 40, 30)
    resposta3 = pygame.Rect(365, 60, 40, 30)
    resposta4 = pygame.Rect(515, 60, 40, 30)

    respostas = []
    respostas = resposta()
    pos = randint(0, 4)
    i = score = 0
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
        screen.fill((255, 255, 255))

        # placar --score
        pos_y_score = height - 50
        pygame.draw.rect(screen, (0, 0, 0), [0, pos_y_score, width, 50])


        pygame.draw.rect(screen, (0, 0, 0), [0, 0, width, 50])
        aux.text(screen, "PERGUNTA: {} + {}".format(lists[i][0], lists[i][1]), (255, 255, 255), 25, 25, 15)


        respostas[pos] = lists[i][2]

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
            if respostas[0] == lists[i][2]:
                print("Acertou 1")
                score += 1
                i += 1

        if y_resposta2 + 30 == y_paddle and x_resposta2 >= x_paddle and x_resposta2 + 40 <= x_paddle + 80:
            if respostas[1] == lists[i][2]:
                print("Acertou 2")
                score += 1
                i += 1

        if y_resposta3 + 30 == y_paddle and x_resposta3 >= x_paddle and x_resposta3 + 40 <= x_paddle + 80:
            if respostas[2] == lists[i][2]:
                print("Acertou 3")
                score += 1
                i += 1

        if y_resposta4 + 30 == y_paddle and x_resposta4 >= x_paddle and x_resposta4 + 40 <= x_paddle + 80:
            if respostas[3] == lists[i][2]:
                print("Acertou 4")
                score += 1
                i += 1

        aux.text(screen, "SCORE: {}".format(score), (255, 255, 255), 25, 25, pos_y_score + 15)
        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if paddle[0] > 0:
                        paddle.move_ip(-10, 0)
                if event.key == pygame.K_RIGHT:
                    if paddle[0] < width - paddle[2]:
                        paddle.move_ip(10, 0)
