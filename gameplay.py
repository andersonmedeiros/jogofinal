import pygame

pygame.init()

width = 600
height = 600
mode = (width, height)

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Retângulos
player = pygame.Rect(530, 530, 30, 50)
player_2 = pygame.Rect(70, 530, 30, 50)
ground = pygame.Rect(0, 580, 600, 25)
cent_plat = pygame.Rect(125, 400, 350, 35)
cent_upper_plat = pygame.Rect(125, 100, 350, 35)
left_plat = pygame.Rect(0, 250, 100, 35)
right_plat = pygame.Rect(500, 250, 100, 35)

# Auxílios
clock = pygame.time.Clock()
close = True

tela = screen = pygame.display.set_mode(mode)
pygame.display.set_caption("Jogo Final")


while close:
    menu(screen, width, height)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_ip(-10, 0)
            if event.key == pygame.K_RIGHT:
                player.move_ip(10, 0)
            if event.key == pygame.K_UP:
                player.move_ip(0, -10)
            if event.key == pygame.K_DOWN:
                player.move_ip(0, 10)
            # MOVIMENTO DO SEGUNDO PLAYER
            if event.key == pygame.K_a:
                player_2.move_ip(-10, 0)
            if event.key == pygame.K_d:
                player_2.move_ip(10, 0)
            if event.key == pygame.K_w:
                player_2.move_ip(0, -10)
            if event.key == pygame.K_s:
                player_2.move_ip(0, 10)
    tela.fill(green)
    pygame.draw.rect(tela, blue, player_2)
    pygame.draw.rect(tela, red, player)
    pygame.draw.rect(tela, white, ground)
    pygame.draw.rect(tela, white, cent_plat)
    pygame.draw.rect(tela, white, cent_upper_plat)
    pygame.draw.rect(tela, white, left_plat)
    pygame.draw.rect(tela, white, right_plat)
    clock.tick(27)
    pygame.display.update()
pygame.quit()
