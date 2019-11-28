import pygame

pygame.init()

width = 600
height = 600
mode = (width, height)
# Cores

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
# Coordenadas do primeiro player

pos_x1 = 530
pos_y1 = 530
shape = pygame.Rect(pos_x1,pos_y1,30,50)
# Coordenadas do segundo player

pos_x2 = 70
pos_y2 = 530
shape_2 = pygame.Rect(pos_x2,pos_y2,30,50)
clock = pygame.time.Clock()
close = True

tela = screen = pygame.display.set_mode(mode)
pygame.display.set_caption("Jogo Final")


while close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x1-= 10
            if event.key == pygame.K_RIGHT:
                pos_x1+= 10
            if event.key == pygame.K_UP:
                pos_y1-= 10
            if event.key == pygame.K_DOWN:
                pos_y1+= 10
            # MOVIMENTO DO SEGUNDO PLAYER
            if event.key == pygame.K_a:
                pos_x2-= 10
            if event.key == pygame.K_d:
                pos_x2+= 10
            if event.key == pygame.K_w:
                pos_y2-= 10
            if event.key == pygame.K_s:
                pos_y2+= 10
    tela.fill(red)
    pygame.draw.rect(tela, black, shape_2)
    pygame.draw.rect(tela, white, shape)

    clock.tick(27)
    pygame.display.update()
pygame.quit()
