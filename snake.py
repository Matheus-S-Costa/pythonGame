import pygame
from pygame.locals import *
from random import randint


#Funcoes de ajuda
def on_grid_random():
    x = randint(0, 59)
    y = randint(0, 47)
    return (x * 10, y * 10)


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


# Definir movimento da cobra
ALTO = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav') #definindo as musicas

screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('Snake Game')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10)) #tamanho inicial
snake_skin.fill((0, 255, 0))  # verde

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10)) #tamanho maca
apple.fill((255, 0, 0)) #vermelha

my_direction = ESQUERDA

clock = pygame.time.Clock()

font = pygame.font.SysFont('ComicCarToon', 32, bold=True, italic=True)
score = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != BAIXO:
                my_direction = ALTO
            if event.key == K_DOWN and my_direction != ALTO:
                my_direction = BAIXO
            if event.key == K_LEFT and my_direction != DIREITA:
                my_direction = ESQUERDA
            if event.key == K_RIGHT and my_direction != ESQUERDA:
                my_direction = DIREITA

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score = score + 1
        barulho_colisao.play()

    #checa se a cobra colidiu com a parede
    if snake[0][0] == 600 or snake[0][1] == 480 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        pygame.mixer.music.stop() #parar a musica ao perder
        break

    # checa se a cobra colidiu com si mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break


    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # Realiza o movimento da cobra
    if my_direction == ALTO:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == BAIXO:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == DIREITA:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == ESQUERDA:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    for x in range(0, 600, 10):  # Desenha grid (linha)
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):  # Desenha gri vertical
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.SysFont('Comic CarToon', 50, bold=True)
    game_over_screen = game_over_font.render('Você perdeu :(', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 200)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()