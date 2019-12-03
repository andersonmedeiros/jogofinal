import pygame
import aux
# paddle = pygame.Rect(285, pos_y_result, 80, 30)
pos_x = 285
pos_y = 505
paddle = pygame.Rect(285, 505, 80, 30)

#def move_paddle_left():


def gameplay(screen, width, height):
    close = True
    while close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False

        # placar --score
        pos_y_score = height - 50        
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), [0, pos_y_score, width, 50])
        aux.text(screen, "SCORE: ", (255, 255, 255), 25, 25, pos_y_score + 15)

        # raquete --result
        pos_x_result = 285
        pos_y_result = pos_y_score - 45

        pygame.draw.rect(screen, (0, 0, 0), paddle)
        aux.text(screen, "RESULT", (255, 255, 255), 25, pos_x_result + 7, pos_y_result + 6)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if paddle[0] > 0:
                        paddle.move_ip(-10, 0)
                if event.key == pygame.K_RIGHT:
                    if paddle[0] < width - paddle[2]:
                        paddle.move_ip(10, 0)
